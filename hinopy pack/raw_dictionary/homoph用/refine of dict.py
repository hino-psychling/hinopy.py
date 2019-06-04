f = open('dict for homoph.dat','r',encoding = 'utf-8')
rawdata = f.readlines()
f.close()
L = [x.strip().split() for x in rawdata]
Index = []
for x in L:
	if x[0] not in Index:
		Index.append(x[0])
Index = [[x] for x in Index]
for x in Index:
	for y in L:
		if x[0] == y[0]:
			x.append(y[1])
f = open('homoph_justdict.dat','w',encoding = 'utf-8')
for x in Index:
	item = '\t'.join(x)+'\n'
	f.write(item)
f.flush()
f.close()
print('done')
while True:
	pass