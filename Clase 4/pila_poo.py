class Pila:
    pila = None
    def __init__(self):
        self.pila = []

    def push(self, val):
        self.pila.append(val)

    def pop(self):
        val = self.pila[-1]
        del self.pila[-1]
        return val


pila = Pila()

pila.push(3)
pila.push(2)
pila.push(1)

print(pila.pop())
print(pila.pop())
print(pila.pop())

#print(len(pila.pila))
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


