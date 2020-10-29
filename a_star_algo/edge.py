class edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

    def get_from_node(self):
        return self.from_node
    
    def get_to_node(self):
        return self.to_node
    
    def get_weight(self):
        return self.weight
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.from_node != other.from_node:
                return False
            if self.to_node != other.to_node:
                return False
            if self.weight == other.to_node:
                return True
        else:
            return False