import sys

import itertools

def total_no(x,k,n):
	for i in itertools.permutations(x):
		p=0
        for key,value in enumerate(i):
            if key-value>=0:
                p=p+1
        if p>=k:
            n=n+1
	return n


n=int(input())
for i in range(n):
	n,k=[int(i) for i in input().split()]
	x=[i for i in range(n)]
	z=total_no(x,k,0)
	print(z)
