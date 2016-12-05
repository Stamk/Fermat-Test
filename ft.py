import math
from random import randint
def FermatTest(a,n):
    b=n-1
    if (pow(a,b,n))==1:
        return 1
    else:
        return 0

print('Enter an integer:')
#n = int(float(input()))
n=2*1000-1
flag=1
#n=int(n)
for i in range(40):
 a = randint(2,n-1)
 if (FermatTest(a,n)==1):
  flag=1
 else:
  flag=0
  break
if (flag==1): print('Yes')
else: print('No')
