from tire.tire import Tire


class CarriganTire(Tire):
    def __init__(self, sensorArr):
        self.sensorArr = sensorArr
    
    def needs_service(self) -> bool:
        for sensor in self.sensorArr:
            if sensor >= 0.9:
                return True
        return False