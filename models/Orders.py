class Orders:
    next_id=1
    all_orders={}
    def __init__(self,cust_id,rest_id,item_id):
        self.order_id=Orders.next_id
        self.cust_id=cust_id
        self.rest_id=rest_id
        self.item_id=item_id
        Orders.next_id+=1
        self.status="Pending"
        Orders.all_orders[self.order_id]=self
