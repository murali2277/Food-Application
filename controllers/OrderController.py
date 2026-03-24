from models.Orders import Orders
from models.Restaurant import Restaurant
from views.Restaurant_views import RestaruantView
class OrderController:
    def book_order(self,cust_id):
        RestaruantView.view_restaurant()
        rest_id=int(input("Enter the Restaurant ID"))
        item_id=int(input("Enter the Items ID"))
        if self.isavailable(rest_id,item_id):
            new_order=Orders(cust_id,rest_id,item_id)
            return new_order
        else:
            print("Choose the correct available item")

    def isavailable(self,rest_id,item_id):
        if rest_id not in Restaurant.all_restaurant:
            return False
        elif rest_id in Restaurant.all_restaurant and item_id not in Restaurant.all_restaurant[rest_id].menu:
            return False
        return True
    
    def orderStatus(self,user):
        if len(user.orders)==0:
            print("No orders")
            return
        else:
            print(f"{'Order ID':<5} {'Rest ID':<5} {'Item Id':<5} Status")
            for user_orders in user.orders.values():
                print(f"{user_orders.order_id:<5} {user_orders.rest_id:<5} {user_orders.item_id:<5} {user_orders.status}")
    def deleteorder(self,user):
        if len(user.orders)==0:
            print("No orders")
            return
        self.orderStatus(user)
        order_id=int(input("Enter the Order ID: "))
        del user.orders[order_id]
        del Orders.all_orders[order_id]
        print("Order canceled successfully")