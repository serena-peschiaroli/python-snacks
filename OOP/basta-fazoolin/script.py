import Menu
import Franchise
import Business

brunch = Menu.Menu(name = "Brunch", items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, start_time = 11, end_time = 16
)

early_bird = Menu.Menu(name = "Early Bird", items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
, start_time = 15, end_time = 18)


dinner = Menu.Menu(name = "Dinner", items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, start_time = 17, end_time = 23)


kids = Menu.Menu(name = "Kids", items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, start_time = 11, end_time = 16)

arepas_menu = Menu.Menu(name = "Take a’ Arepa", items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, start_time = 10, end_time = 7.50
)


print(brunch)

print(brunch.calculate_bill(['pancakes', 'home fries', 'coffee']))

print(early_bird.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))


flagship_store = Franchise.Franchise(address = "1232 West End Road", menus = [brunch, early_bird, dinner, kids])
new_installment = Franchise.Franchise(address = "12 East Mulberry Street", menus = [brunch, early_bird, dinner, kids])

arepas_place = Franchise.Franchise(address= "189 Fitzgerald Avenue", menus = [arepas_menu])
print(new_installment.available_menus(17))

business_one = Business.Business(name = "Basta Fazoolin' with My Heart", franchises = [flagship_store, new_installment])

business_two = Business.Business(name = "Take a' Arepa", franchises = [arepas_place])