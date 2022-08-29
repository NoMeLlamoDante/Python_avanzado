class Pila:
    def __init__(self):
        #El encapsulamiento en python se hace con doble guión bajo __
        self.__pila = []

    def push(self, val):
        self.__pila.append(val)

    def pop(self):
        val = self.__pila[-1]
        del self.__pila[-1]
        return val


pila = Pila()

pila.push(3)
pila.push(2)
pila.push(1)

print(pila.pop())
print(pila.pop())
print(pila.pop())

print(len(pila.__pila))
#pila = []
#def push(val):
#    pila.append(val)
#
#def pop():
#    val = pila[-1]
#    del pila[-1]
#    return val
#
#
#push(3)
#push(2)
#push(1)
#
#print(pop())
#print(pop())
#print(pop())


