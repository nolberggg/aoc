#solution part 1
"""
puzzle = open("puzzel1_1adventofcode2024.txt","r")
data= puzzle.read()
L = []
R = []
list = data.split()

L = list[::2]
R = list[1::2]
print(L)
L = sorted(L)
R = sorted(R)
final = []

for i in range(len(L)):
   diff = abs(int(L[i]) - int(R[i]))
   final.append(diff)
   
print(final)
print(sum(final))
"""
#solution part 2
puzzle = open("puzzel1_1adventofcode2024.txt","r")
data= puzzle.read()
L = []
R = []
list = data.split()

L = list[::2]
R = list[1::2]

similar = []
for i in range(len(L)):
    total = R.count(L[i])
    similar.append(total*int(L[i]))

print(sum(similar))
    


    
