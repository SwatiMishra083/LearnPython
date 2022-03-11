#flush parameter
import time
g=open('p16sample.txt','r')
a=g.read()
s=time.time()
print(a,flush=False)
e=time.time()
print(e-s)
