import math

def Log2(x):
    if x == 0:
        return false
 
    return (math.log10(x) /
            math.log10(2))
 
def isPowerOfTwo(n):
    return (math.ceil(Log2(n)) ==
            math.floor(Log2(n)))
 
if __name__ == "__main__":
    n = int(input('Enter any number: '))
 
    if(isPowerOfTwo(n)):
        print("Yes")
    else:
        print("No")
 
