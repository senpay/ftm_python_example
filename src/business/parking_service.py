from doctest import UnexpectedException
import math


class ParkingService:

    def calculate_parking_price(self, parking_time):
        if (parking_time <= 60):
            return "1£"
        if (parking_time <= 240):
            hours = math.ceil(parking_time / 60)
            cost = hours * 70
            return f'{cost//100}£{cost%100}p'
        if (parking_time <= 1440):
            return "15£"
        else:
            raise UnexpectedException("Something hasn't gone right")

