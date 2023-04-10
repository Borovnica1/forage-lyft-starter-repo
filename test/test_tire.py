import unittest
from datetime import datetime

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire


class TestCarriganTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tireWearSensorArr = [0.25, 0.92, 0.15, 0.70]
        tire = CarriganTire(tireWearSensorArr)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tireWearSensorArr = [0.25, 0.72, 0.15, 0.70]
        tire = CarriganTire(tireWearSensorArr)
        self.assertFalse(tire.needs_service())

class TestOctoprimeTire(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        tireWearSensorArr = [0.95, 0.95, 0.35, 0.80]
        tire = OctoprimeTire(tireWearSensorArr)
        self.assertTrue(tire.needs_service())

    def test_tire_should_not_be_serviced(self):
        tireWearSensorArr = [0.25, 0.72, 0.15, 0.70]
        tire = OctoprimeTire(tireWearSensorArr)
        self.assertFalse(tire.needs_service())
    