triangle = open('triangle.txt')
lines = triangle.readlines()
triangle.close()

triarray = []

for line in lines:
        a = line.split(' ')
        if a[-1]=='\n':
                a.pop()
        b = [int(x) for x in a]
        triarray.insert(0,b)

while (len(triarray)>1):
        for ind,val in enumerate(triarray[1]):
                a = triarray[0][ind]
                b = triarray[0][ind+1]
                if a > b:
                        triarray[1][ind] = a + triarray[1][ind]
                else:
                        triarray[1][ind] = b + triarray[1][ind]
        triarray.pop(0)

print triarray[0][0]
