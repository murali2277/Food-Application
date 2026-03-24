from models.Customer import Customer
from models.DeliveryBoy import DeliveryBoy 
from models.Restaurant import Restaurant
from views.auth_views import AuthView
from models.Restaurant import Restaurant

class AuthController:
    current_user=None
    current_role=None
    def __init__(self):
        self.cust=Customer("MK", "mk@example.com", "2277", "123456")
        self.rest=Restaurant("Kovai kitchen", "1234")
        self.delivery=DeliveryBoy("John", "d@gmail.com", "1234")
    def show_menu(self):
        AuthView.show_auth_menu()
        choice=int(input("Enter your choice: "))
        if choice==1:
            self.current_user=self.cust
            self.current_role="Customer"
            AuthController.current_user=self.cust
            AuthController.current_role="Customer"
            print("Customer registered successfully!")
        elif choice==2:
            self.current_user=self.delivery
            self.current_role="Delivery"
            AuthController.current_user=self.delivery
            AuthController.current_role="Delivery"
            print("Delivery Boy registered successfully!")
        elif choice==3:
            self.current_user=self.rest
            self.current_role="Restaurant"
            AuthController.current_user=self.rest
            AuthController.current_role="Restaurant"
            print("Restaurant registered successfully!")