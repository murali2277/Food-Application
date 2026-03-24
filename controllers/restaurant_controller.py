from controllers.auth_controller import AuthController
from views.Restaurant_views import RestaruantView
class RestaurantController:

    user=AuthController.current_user

    def show_menu(self):
        RestaruantView.show_restaurant_menu()
        option=int(input("Enter the option"))
        if option==1:
            self.add_menu()
        elif option==4:
            self.view_menu_items()
    
    def view_menu_items(self):
        RestaruantView.view_restaurant()

    def add_menu(self):
        RestaruantView.add_menu()
        item_name=input("Enter the menu name")
        if item_name in user.menu():
            print("Item already in menu list")
        else:
            next_id=len(user.menu)
            user.menu[next_id]=item_name

