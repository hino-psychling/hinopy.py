f = open('sakuin.dat','r',encoding = 'utf-8')
rawdata = f.readlines()
f.close()
L = [x.strip().split(',')[:2] for x in rawdata]
dictionary = []
for x in L:
	if x not in dictionary:
		dictionary.append(x)
		
f = open('dict for homoph.dat','w',encoding = 'utf-8')
for x in dictionary:
	item = x[0]+'\t'+x[1]+'\n'
	f.write(item)
f.flush()
f.close()
print('done')
while True:
	pass


