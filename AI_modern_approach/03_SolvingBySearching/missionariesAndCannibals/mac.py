class Bank:
    def __init__(self, n_can, n_miss, has_boat):
        self.n_can = n_can
        self.n_miss = n_miss
        self.has_boat = has_boat

    def cross(self, n_can, n_miss, other_bank):
        if self.has_boat:
            self.n_can -= n_can
            self.n_miss -= n_miss
            other_bank.n_can += n_can
            other_bank.n_miss += n_miss
            self.has_boat = False
            other_bank.has_boat = True
        
    def is_legal_state(self):
        if self.n_can > n_miss:
            return False
        if self.n_can < 0 or self.n_miss < 0:
            return False
        return True
            

class World:
    bank1 = Bank(3, 3, True)
    bank2 = Bank(0, 0, False)
    
