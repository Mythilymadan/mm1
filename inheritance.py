class Vechicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage


class Bus(Vechicle):
    pass


sb=Bus("School_volvo",180,12)
print("Vehicle Name=",sb.name,   "Maximum speed=",sb.max_speed,    "Mileage=",sb.mileage)