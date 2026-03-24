from controllers.auth_controller import AuthController
from models.Restaurant import Restaurant
class RestaruantView:
    @staticmethod
    def show_restaurant_menu():
        print("1.Add Menu Item")
        print("2.Update Menu Item")
        print("3.View Orders")
        print("4.View Menu Item")
        print("0.Logout")
    @staticmethod
    def view_restaurant():
        if len(Restaurant.all_restaurant)==0:
            print("No Restaurnat List")
            return
        else:
            for rest_key,rest in Restaurant.all_restaurant.items():
                print(f"\nRestaurant Name:{rest.resaturant_name}")
                print(f"{'Rest ID':<5}{'ID':<5} {'Menu Item'}")
                for key,items in rest.menu.items():
                    print(f"\n{rest_key:<5} {key:<5} {items}")
            print('\n')
    @staticmethod
    def add_menu():
        print("Add mennu")