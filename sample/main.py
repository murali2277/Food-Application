from sample.Customer import Customer
from sample.Delivery_Boy import DeliveryBoy
from sample.Restaurant import Order, Restaurant


def show_title():
    print("SIMPLE FOOD DELIVERY APP")


def show_role_menu():
    print("\nChoose Role")
    print("1. Customer")
    print("2. Restaurant")
    print("3. Delivery Boy")
    print("0. Exit")


def show_customer_menu(name):
    print(f"\n{name} - Customer Menu")
    print("1. View Restaurants and Menu")
    print("2. Add Item to Cart")
    print("3. View Cart")
    print("4. Place Order")
    print("5. Track My Orders")
    print("6. Switch Role")


def show_restaurant_menu(name):
    print(f"\n{name} - Restaurant Menu")
    print("1. View Menu")
    print("2. Add Menu Item")
    print("3. Update Menu Item")
    print("4. Delete Menu Item")
    print("5. View Orders")
    print("6. Confirm Order")
    print("7. Switch Role")


def show_delivery_menu(name):
    print(f"\n{name} - Delivery Boy Menu")
    print("1. View Assigned Orders")
    print("2. Mark Order Delivered")
    print("3. Switch Role")


def read_number(prompt=">> "):
    value = input(prompt).strip()
    if value.isdigit():
        return int(value)
    return -1


def read_price(prompt):
    value = input(prompt).strip()
    try:
        return float(value)
    except ValueError:
        return -1


