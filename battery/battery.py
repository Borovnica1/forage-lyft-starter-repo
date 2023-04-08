from abc import ABC, abstractmethod
from calendar import isleap
    
def add_years(d, years):
    new_year = d.year + years
    try:
        return d.replace(year=new_year)
    except ValueError:
        if (d.month == 2 and d.day == 29 and # leap day
            isleap(d.year) and not isleap(new_year)):
            return d.replace(year=new_year, day=28)
        raise
    
class Battery(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def needs_service(self) -> bool:
        pass