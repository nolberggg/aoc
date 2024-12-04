#day 4 oh lord
import re
puzzle = open("puzzle 4.txt", "r")
data = puzzle.read()
# real length is 140
# test length is 10
print(data)
print(len(data))

#TYPE 1 and 2 
type1 = re.findall("XMAS",data)
type2 = re.findall("SAMX",data)
total1 = type1 + type2
print(len(total1))

#TYPE 3 and 4
bits = data.split("\n")
lines = ["" for i in range(0, len(bits[0]))]
for bit in bits:
    for i in range(0, len(bit)):
        if bit[i] != " ":
            lines[i] += bit[i]
    "\n".join(lines)
data2 = " ".join(lines)
type3 = re.findall("XMAS",data2)
type4 = re.findall("SAMX",data2)
total2 = type3 + type4
print(len(total2))

# type 5 and 6
newish=[]
new=[]
f = open("puzzle 4.txt", "r")
g = data.splitlines(True)
for i in g:
    s = i.strip("\n")
    new.append(s)

print(new)


result = [" " * (list(enumerate(new)).index((i, x)) + 1) + x for i, x in enumerate(new)]
    
newest = "\n".join(result)

print(newest)


bitss = newest.split("\n")
max_length = max(len(line) for line in bitss)
liness = ["" for _ in range(max_length)]

for bitt in bitss:
    for i in range(max_length):
        if i < len(bitt) and bitt[i] != " ":
            liness[i] += bitt[i]

data3 = " ".join(liness)
type5 = re.findall("XMAS", data3)
type6 = re.findall("SAMX", data3)
total3 = type5 + type6
print(len(total3))

#msxmaxsamx

# type 7 and 8
newreverse=[]
for i in new:
    newreverse.append(i[::-1])


result2 = [" " * (list(enumerate(newreverse)).index((i, x)) + 1) + x for i, x in enumerate(newreverse)]
    
newestrev = "\n".join(result2)

print(newestrev)


bitsss = newestrev.split("\n")
max_len = max(len(lineee) for lineee in bitsss)
linesss = ["" for _ in range(max_len)]

for bittt in bitsss:
    for i in range(max_len):
        if i < len(bittt) and bittt[i] != " ":
            linesss[i] += bittt[i]

data4 = " ".join(linesss)
print(data4)
type7 = re.findall("XMAS", data4)
type8 = re.findall("SAMX", data4)
total4 = type7 + type8
print(len(total4))


print(len(total1) + len(total2)+len(total3)+len(total4))