#Collatz sequence
def collatz(number) :
    try:
        number=int(number)
    except ValueError :
        print("invlid value, you hava to enter an integer.")
        return
    while(number==1):
        return
    result=number%2
    if result==0:
        print( str(int(number/2)))
        collatz(number/2)
    elif result==1:
        print(str(3*number+1))
        collatz(3*number+1)
    else:
        print("something wrong")
print("Enter number:")
num=input()
collatz(num)

