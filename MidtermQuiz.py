class DistanceConversion():
    def __init__(self,distance):
        self._distance = float(input("Enter the distance in meter: "))
    def mtocm(self):
        return self._distance * 100
    def mtokm(self):
        return self._distance / 1000
    def mtoin(self):
        return self._distance * 39.97

    def Display(self):
        print("\nmeter to centimeter:",self.mtocm(),"\nmeter to kilometer: ", self.mtokm(), "\nmeter to inches:", self.mtoin())
conversion =  DistanceConversion(input)
conversion.Display()
