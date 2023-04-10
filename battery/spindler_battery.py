from battery.battery import Battery
from battery.battery import add_years


class SpindlerBattery(Battery):
    def __init__(self, current_date, last_service_date):
        self.current_date = current_date
        self.last_service_date = last_service_date

    def needs_service(self) -> bool:
        date_when_service_will_be_needed = add_years(self.last_service_date, 3)
        return self.current_date > date_when_service_will_be_needed
