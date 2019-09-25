

a = [1, 1, 2, 3, 5, 8, 13, 21, 24, 55, 89]
b=[]

for num in a:
    if num < 5:
        print(num)
        b.append(num)
print(b)