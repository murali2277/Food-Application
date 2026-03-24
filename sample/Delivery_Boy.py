class DeliveryBoy:
    next_id = 1

    def __init__(self, name, phone_number, pincode):
        self.delivery_boy_id = DeliveryBoy.next_id
        DeliveryBoy.next_id += 1

        self.delivery_boy_name = name
        self.phone_number = phone_number
        self.pincode = pincode

        self.is_available = True
        self.active_order_ids = []
        self.completed_orders = 0
        self.customer_ratings = []

    def assign_order(self, order_id):
        self.active_order_ids.append(order_id)
        self.is_available = False

    def close_order(self, order_id):
        if order_id in self.active_order_ids:
            self.active_order_ids.remove(order_id)
            self.completed_orders += 1
        if len(self.active_order_ids) == 0:
            self.is_available = True

    def add_customer_rating(self, rating):
        self.customer_ratings.append(rating)

    def average_rating(self):
        if len(self.customer_ratings) == 0:
            return 0
        return sum(self.customer_ratings) / len(self.customer_ratings)
