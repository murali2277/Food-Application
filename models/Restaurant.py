class Restaurant:
    next_id=1
    all_restaurant={}
    def __init__(self,resaturant_name,address):
        self.id=Restaurant.next_id
        self.resaturant_name=resaturant_name
        self.address=address
        Restaurant.next_id+=1
        self.menu={
            1:'Idly',
            2:'Dosa',
            3:'Chappti'
        }
        Restaurant.all_restaurant[self.id]=self
        
        