class Factory:

 def __init__(self,BT,Tyers,ET):
    print(BT,Tyers,ET)
    self.BT = BT # object attribute
    self.Typers = Tyers
    self.ET = ET
    
 def show(self):
   print(f"Your Details are\n{self.BT},{self.ET}{self.Typers}")


farari = Factory("Covered",4,"8 Cycle")
alto = Factory("Covered",4,"4 Cycle")
print(farari.BT)

alto.show()