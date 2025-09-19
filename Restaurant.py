from abc import ABC, abstractmethod

class Restaurant(ABC):
    def __init__(self, items, prices):
        self.items = items
        self.prices = prices
        self.order_count = [0] * len(items)

    @abstractmethod
    def display_items(self):
        pass

    @abstractmethod
    def order_item(self, choice):
        pass

    def generate_bill(self):
        total = 0
        for i, count in enumerate(self.order_count):
            if count > 0:
                print(f"{self.items[i]:20} {count:^8} Rs.{self.prices[i]:<8} Rs.{count * self.prices[i]}")
                total += count * self.prices[i]
        return total


class Breakfast(Restaurant):
    def __init__(self):
        items = ["Idli (2 pcs)", "Vada (2 pcs)", "Masala Dosa", "Utthapa", "Appam"]
        prices = [40, 50, 90, 80, 70]
        super().__init__(items, prices)

    def display_items(self):
        print("-----------Breakfast-----------")
        for i, (item, price) in enumerate(zip(self.items, self.prices), start=1):
            print(f"{i}. {item:20} Rs. {price}")
        print(f"{len(self.items) + 1}. Exit")

    def order_item(self, choice):
        if 1 <= choice <= len(self.items):
            self.order_count[choice - 1] += 1
            print(f"Your {self.items[choice - 1]} is ready.")
            return self.prices[choice - 1]
        return 0


class Lunch(Restaurant):
    def __init__(self):
        items = ["Roti", "Rice", "Dal", "Butter Paneer"]
        prices = [20, 80, 80, 140]
        super().__init__(items, prices)

    def display_items(self):
        print("-------------Lunch-------------")
        for i, (item, price) in enumerate(zip(self.items, self.prices), start=1):
            print(f"{i}. {item:20} Rs. {price}")
        print(f"{len(self.items) + 1}. Exit")

    def order_item(self, choice):
        if 1 <= choice <= len(self.items):
            self.order_count[choice - 1] += 1
            print(f"Your {self.items[choice - 1]} is ready.")
            return self.prices[choice - 1]
        return 0


class Snacks(Restaurant):
    def __init__(self):
        items = ["Vada Pav", "Sandwich", "Samosa", "Dabeli"]
        prices = [20, 80, 20, 30]
        super().__init__(items, prices)

    def display_items(self):
        print("--------------Snacks---------------")
        for i, (item, price) in enumerate(zip(self.items, self.prices), start=1):
            print(f"{i}. {item:20} Rs. {price}")
        print(f"{len(self.items) + 1}. Exit")

    def order_item(self, choice):
        if 1 <= choice <= len(self.items):
            self.order_count[choice - 1] += 1
            print(f"Your {self.items[choice - 1]} is ready.")
            return self.prices[choice - 1]
        return 0


class Dinner(Restaurant):
    def __init__(self):
        items = ["Roti", "Rice", "Dal", "Kaju Masala", "Tomato Soup"]
        prices = [20, 80, 80, 140, 120]
        super().__init__(items, prices)

    def display_items(self):
        print("------------Dinner-------------")
        for i, (item, price) in enumerate(zip(self.items, self.prices), start=1):
            print(f"{i}. {item:20} Rs. {price}")
        print(f"{len(self.items) + 1}. Exit")

    def order_item(self, choice):
        if 1 <= choice <= len(self.items):
            self.order_count[choice - 1] += 1
            print(f"Your {self.items[choice - 1]} is ready.")
            return self.prices[choice - 1]
        return 0


class HotelPython:
    def __init__(self):
        self.total_bill = 0
        self.categories = {
            1: Breakfast(),
            2: Lunch(),
            3: Snacks(),
            4: Dinner()
        }

    def display_main_menu(self):
        print("-----------Menu--------------")
        print("1. Breakfast")
        print("2. Lunch")
        print("3. Snacks")
        print("4. Dinner")
        print("5. Exit")

    def run(self):
        print("Welcome to Hotel Python")
        while True:
            if self.total_bill > 0:
                print("-----------Menu--------------                           -----------Bill-----------")
                print(f"                                                                   Rs. {self.total_bill}")
                print("1. Breakfast")
                print("2. Lunch")
                print("3. Snacks")
                print("4. Dinner")
                print("5. Exit")
            else:
                self.display_main_menu()

            try:
                cat_choice = int(input("Enter what would you like to have: "))
            except ValueError:
                continue

            if cat_choice in self.categories:
                category = self.categories[cat_choice]
                category.display_items()
                try:
                    item_choice = int(input("Enter your dish number: "))
                    added_price = category.order_item(item_choice)
                    self.total_bill += added_price
                except ValueError:
                    continue
            elif cat_choice == 5:
                if self.total_bill > 0:
                    print("-----------Final Bill-----------")
                    print("Item                 Qty     Price     Total")
                    for cat in self.categories.values():
                        cat.generate_bill()
                    print(f"{'':35}Total: Rs. {self.total_bill}")
                print("Thank You, Visit us Again!!!!!")
                break


if __name__ == "__main__":
    hotel = HotelPython()
    hotel.run()
