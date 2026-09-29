class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return f" The store is located at {self.address}"

    def available_menus(self, time):
        available = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                available.append(menu)

        return available


