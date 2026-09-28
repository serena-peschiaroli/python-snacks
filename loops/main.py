#The provided code stub reads an integer, n, from STDIN. For all non-negative integers i>n, print i**2


n = int(input("Insert a number: "))
if (n < 1) or (n > 20):
    print("Invalid number, please insert a number between 1 and 20")
else:
    for i in range(n+1):
        print(i**2)

