


class CargoHold:

    def __init__(self, max_cap):
        self.max_cap = max_cap
        self.cur_cap = 0


    def add_good(self, good_type, quantity):
        if self.cur_cap + quantity > self.max_cap:
            print("No room in cargo hold")
            return
        else:
            self.cur_cap += quantity

    def remove_good(selfself, good_type, quantity):
        if self.cur_cap - quantity < 0:
            print("Cannot more goods than actual amount of good in cargo hold")
            return
        else:
            self.cur_cap -= quantity

    def is_full(self):
        return self.cur_cap == self.max_cap

    def get_cur_cap(self):
        return self.cur_cap

    def get_max_cap(self):
        return self.max_cap