class FoodApplication:
    def __init__(self):
        self.customers = {}
        self.restaurants = {}
        self.delivery_boys = {}
        self.orders = {}

        self.current_role = None
        self.current_user = None

        self.seed_predefined_data()

    def seed_predefined_data(self):
        customer1 = Customer("Sakthi", "9876543210", "Gandhipuram", "641012")
        customer2 = Customer("Muthu", "9898989898", "Singanallur", "641005")
        customer3 = Customer("Divya", "9797979797", "Saibaba Colony", "641011")

        self.customers[customer1.customer_name] = customer1
        self.customers[customer2.customer_name] = customer2
        self.customers[customer3.customer_name] = customer3

        rest1 = Restaurant("Kovai Mess", "641012")
        rest1.add_menu_item("Dosa", 55)
        rest1.add_menu_item("Idly", 40)
        rest1.add_menu_item("Veg Meals", 120)

        rest2 = Restaurant("Annapoorna", "641005")
        rest2.add_menu_item("Chapati", 50)
        rest2.add_menu_item("Fried Rice", 140)
        rest2.add_menu_item("Biriyani", 190)

        self.restaurants[rest1.restaurant_name] = rest1
        self.restaurants[rest2.restaurant_name] = rest2

        boy1 = DeliveryBoy("Kumar", "9000000001", "641012")
        boy2 = DeliveryBoy("Ravi", "9000000002", "641005")
        boy3 = DeliveryBoy("Manoj", "9000000003", "641007")

        self.delivery_boys[boy1.delivery_boy_name] = boy1
        self.delivery_boys[boy2.delivery_boy_name] = boy2
        self.delivery_boys[boy3.delivery_boy_name] = boy3

    def profile_name(self, user):
        if hasattr(user, "customer_name"):
            return user.customer_name
        if hasattr(user, "restaurant_name"):
            return user.restaurant_name
        return user.delivery_boy_name

    def choose_profile(self, users, title):
        print(f"\nSelect {title}")
        values = list(users.values())
        for i, user in enumerate(values, 1):
            print(f"{i}. {self.profile_name(user)}")

        option = read_number("Choose profile: ")
        if option < 1 or option > len(values):
            print("Invalid choice.")
            return None
        return values[option - 1]

    def choose_role(self):
        show_role_menu()
        choice = read_number()

        if choice == 1:
            user = self.choose_profile(self.customers, "Customer")
            if user is not None:
                self.current_role = "customer"
                self.current_user = user
        elif choice == 2:
            user = self.choose_profile(self.restaurants, "Restaurant")
            if user is not None:
                self.current_role = "restaurant"
                self.current_user = user
        elif choice == 3:
            user = self.choose_profile(self.delivery_boys, "Delivery Boy")
            if user is not None:
                self.current_role = "delivery"
                self.current_user = user
        elif choice == 0:
            return False
        else:
            print("Please choose a valid role.")

        return True

    def show_restaurants(self):
        print("\nRestaurants")
        for i, restaurant in enumerate(self.restaurants.values(), 1):
            title = (
                f"{i}. {restaurant.restaurant_name} "
                f"(Pincode: {restaurant.pincode})"
            )
            print(title)
            restaurant.display_menu()

    def choose_restaurant(self):
        values = list(self.restaurants.values())
        print("\nChoose Restaurant")
        for i, restaurant in enumerate(values, 1):
            print(f"{i}. {restaurant.restaurant_name}")

        option = read_number("Restaurant number: ")
        if option < 1 or option > len(values):
            print("Invalid restaurant.")
            return None
        return values[option - 1]

    def add_item_to_cart(self):
        customer = self.current_user
        restaurant = self.choose_restaurant()
        if restaurant is None:
            return

        if len(restaurant.menu) == 0:
            print("Selected restaurant has no menu items.")
            return

        has_other_restaurant_cart = (
            customer.cart_restaurant is not None
            and customer.cart_restaurant != restaurant.restaurant_name
        )
        if has_other_restaurant_cart:
            print("Your cart has items from another restaurant.")
            print("Please place current cart first.")
            return

        restaurant.display_menu()
        item_id = read_number("Enter item ID: ")
        quantity = read_number("Enter quantity: ")

        if quantity <= 0:
            print("Quantity should be greater than 0.")
            return

        menu_item = restaurant.get_menu_item(item_id)
        if menu_item is None:
            print("Menu item not found.")
            return

        customer.cart_restaurant = restaurant.restaurant_name
        customer.add_to_cart(
            menu_item.item_id,
            menu_item.name,
            menu_item.price,
            quantity,
        )
        print(f"Added {quantity} x {menu_item.name} to cart.")

    def assign_delivery_boy(self, pincode):
        for boy in self.delivery_boys.values():
            if boy.is_available and boy.pincode == pincode:
                return boy

        for boy in self.delivery_boys.values():
            if boy.is_available:
                return boy
        return None

    def place_order(self):
        customer = self.current_user
        if len(customer.cart) == 0:
            print("Cart is empty.")
            return

        item_snapshot = []
        for item in customer.cart.values():
            item_snapshot.append(
                {
                    "name": item["name"],
                    "quantity": item["quantity"],
                    "price": item["price"],
                }
            )

        order = Order(
            customer.customer_name,
            customer.pincode,
            customer.cart_restaurant,
            item_snapshot,
            customer.cart_total(),
        )

        delivery_boy = self.assign_delivery_boy(customer.pincode)
        if delivery_boy is not None:
            delivery_boy.assign_order(order.order_id)
            order.delivery_boy_name = delivery_boy.delivery_boy_name
            order.status = "Assigned to Delivery Boy"
        else:
            order.status = "Placed"

        self.orders[order.order_id] = order
        customer.add_order(order.order_id)
        customer.clear_cart()

        print(f"Order placed successfully. Order ID: {order.order_id}")
        if order.delivery_boy_name:
            print(f"Assigned to delivery boy: {order.delivery_boy_name}")

    def customer_orders(self, customer_name):
        result = []
        for order in self.orders.values():
            if order.customer_name == customer_name:
                result.append(order)
        return result

    def track_my_orders(self):
        orders = self.customer_orders(self.current_user.customer_name)
        if len(orders) == 0:
            print("No orders found.")
            return

        print("\nMy Orders")
        for order in orders:
            order.display_summary()
            order.display_items()

    def restaurant_orders(self, restaurant_name):
        result = []
        for order in self.orders.values():
            if order.restaurant_name == restaurant_name:
                result.append(order)
        return result

    def restaurant_view_orders(self):
        orders = self.restaurant_orders(self.current_user.restaurant_name)
        if len(orders) == 0:
            print("No orders found for this restaurant.")
            return

        print("\nRestaurant Orders")
        for order in orders:
            order.display_summary()

    def restaurant_confirm_order(self):
        pending = []
        for order in self.restaurant_orders(self.current_user.restaurant_name):
            if order.status in ("Placed", "Assigned to Delivery Boy"):
                pending.append(order)

        if len(pending) == 0:
            print("No pending orders to confirm.")
            return

        for order in pending:
            print(
                f"Order ID {order.order_id} "
                f"- Current Status: {order.status}"
            )

        order_id = read_number("Enter order ID to confirm: ")
        selected = None
        for order in pending:
            if order.order_id == order_id:
                selected = order
                break

        if selected is None:
            print("Order not found.")
            return

        selected.status = "Restaurant Confirmed"
        print(f"Order {selected.order_id} confirmed.")

    def restaurant_add_menu_item(self):
        name = input("Item name: ").strip()
        price = read_price("Price: ")
        if name == "" or price <= 0:
            print("Invalid item details.")
            return
        self.current_user.add_menu_item(name, price)

    def restaurant_update_menu_item(self):
        self.current_user.display_menu()
        item_id = read_number("Item ID to update: ")
        name = input("New item name: ").strip()
        price = read_price("New price: ")
        if name == "" or price <= 0:
            print("Invalid item details.")
            return
        self.current_user.update_menu_item(item_id, name, price)

    def restaurant_delete_menu_item(self):
        self.current_user.display_menu()
        item_id = read_number("Item ID to delete: ")
        self.current_user.delete_menu_item(item_id)

    def delivery_assigned_orders(self, boy_name):
        result = []
        for order in self.orders.values():
            if (
                order.delivery_boy_name == boy_name
                and order.status != "Delivered"
            ):
                result.append(order)
        return result

    def view_assigned_orders(self):
        orders = self.delivery_assigned_orders(
            self.current_user.delivery_boy_name
        )
        if len(orders) == 0:
            print("No active assigned orders.")
            return

        print("\nAssigned Orders")
        for order in orders:
            order.display_summary()

    def mark_order_delivered(self):
        orders = self.delivery_assigned_orders(
            self.current_user.delivery_boy_name
        )
        if len(orders) == 0:
            print("No active assigned orders.")
            return

        for order in orders:
            print(f"Order ID {order.order_id} - {order.status}")

        order_id = read_number("Order ID to mark delivered: ")
        selected = None
        for order in orders:
            if order.order_id == order_id:
                selected = order
                break

        if selected is None:
            print("Order not found.")
            return

        selected.status = "Delivered"
        self.current_user.close_order(selected.order_id)
        print(f"Order {selected.order_id} marked as delivered.")

    def run_customer_flow(self):
        while self.current_role == "customer":
            show_customer_menu(self.current_user.customer_name)
            choice = read_number()

            if choice == 1:
                self.show_restaurants()
            elif choice == 2:
                self.add_item_to_cart()
            elif choice == 3:
                self.current_user.display_cart()
            elif choice == 4:
                self.place_order()
            elif choice == 5:
                self.track_my_orders()
            elif choice == 6:
                self.current_role = None
                self.current_user = None
            else:
                print("Choose a valid option.")

    def run_restaurant_flow(self):
        while self.current_role == "restaurant":
            show_restaurant_menu(self.current_user.restaurant_name)
            choice = read_number()

            if choice == 1:
                self.current_user.display_menu()
            elif choice == 2:
                self.restaurant_add_menu_item()
            elif choice == 3:
                self.restaurant_update_menu_item()
            elif choice == 4:
                self.restaurant_delete_menu_item()
            elif choice == 5:
                self.restaurant_view_orders()
            elif choice == 6:
                self.restaurant_confirm_order()
            elif choice == 7:
                self.current_role = None
                self.current_user = None
            else:
                print("Choose a valid option.")

    def run_delivery_flow(self):
        while self.current_role == "delivery":
            show_delivery_menu(self.current_user.delivery_boy_name)
            choice = read_number()

            if choice == 1:
                self.view_assigned_orders()
            elif choice == 2:
                self.mark_order_delivered()
            elif choice == 3:
                self.current_role = None
                self.current_user = None
            else:
                print("Choose a valid option.")

    def run(self):
        show_title()
        while True:
            if self.current_role is None:
                keep_running = self.choose_role()
                if not keep_running:
                    print("\nGoodbye!")
                    break

            if self.current_role == "customer":
                self.run_customer_flow()
            elif self.current_role == "restaurant":
                self.run_restaurant_flow()
            elif self.current_role == "delivery":
                self.run_delivery_flow()


if __name__ == "__main__":
    app = FoodApplication()
    app.run()
