class Customer:
    next_id=1
    def __init__(self, name, email, password, pincode):
        self.id=Customer.next_id
        self.name = name
        self.email = email
        self.password = password
        self.pincode = pincode
        Customer.next_id+=1
        self.orders={}