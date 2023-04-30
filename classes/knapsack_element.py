from dataclasses import dataclass

@dataclass
class KnapsackElement():
    weight:int 
    value:int

    def get_weight(self):
        return self.weight
    
    def get_value(self):
        return self.value