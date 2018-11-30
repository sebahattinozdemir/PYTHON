
def perfectNumber(number) :

    temp=0
    for i in range(1,number) :
        if(number%i==0):
            temp+=i
    if(number==temp):
        return True
    else:
        False

for i in range(1,1001):
    if(perfectNumber(i)):
        print("Mukemmel Sayi:{}".format(i))