# poly --> Multiple
# morphism --> Form

# Method Overriding

class grandfaather:
    def greet(self):
        print("Form Grandfather")
class father(grandfaather):
    def greet(self):
        print("Form father")
class children(father):
    def greet(self):
        print("Form Children")

gf = grandfaather()
fat= father()
ch= children()

gf.greet()
fat.greet()
ch.greet()

# Method Overloading

class shape:
    def area (slef, a,b=10):
        return a*b
p= shape()
print(p.area(12))
print(p.area(12,10))


