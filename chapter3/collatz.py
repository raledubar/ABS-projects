# The collatz sequence 

def collatz(number):
    while (number != 1):
        if (number % 2==0):
            number //= 2
            print(number)
        elif(number % 2 == 1):
            number = (3 * number) +1 
            print(number)

    print(number)
    return number 

if __name__ == "__main__":
    print("please give me a number")
    number = int(input())
    collatz(number)