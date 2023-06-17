data = [[1,2,3],[4,5],[6,7,8,9]]
print(data[1])
print(data[2][3])

for sub in data:
    for item in data:
        print(item, end="    ")
    print()