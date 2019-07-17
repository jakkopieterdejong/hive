class HiveMatch:
    
    def __init__(self, name_w, name_b):
        self.name_w = name_w
        self.name_b = name_b
        self.moves = []
        self.turn_w = True
            
    def __str__(self):  
        return "A Hive match between {} (white) and {} (black).".format(self.name_w, self.name_b)
        
    def print_moves(self):
        for m in self.moves:
            print(m)
        
    def __repr__(self):
        return "HiveMatch(name_w = {}, name_b = {})".format(self.name_w, self.name_b)
    
    def add_move(self, move_str):
        self.moves.append(move_str)
    
    # WIP
    def cancel_move(self):
        pass
    
    # WIP
    def new_match(self):
        pass
    
    # WIP
    def print_board(self, turn=None):
        pass
    
    # WIP: alternative constructor
    @classmethod
    def from_move_list(cls, move_list):
        return cls("Dummy", "Dummy")
        


hm_1 = HiveMatch("Otto", "Bernard")
print(str(hm_1))

hm_1.print_moves()
hm_1.add_move("wQ")
hm_1.add_move("bA-")
hm_1.print_moves()
