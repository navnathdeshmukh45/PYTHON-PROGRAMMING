class Factory:

  def __init__(self,BT,Tyers,ET):
        print(BT,Tyers,ET)
        self.BT = BT # object attribute
        self.Typers = Tyers
        self.ET = ET
    
# def show(self):
#       print(f"Your Details are\n{self.BT},   {self.ET}{self.Typers}")


class Honda(Factory):
  def __init__(self, BT, Tyers, ET,glass):
     super().__init__(BT, Tyers, ET)
     self.glass = glass

obj = Honda("Covered",4,"8 Cycle",5)
print(obj.glass)