class CBN:
    def ir(self):
        return 5

class Zenith(CBN):
    def ir(self):
        return 10

class UBA(CBN):
    def ir(self):
        return 12.0

c = CBN()
z = Zenith()
u = UBA()

print(c.ir())
print(z.ir())
print(u.ir())