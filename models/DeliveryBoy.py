class DeliveryBoy:
    next_id=1
    def __init__(self, name, email, password):
        self.id=DeliveryBoy.next_id
        self.name = name
        self.email = email
        self.password = password
        DeliveryBoy.next_id+=1