class Factory:

 def __init__(self,BT,Tyers,ET):
    print(BT,Tyers,ET)
    self.BT =BT
    self.Typers =Tyers
    self.ET =ET

farari = Factory("Covered",4,"8 Cycle")
print(farari.BT)