import sys

n= int(sys.argv[1])
# preload fib[0] and fib[1] to 1
fib=[1,1]

for x in range (2,n):
	fib.append(fib[x-1] + fib[x-2])

print fib
