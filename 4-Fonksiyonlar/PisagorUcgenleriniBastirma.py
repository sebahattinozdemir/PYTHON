
def pisagor_yazdir():

    for i in range(1,101):
        for j in range(1,101):

            hipotenus = i**2 + j**2
            hipotenus = hipotenus**0.5
            if(hipotenus == int(hipotenus)):
                print((i,j,int(hipotenus)))


pisagor_yazdir()