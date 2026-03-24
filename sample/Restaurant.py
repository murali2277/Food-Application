class MenuItem:
    next_id = 1

    def __init__(self, name, price):
        self.item_id = MenuItem.next_id
        MenuItem.next_id += 1
        self.name = name
        self.price = price


class Restaurant:
    next_id = 1

    def __init__(self, restaurant_name, pincode):
        self.restaurant_id = Restaurant.next_id
        Restaurant.next_id += 1

        self.restaurant_name = restaurant_name
        self.pincode = pincode
        self.menu = {}
        self.customer_ratings = []

    def add_menu_item(self, name, price):
        new_item = MenuItem(name, price)
        self.menu[new_item.item_id] = new_item
        print(f"Menu item '{name}' added with ID {new_item.item_id}.")

    def update_menu_item(self, item_id, name, price):
        if item_id not in self.menu:
            print("Menu item not found.")
            return

        item = self.menu[item_id]
        item.name = name
        item.price = price
        print("Menu item updated.")

    def delete_menu_item(self, item_id):
        if item_id not in self.menu:
            print("Menu item not found.")
            return

        removed = self.menu.pop(item_id)
        print(f"Menu item '{removed.name}' deleted.")

    def display_menu(self):
        if len(self.menu) == 0:
            print("No menu items available.")
            return

        print(f"\n{self.restaurant_name} Menu")
        print(f"{'ID':<5} {'Item':<20} {'Price':<10}")
        for item in self.menu.values():
            print(f"{item.item_id:<5} {item.name:<20} {item.price:<10.2f}")

    def get_menu_item(self, item_id):
        return self.menu.get(item_id)

    def add_customer_rating(self, rating):
        self.customer_ratings.append(rating)

    def average_rating(self):
        if len(self.customer_ratings) == 0:
            return 0
        return sum(self.customer_ratings) / len(self.customer_ratings)


class Order:
    next_id = 1

    def __init__(
        self,
        customer_name,
        customer_pincode,
        restaurant_name,
        items,
        total_amount,
    ):
        self.order_id = Order.next_id
        Order.next_id += 1

        self.customer_name = customer_name
        self.customer_pincode = customer_pincode
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_amount = total_amount

        self.status = "Placed"
        self.delivery_boy_name = None

        self.customer_rating = None
        self.customer_feedback = ""
        self.delivery_boy_rating = None
        self.delivery_boy_feedback = ""

    def display_summary(self):
        summary = (
            f"Order ID: {self.order_id} | Customer: {self.customer_name} | "
            f"Restaurant: {self.restaurant_name}"
        )
        print(
            f"{summary} | Amount: {self.total_amount:.2f}"
        )
        print(f"Status: {self.status}")
        if self.delivery_boy_name:
            print(f"Delivery Boy: {self.delivery_boy_name}")

    def display_items(self):
        print(f"{'Item':<20} {'Qty':<6} {'Price':<10} {'Total':<10}")
        for item in self.items:
            line_total = item["quantity"] * item["price"]
            print(
                f"{item['name']:<20} {item['quantity']:<6} "
                f"{item['price']:<10.2f} {line_total:<10.2f}"
            )
