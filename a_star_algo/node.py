import enum

#enum for state
class NodeState(enum.Enum):
    CLOSED = 1
    OPEN = 2
    START = 3
    END = 4

class node:
    #latitude lines measure your position north/south
    #longitude lines measure your position east/west

    #initializer
    def __init__(self, lat, long, state):
        self.lat = lat
        self.long = long
        self.edges = []
        self.state = state
    
    def get_pos(self):
        return self.lat, self.long

    def add_edge(self, edge):
        self.edges.append(edge)
    
    def remove_edge(self, edge):
        if edge in self.edges:
            self.edges.remove(edge)
    
    def set_state(self, newState):
        self.state = newState
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            if self.lat != other.lat:
                return False
            if self.long != other.long:
                return False
            if self.state == other.state:
                return True
        else:
            return False