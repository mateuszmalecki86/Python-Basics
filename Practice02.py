
length = int(input("Enter sequence length: "))
a=0
b=1
x=[1]

if length == 0:
    print("Chosen value is 0")


for z in range(length):
    print(x)
    c = b+a
    a = b
    b = c
    x.append(c)


