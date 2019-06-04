# -*- coding: utf-8 -*-

f = open('sakuin.dat','r',encoding = 'utf-8')
rawdata = f.readlines()
f.close()
L = [[x.split(',')[0],x.split(',')[1]] for x in rawdata]

L1 = []
L2 = []
L3 = []
L4 = []
L5 = []
L6 = []
L7 = []
L8 = []
L9 = []

for x in L:
	if len(x[1]) == 1:
		L1.append(x)
	elif len(x[1]) == 2:
		L2.append(x)
	elif len(x[1]) == 3:
		L3.append(x)
	elif len(x[1]) == 4:
		L4.append(x)
	elif len(x[1]) == 5:
		L5.append(x)
	elif len(x[1]) == 6:
		L6.append(x)
	elif len(x[1]) == 7:
		L7.append(x)
	elif len(x[1]) == 8:
		L8.append(x)
	else:
		L9.append(x)

f = open('length2.dat','w',encoding = 'utf-8')
for x in L2:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()
		
f = open('length3.dat','w',encoding = 'utf-8')
for x in L3:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()

f = open('length4.dat','w',encoding = 'utf-8')
for x in L4:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()

f = open('length5.dat','w',encoding = 'utf-8')
for x in L5:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()

f = open('length6.dat','w',encoding = 'utf-8')
for x in L6:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()

f = open('length7.dat','w',encoding = 'utf-8')
for x in L7:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()

f = open('length8.dat','w',encoding = 'utf-8')
for x in L8:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()

f = open('length9.dat','w',encoding = 'utf-8')
for x in L9:
	s = ','.join(x) + '\n'
	f.write(s)
f.flush()
f.close()

print('done')

while True:
	pass