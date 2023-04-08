from abc import ABC, abstractmethod
from datetime import date
from engine.capulet_engine import CapuletEngine
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery
class Serviceable(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass


class Car(Serviceable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return super().needs_service()
    


class CarFactory:
    def __init__(self):
        pass

    def create_calliope(self, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(current_date, last_service_date)
        car = Car(capuletEngine, spindlerBattery)
        return car
    
    def create_glissade(self, car, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        spindlerBattery = SpindlerBattery(current_date, last_service_date)
        car = Car(willoughbyEngine, spindlerBattery)
        return car

    def create_palindrome(self, car, current_date: date, last_service_date: date, warning_light: bool) -> Car:
        sternmanEngine = SternmanEngine(warning_light)
        spindlerBattery = SpindlerBattery(current_date, last_service_date)
        car = Car(sternmanEngine, spindlerBattery)
        return car

    def create_rorschach(self, car, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        willoughbyEngine = WilloughbyEngine(current_mileage, last_service_mileage)
        nubbinBattery = NubbinBattery(current_date, last_service_date)
        car = Car(willoughbyEngine, nubbinBattery)
        return car

    def create_thovex(self, car, current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        capuletEngine = CapuletEngine(current_mileage, last_service_mileage)
        nubbinBattery = NubbinBattery(current_date, last_service_date)
        car = Car(capuletEngine, nubbinBattery)
        return car
    
curDate = date.today()
carFactory = CarFactory()
calCar1 = carFactory.create_calliope(curDate, 100, 200, 400)
print('calCar1', calCar1.engine.current_mileage, calCar1.battery.last_service_date)