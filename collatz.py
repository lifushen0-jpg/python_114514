def collatz(number):
    if number%2==0:
        if number/2==1:
            print(int(number/2))
            return number/2
        print(int(number/2))
        return collatz(number/2)
    if number%2==1:
        if number==1:
            print(number)
            return number
        print(int(3*number+1))
        return collatz(number*3+1)
print(collatz(114514))