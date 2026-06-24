import re,sys
val=sys.argv[1]
f=open(sys.argv[2])
c=f.read()
f.close()
c2=re.sub(r'title: "[^"]*"',f'title: "{val}"'.format(val=val),c)
open(sys.argv[2],"w").write(c2)
print("title_ok")
