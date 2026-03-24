from controllers.auth_controller import AuthController
from controllers.customer_controller import CustomerController
from controllers.delivery_boy_controller import DeliveryController
from controllers.restaurant_controller import RestaurantController
from models.Restaurant import Restaurant

def main():
    auth=AuthController()
    customer=CustomerController()
    delivery=DeliveryController()
    rest=RestaurantController()
    
    while True:
        if auth.current_user is None:
            auth.show_menu()
        elif auth.current_role=='Customer':
            customer.show_menu()
        elif auth.current_role=='Restaurant':
            rest.show_menu()
        elif auth.current_role=='Delivery':
            delivery.show_menu()

if __name__=='__main__':
    main()