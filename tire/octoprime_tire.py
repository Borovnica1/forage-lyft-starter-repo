from tire.tire import Tire


class OctoprimeTire(Tire):
    def __init__(self, sensorArr):
        self.sensorArr = sensorArr
    
    def needs_service(self) -> bool:
        tireWorn = 0
        for sensor in self.sensorArr:
            tireWorn += sensor
        return True if tireWorn >= 3 else False