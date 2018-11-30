

a = 1
b = 1
fibonacci = [a, b]

for i in range(1, 20):
    print("a:{} b:{}".format(a,b))
    a, b = b, a+b
    fibonacci.append(b)
print("fibonacci:", fibonacci)


