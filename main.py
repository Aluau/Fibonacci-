A=1
B=1
C=0
while A==A:
	i=input('NO.fibonacci ')
	u=0
	X=1
	while u<int(i):
	  A=B+C
	  print(X,'.',A)
	  u+=1
	  X+=1
	  B=A+C
	  print(X,'.',B)
	  u+=1
	  X+=1
	  C=A+B
	  print(X,'.',C)
	  u+=1
	  X+=1