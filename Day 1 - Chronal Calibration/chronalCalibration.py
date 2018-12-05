from itertools import cycle

frequenciesSet = []
freq = 0
freqSeen = set()

with open('input.txt') as frequencies: 
    for frequency in frequencies: 
        frequenciesSet.append(int(frequency))
print (sum(frequenciesSet))

for num in cycle(frequenciesSet):
    freq = freq + num
    if freq in freqSeen:
        print(freq)
        break
    else:
        freqSeen.add(freq)