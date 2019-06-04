L = list(range(2,10))
for x in L:
    name = 'length'+str(x)+'.dat'
    NoU = 'jonbs_dict'+str(x)+'.dat'
    f = open(name,'r',encoding = 'utf-8')
    rawdata = f.readlines()
    f.close()
    
    L1 = [x.strip().split(',') for x in rawdata]
    L2 = []
    for x in L1:
        if not x in L2:
            L2.append(x)

    f = open(NoU,'w',encoding = 'utf-8')
    for x in L2:
        s = '\t'.join(x) + '\n'
        f.write(s)
    f.flush()
    f.close()

print('done')

while True:
    pass