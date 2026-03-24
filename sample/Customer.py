class Customer:
    next_id = 1

    def __init__(self, name, phone_number, address, pincode):
        self.customer_id = Customer.next_id
        Customer.next_id += 1

        self.customer_name = name
        self.phone_number = phone_number
        self.address = address
        self.pincode = pincode

        self.cart = {}
        self.cart_restaurant = None
        self.order_ids = []

        self.total_orders = 0
        self.restaurant_ratings = []

    def add_to_cart(self, item_id, item_name, price, quantity):
        if item_id in self.cart:
            self.cart[item_id]["quantity"] += quantity
        else:
            self.cart[item_id] = {
                "name": item_name,
                "price": price,
                "quantity": quantity,
            }

    def clear_cart(self):
        self.cart = {}
        self.cart_restaurant = None

    def cart_total(self):
        total = 0
        for item in self.cart.values():
            total += item["price"] * item["quantity"]
        return total

    def display_cart(self):
        if len(self.cart) == 0:
            print("Your cart is empty.")
            return

        print("\nYour Cart")
        print(f"Restaurant: {self.cart_restaurant}")
        print(f"{'ID':<5} {'Item':<20} {'Qty':<6} {'Price':<10} {'Total':<10}")
        for item_id, item in self.cart.items():
            line_total = item["price"] * item["quantity"]
            print(
                f"{item_id:<5} {item['name']:<20} {item['quantity']:<6} "
                f"{item['price']:<10.2f} {line_total:<10.2f}"
            )
        print(f"Grand Total: {self.cart_total():.2f}")

    def add_order(self, order_id):
        self.order_ids.append(order_id)
        self.total_orders += 1

    def add_restaurant_rating(self, rating):
        self.restaurant_ratings.append(rating)

    def average_rating(self):
        if len(self.restaurant_ratings) == 0:
            return 0
        return sum(self.restaurant_ratings) / len(self.restaurant_ratings)
