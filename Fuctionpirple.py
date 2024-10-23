# funciones son para no tener que repetir codigo

#def FuctionName(Input): # le dice a la computadora que vamos con una funcion
    # Action, se pone un tab
    # return Output
    # More code (seria parte del codigo, pq esta indentado)

def addOne(Number):
    Output = Number + 1
    return Output

Var = 0
print(Var)
Var2 = addOne(Var)
Var3 = addOne(Var2)
Var4 = addOne(2.1+3.4)
print(Var2)
print(Var3)
print(Var4)

def addOneAddTwo(NumberOne, NumberTwo):
    Output = NumberOne + 1
    Output += NumberTwo + 2 # es lo mismo que Output = Output = NumberTwo + 2
    return Output

Sum = addOneAddTwo(Var2,Var3)

print(Sum)

