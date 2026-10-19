import json,hashlib,re,html
from pathlib import Path
cases=[]
def add(name,text,refusal=None):
    c=dict(key='focused::'+name,text=text,rows=[],input_sha256=hashlib.sha256(text.encode()).hexdigest(),package='focused',dataset=name)
    if refusal:c['expected_refusal']=refusal
    else:
        for i,line in enumerate(text.splitlines()):
            a,b,te,se=[v.strip() for v in line.split('|')];c['rows'].append(dict(A=a,B=b,te=float(te),se=float(se),study=str(i+1)))
    cases.append(c)
add('built-in',html.unescape(re.search(r'<textarea[^>]*id="src"[^>]*>(.*?)</textarea>',Path('app-original/component-nma/index.html').read_text(encoding='utf-8'),re.S).group(1)))
add('tiny','a | control | -.4 | .12\nb | control | -.3 | .15\na+b | control | -.65 | .13\na+c | control | -.55 | .16\nc | control | -.2 | .18\nb+c | control | -.45 | .14\na+b+c | control | -.8 | .2')
add('heterogeneous','a | control | -2 | .1\nb | control | 1 | .2\na+b | control | 3 | .3\na | b | 2 | .15\nb | control | -.5 | .25')
add('saturated','a | control | -.3 | .1\nb | control | .2 | .2')
add('disconnected-identifiable','a+b | control | .3 | .1\na | b | -.2 | .2\na+b | control | .7 | .1\na | b | -.5 | .3')
add('no-literal-control-identifiable','a+b | a | .3 | .1\na+b | b | .4 | .2\na+b | a | .8 | .1')
add('case-whitespace',' A + B | CONTROL | .4 | .1\na | control | .3 | .15\nb | control | .2 | .2')
add('html-label','<tag>&x | control | .3 | .1\nconstructor | control | .2 | .15\n__proto__ | control | .1 | .2')
add('singular','a | b | .3 | .1\na | b | .4 | .2','Components are not identifiable from the contrasts.')
add('empty','','At least 2 valid contrasts are required.')
add('singleton','a | control | .3 | .1','At least 2 valid contrasts are required.')
for name,text in [('numeric-junk','a | control | .3oops | .1\na | control | .4 | .1'),('empty-number','a | control | | .1\na | control | .4 | .1'),('nonpositive-se','a | control | .3 | 0\na | control | .4 | .1'),('empty-component','a+ | control | .3 | .1\na | control | .4 | .1'),('duplicate-component','a+a | control | .3 | .1\na | control | .4 | .1'),('short-row','bad line\na | control | .4 | .1'),('same-treatment','a | a | .3 | .1\na | control | .4 | .1')]:
    add(name,text,'Invalid contrast input.')
add('no-row-cap','\n'.join('a | control | .2 | .1' for _ in range(2001)))
Path('focused-corpus.json').write_text(json.dumps(cases,indent=2)+'\n',encoding='utf-8')
print(len(cases),'focused cases')
