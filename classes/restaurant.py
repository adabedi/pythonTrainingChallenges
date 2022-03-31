class Menu:
    def __init__(self, name, items, start_time, end_time) -> None:
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return "{name} menu available from {start_time} to {end_time}".format(
            name=self.name, start_time=self.start_time, end_time=self.end_time)

    def calculate_bill(self, purchased_items):
        price = 0
        for item in purchased_items:
            price += brunch.get(item, 0)
        return price


class Franchise:
    def __init__(self, address, menus) -> None:
        self.address = address
        self.menus = menus

    def __repr__(self) -> str:
        return self.address

    def available_menus(self, time):
        menu = [menu_item.name for menu_item in self.menus
                if menu_item.start_time <= time and menu_item.end_time >= time]
        return menu


class Businesses:
    def __init__(self, name, franchises) -> None:
        self.name = name
        self.franchises = franchises

    def __repr__(self) -> str:
        pass


brunch = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
branch_menu = Menu('brunch', brunch, 1100, 1600)

print(branch_menu)
print('\n')
print(branch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))

early_bird = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00
}
early_bird_menu = Menu('early_bird', early_bird, 700, 1100)


dinner = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}

dinner_menu = Menu('dinner', dinner, 1600, 2100)

kids = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}

kids_menu = Menu('kids', kids, 700, 2100)

menus = [
    branch_menu, kids_menu, dinner_menu, early_bird_menu]

flagship_store = Franchise("1232 West End Road", menus)

new_installment = Franchise("12 East Mulberry Street", menus)
print(flagship_store.available_menus(1100))

franchises = [flagship_store, new_installment]

my_business = Businesses("Basta Fazoolin' with my Heart", franchises)
