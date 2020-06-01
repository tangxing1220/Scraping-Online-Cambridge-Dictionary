extendURLs = []
fd = open('extendURLs.txt','r')
contents = fd.readlines()
fd.close()

for name in contents:
	name = name.strip('\n')
	extendURLs.append(name)

while 'https://dictionary.cambridge.org/browse/' in extendURLs:
    extendURLs.remove('https://dictionary.cambridge.org/browse/')

m = 0
for i in 'abcdefghijklmnopqrstuvwxyz':
	n = 0
	fd = open('extendURL_'+ i +'.txt', 'w')
	for name in extendURLs:
		if 'https://dictionary.cambridge.org/dictionary/english-chinese-traditional/' + i in name:
			fd.write(name)
			fd.write('\n')
			n= n + 1
	fd.close()
	m = m + n
	print(f"{i} {n}")
print (f"total: {m}")

fd = open('extendURLs.txt', 'w')
for name in extendURLs:
    fd.write(name)
    fd.write('\n')
fd.close()
print(len(extendURLs))
