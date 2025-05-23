# Encapsultion

class Order():

    def __init__(self, cname, items, total, discount, feedback):
        self.cname = cname
        self.items = items
        self.__total = total
        self.__discount = discount
        self.__feedback = feedback
        

    def __calculate_oreder_price(self):

        return self.__total - self.__discount
    
    def _admin_view_order_details(self):

        return {
            "customer": self.cname,
            "item": self.items,
            "total": self.__total,
            "discount": self.__discount,
            "final_price": self.__calculate_oreder_price(),
            "feedback": self.get_feedback()
        }
    
    def customer_view_order_details(self):
        self.update_feedback("good")

        return {
            "customer": self.cname,
            "item": self.items,           
            "final_price": self.__calculate_oreder_price()
        }
    
    def get_feedback(self):
        return self.__feedback
    
    def update_feedback(self, feedback):
        self.__feedback = feedback
    

    

class AdminView():

    def show_order(self, objects):
        return objects._admin_view_order_details()


class CustomerView():

    def show_order(self, objects):
        return objects.customer_view_order_details()


    
o1 = Order("ragu", ["cake", "fruits"], 100, 25, "Bad")

# print(o1._admin_view_order_details())
# print(o1.customer_view_order_details())

admin =AdminView()
customer = CustomerView()

print("ADMIN-->", admin.show_order(o1))
print("CUSTOMER -->", customer.show_order(o1))

print("ADMIN-->", admin.show_order(o1))




# print(o1.__calculate_oreder_price()) # it won't work private method never call outside the class
# # # AttributeError: 'Order' object has no attribute '__calculate_oreder_price'. Did you mean: '_Order__calculate_oreder_price'?


