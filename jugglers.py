juggs = open("jugglefest.txt")
for i, line in enumerate(juggs):
    if line == '\n':
        numcirc=i
juggs.close()
numjuggs = i - numcirc
juggspercirc = numjuggs/numcirc
class Circuit:
    def __init__(self, num, stats, jugglers):
        self.num = num
        self.stats = stats
        self.jugglers = jugglers
##    def isFull(self):
##        return len(self.jugglers) == juggspercirc
class Juggler:
    def __init__(self, num, stats, prefs):
        self.num = num
        self.stats = stats
        self.prefs = prefs
        self.circuit = -1
def getScore(circ,jugg):
    return sum([a*b for a,b in zip(circuits[circ].stats,jugglers[jugg].stats)])
def assignCircuits(juggs):
    freejugglers = juggs
    while freejugglers!=[]:
        jugg = freejugglers.pop(0)
        for i, circ in enumerate(jugglers[jugg].prefs):
            if len(circuits[circ].jugglers) < juggspercirc:
                if type(jugg) is int:
                    circuits[circ].jugglers.append(jugg)
                    jugglers[jugg].circuit=circ
                    break
            else:
                a = circuits[circ].jugglers
                for j, k in enumerate(circuits[circ].jugglers):
                    if getScore(circ,k) < getScore(circ,jugg):
                        a[j]=jugg
                        circuits[circ].jugglers = a
                        jugglers[jugg].circuit = circ
                        freejugglers.append(k)
                        break
                        break
circuits = []
jugglers = []
juggs = open("jugglefest.txt")
for line in juggs:
    if line[0] == 'C':
        a = line.split(' ')
        num = int(a[1][1:])
        stats = [int(a[2][2:]),int(a[3][2:]),int(a[4][2:])]
        b = Circuit(num,stats,[])
        circuits.append(b)
    elif line[0] == 'J':
        a = line.split(' ')
        num = int(a[1][1:])
        stats = [int(a[2][2:]),int(a[3][2:]),int(a[4][2:])]
        c = a[5].split(',')
        prefs = []
        for i in c:
            prefs.append(int(i[1:]))
        q = Juggler(num,stats,prefs)
        jugglers.append(q)
juggs.close()
juggnums = list(xrange(len(jugglers)))
assignCircuits(juggnums)
output = open('jugglefestoutput.txt','w')
for circuit in circuits:
    output.write('C'+str(circuit.num)+' ')
    for ind,i in enumerate(circuit.jugglers):
        jugg = jugglers[i]
        output.write('J'+str(i))
        prefs = jugg.prefs
        for j in prefs:
            score = getScore(j,i)
            output.write(' C' + str(j) + ':' + str(score))
        if ind+1 < len(circuit.jugglers):
            output.write(', ')
        else:
            output.write('\n')
output.close()
