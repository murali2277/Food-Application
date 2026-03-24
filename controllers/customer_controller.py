from views.customer_views import CutomerView
from views.Restaurant_views import RestaruantView
from controllers.OrderController import OrderController
from controllers.auth_controller import AuthController
class CustomerController:
    def __init__(self):
        self.order=OrderController()
    def show_menu(self):
        user=AuthController.current_user
        if user is None:
            print("Please login first.")
            return
        CutomerView.customer_menu()
        option=int(input("Enter the Option: "))
        if option==1:
            #view restaurnat
            #self.view_restaurnat_list()
            RestaruantView.view_restaurant()
        elif option==4:
            cust_id=user
            new_order=self.order.book_order(cust_id)
            user.orders[new_order.order_id]=new_order
        elif option==2:
            print(user)
            self.order.orderStatus(user)
        elif option==3:
            self.order.deleteorder(user)


        # elif option==2:
        #     #track order
        #     pass
        # elif option==0:
        #     #logout
        #     pass
    # def view_restaurnat_list(self):
    #     RestaruantView.view_restaurant()