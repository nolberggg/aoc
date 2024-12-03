"""
with open("puzzel2.txt", "r") as file:
    array = []
    for line in file:
        array.append([int(x) for x in line.split()])

print(array)
safecounter = 0
for line in array:
    counter = 0
    print(line)
    if sorted(line) == line or sorted(line,reverse=True) == line:
        print("Ascends or Descends...")
        for n in line:
            if counter == len(line)-1:
                print("Safe!")
                safecounter += 1
                break
            start = line.index(n)
            next = line.index(n) + 1
            if abs((line[start] - line[next])) < 4 and abs((line[start] - line[next])) > 0:
                print("Safe", abs((line[start] - line[next])))
                #print("Safe")
            else:
                print("Too high level change...", abs((line[start] - line[next])) )
                break
            counter += 1
    else:
        print("Failed to ascend or descend...")
print(safecounter)
"""

with open("puzzel2.txt", "r") as file:
    array = []
    for line in file:
        array.append([int(x) for x in line.split()])

print(array)
safecounter = 0
for line in array:
    counter = 0
    print(line)
    if sorted(line) == line or sorted(line,reverse=True) == line:
        print("Ascends or Descends...")
        for n in line:
            if counter == len(line)-1:
                print("Safe!")
                safecounter += 1
                break
            start = line.index(n)
            next = line.index(n) + 1
            if abs((line[start] - line[next])) < 4 and abs((line[start] - line[next])) > 0:
                print("Safe", abs((line[start] - line[next])))
                #print("Safe")
            else:
                print("Too high level change...", abs((line[start] - line[next])) )
                break
            counter += 1
    else:
        print("Failed to ascend or descend...")
        for n in line:
            rank = line[n]
            print(rank)
            line2 = line.remove(rank)
            print(line2)
            if sorted(line2) == line2 or sorted(line2,reverse=True) == line2:
                print("Continue")
            else:
                print("nope!")
        
print(safecounter)