class Maths:
    def GetInput(self):
        self.n1 = int(input("Enter First Number"))
        self.n2 = int(input("Enter Second Number"))

class Division(Maths):
    def Div(self):
        try:
            self.div=self.n1/self.n2
        except Exception:
            print("Divide by zero",Exception)
            exit()

class Result(Division):
    def output(self):
        print("Division of %s" % self.n1, "and %s is" % self.n2, self.div)
obj=Result()
obj.GetInput()
obj.Div()
obj.output()