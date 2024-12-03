import re
import ast
puzzle = open("puzzle3.txt", "r")
data = puzzle.read()
#data = re.sub('[^mul0-9(),]',"",puzzle.read())
print(data)
sub = "mul"
total = []
for match in re.finditer(sub,data):
    found = match.span()
    start = found[1]
    end = found[1]
    if data[end] == "(":
        #print(data[found2])
        found3 = data.find(")",found[1])+1
        #print("start...",start)
        #print("end...",found3)
        #print(data[start:found3])
        try:
            test = ast.literal_eval(data[start:found3])
            try:
                total.append(test[0]*test[1])
                print(test,test[0]*test[1])
            except:
                print("out of range!")
        except SyntaxError:
            print("skipping...")
print(sum(total))