import unittest

from engine.WilloughbyEngine import WilloughbyEngine

from engine.SternmanEngine import SternmanEngine

from engine.CapuletEngine import CapuletEngine


class TestCapuletEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 30001
        engine = CapuletEngine(last_service_mileage, current_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 29999
        engine = CapuletEngine(last_service_mileage, current_mileage)

        self.assertFalse(engine.needs_service())

class TestSternmanEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_is_on = True
        engine = SternmanEngine(warning_light_is_on)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_is_on = False
        engine = SternmanEngine(warning_light_is_on)

        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 60001
        engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        last_service_mileage = 0
        current_mileage = 59999
        engine = WilloughbyEngine(last_service_mileage, current_mileage)

        self.assertFalse(engine.needs_service())

if __name__ == '__main__':
    unittest.main()