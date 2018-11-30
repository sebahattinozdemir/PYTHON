
def ebob(number1,number2):

    temp = 0
    if(number1>=number2):
        for i in range(1,number2+1):
            if(number2%i == 0 and number1%i==0):
                if(temp<i): temp = i

    else:
        if (number2 > number1):
            for i in range(1, number1+1):
                if (number2 % i == 0 and number1 % i == 0):
                    if (temp < i): temp = i


    return temp


num1 = int(input("Birinci Sayiyi Giriniz:"))
num2 = int(input("Ikinci Sayiyi Giriniz:"))

print("E.B.O.B:{}".format(ebob(num1,num2)))