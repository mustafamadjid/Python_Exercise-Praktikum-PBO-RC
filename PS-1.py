N = int(input("N = "))

a = 0

for i in range(1,N+1):
    for j in range(1,(N-i)+1):
        print(end = " ")
    
    while a != (2*i-1):
        print("*", end = "")
        a += 1
    a = 0
    print()