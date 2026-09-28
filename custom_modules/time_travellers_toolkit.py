from decimal import Decimal
from datetime import datetime
from random import randint
from random import choice
import custom_module


current_time = datetime.now()
print(current_time)

base_cost = Decimal(100)

destinations = ['Venice', 'Paris', 'London', 'Rome', 'Giza', 'Machu Picchu']
target_year = randint(1200, 2027)
selected_destination = choice(destinations)

def get_travel_cost(
        target_year:int,
        base_cost:Decimal = Decimal('100.00'),
        rate_per_year:Decimal = Decimal('50.00')
):
    current_year = datetime.now().year
    years_travelled = abs(target_year - current_year)

    multiplier = Decimal(years_travelled)
    total_cost = base_cost + (multiplier * rate_per_year)

    return total_cost



cost = get_travel_cost(target_year)
print(cost)

message = custom_module.generate_time_travel_message(target_year, selected_destination, cost)
print(message)



