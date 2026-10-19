// Complete page scripts; linkedom provides DOM, no estimator reimplementation.
const fs=require('fs'),vm=require('vm'),path=require('path');
const {parseHTML}=require('linkedom');
const variant=process.argv[2]||'original',root=`app-${variant}`;
const html=fs.readFileSync(`${root}/component-nma/index.html`,'utf8');
const {window,document}=parseHTML(html),blobs=new Map(),downloads=[];
const fakeURL={createObjectURL(b){const k='blob:audit-'+blobs.size;blobs.set(k,b);return k;},revokeObjectURL(){}};
const storage=new Map();window.localStorage={getItem:k=>storage.get(k)||null,setItem:(k,v)=>storage.set(k,v),removeItem:k=>storage.delete(k)};
window.matchMedia=()=>({matches:false});window.Blob=Blob;window.URL=fakeURL;
document.readyState='loading';
const context=vm.createContext({window,document,Blob,URL:fakeURL,console,Event:window.Event,MutationObserver:window.MutationObserver,setTimeout:()=>0,clearTimeout(){},requestAnimationFrame:fn=>fn(),matchMedia:window.matchMedia});
for(const name of ['AlmFlow','AlmAutosave','MaComparisons','MaStudies','Toast','AlmBuildInfo'])Object.defineProperty(context,name,{get:()=>window[name]});
document.addEventListener('click',e=>{if(e.target.tagName==='A'&&e.target.download)downloads.push({name:e.target.download,blob:blobs.get(e.target.href)});});
const executed=[],omitted=[];
for(const [i,s] of Array.from(document.querySelectorAll('script')).entries()){
    const rel=s.src?path.posix.normalize('component-nma/'+s.src):`component-nma/index.html:inline-${i}`;
    if(rel==='hub/shared/chart-export-auto.js'){omitted.push({file:rel,reason:'requires browser geometry, computed styles and canvas; source reviewed, visual download behavior unverified'});continue;}
    vm.runInContext(s.src?fs.readFileSync(`${root}/${rel}`,'utf8'):s.textContent,context,{filename:rel});executed.push(rel);
}
document.readyState='complete';document.dispatchEvent(new window.Event('DOMContentLoaded'));
const defaultResult=JSON.parse(JSON.stringify(window._almLastCnma()));
let design=null,forestMarkup='';const originalMatMul=context.matMul;
context.matMul=function(A,B){if(design===null)design=B.map(r=>r.slice());return originalMatMul(A,B);};
const forest=document.querySelector('#forest');let proto=forest,desc;
while(proto&&!desc){desc=Object.getOwnPropertyDescriptor(proto,'innerHTML');proto=Object.getPrototypeOf(proto);}
Object.defineProperty(forest,'innerHTML',{get(){return desc.get.call(this);},set(s){forestMarkup=s;return desc.set.call(this,s);}});
function run(c){
    for(const x of document.querySelectorAll('.toast-item'))x.remove();
    let error=null;design=null;
    try{window.__almCnmaLoad(c.text);}catch(e){error=e.message;}
    const result=window._almLastCnma();let parsed=null,parseError=null;
    try{parsed=vm.runInContext('parse(document.getElementById("src").value)',context);}catch(e){parseError=e.message;}
    return {key:c.key,result:result?JSON.parse(JSON.stringify(result)):null,error,parseError,toasts:Array.from(document.querySelectorAll('.toast-item'),x=>x.textContent),componentTable:Array.from(document.querySelectorAll('#comp-body tr'),r=>Array.from(r.querySelectorAll('td'),x=>x.textContent)),combinationTable:Array.from(document.querySelectorAll('#int-body tr'),r=>Array.from(r.querySelectorAll('td'),x=>x.textContent)),svg:document.querySelector('#forest').outerHTML,forestMarkup,viewBox:forest.getAttribute('viewBox'),design,parsed};
}
async function exportsFor(index){
    const out={};
    for(const action of ['json','csv','md','report-md','report-txt']){
        const before=downloads.length;document.querySelector(`[data-action="${action}"]`).click();await Promise.resolve();await Promise.resolve();
        if(downloads.length!==before+1||!downloads.at(-1).blob)throw Error('missing export '+action);
        const file=`downloads-${variant}/${String(index).padStart(4,'0')}-${action}.${action==='json'?'json':action==='csv'?'csv':action==='report-txt'?'txt':'md'}`;
        fs.writeFileSync(file,await downloads.at(-1).blob.text());out[action]=file;
    }
    return out;
}
(async()=>{
    fs.mkdirSync(`downloads-${variant}`,{recursive:true});
    const cases=[...JSON.parse(fs.readFileSync('corpus.json')),...JSON.parse(fs.readFileSync('focused-corpus.json'))],out=[];
    for(const c of cases){let got;try{got=run(c);}catch(e){got={key:c.key,error:e.message,result:null};}try{got.exports=await exportsFor(out.length);}catch(e){got.exportError=e.message;}out.push(got);}
    fs.writeFileSync(`app-${variant}.json`,JSON.stringify(out));
    const bus=[];
    if(fs.existsSync('bus-corpus.json'))for(const c of JSON.parse(fs.readFileSync('bus-corpus.json'))){
        window.__almCnmaLoad('a | control | .3 | .1\na | control | .4 | .1');
        for(const x of document.querySelectorAll('.toast-item'))x.remove();
        if(c.env)storage.set('ma-comparisons-v1',JSON.stringify(c.env));else storage.delete('ma-comparisons-v1');
        let error=null;try{document.querySelector('#btn-bus-load').click();}catch(e){error=e.message;}
        bus.push({key:c.key,error,converted:window.MaComparisons.toContrasts(c.env),result:window._almLastCnma(),text:document.querySelector('#src').value,toasts:Array.from(document.querySelectorAll('.toast-item'),x=>x.textContent),componentTable:document.querySelector('#comp-body').textContent,forestMarkup});
    }
    fs.writeFileSync(`bus-${variant}.json`,JSON.stringify(bus));
    fs.writeFileSync(`runtime-${variant}.json`,JSON.stringify({engine:'Node VM + linkedom',node:process.version,linkedom:require('linkedom/package.json').version,executed,omitted,defaultResult,browserLayoutVerified:false},null,2));
    console.log(`APP ${variant}: ${out.length} configurations; ${downloads.length} real export blobs; ${out.filter(x=>x.error).length} execution errors`);
})().catch(e=>{console.error(e);process.exitCode=1;});
