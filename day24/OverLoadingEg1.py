class Greet:

    def Hello(self, name=None):
        if name:
            print("Hello", name)
        else:
            print("Hello")


g = Greet()
g.Hello()
g.Hello("Boo boo")