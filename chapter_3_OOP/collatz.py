# The collatz sequence 

class Collatz():
    def __init__(self, n:int) -> int:
        self.n = n
    
    def collatz(self):
        while (self.n != 1):
            if (self.n % 2 == 0):
                self.n //= 2
                print(self.n)
            elif(self.n % 2 == 1):
                self.n = ( 3 * self.n) + 1
                print(self.n)
 #       print(self.n)
        return self.n
if __name__ == "__main__":

    print("please give me a number")
    number = int(input())
    mycollatz = Collatz(number)
    mycollatz.collatz()
            
