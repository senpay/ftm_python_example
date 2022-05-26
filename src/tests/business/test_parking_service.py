import unittest
import ddt

from business.parking_service import ParkingService

@ddt.ddt
class TestStringMethods(unittest.TestCase):

    @ddt.data(
            (50, '1£'),
            (59, '1£'),
            (60, '1£'),
            (61, '1£40p'),
            (180, '2£10p'),
            (200, '2£80p'),
            (239, '2£80p'),
            (240, '2£80p'),
            (241, '15£'),
            (300, '15£'),
            (1440, '15£'),
            (2000, 'N/A')
    )
    def test_parking_service(self, case):
        duration, payment = case

        result = self.parking_service.calculate_parking_price(duration)

        self.assertEqual(result, f"{payment}")




    
    def setUp(self):
        self.parking_service = ParkingService()