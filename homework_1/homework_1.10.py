input = [1, 5, 2, 9, 2, 9, 1]

map = dict.fromkeys(input, 0)
for i in input:
    map[i] = map[i]+1

for i in map:
    if(map[i] == 1):
        print(i)
