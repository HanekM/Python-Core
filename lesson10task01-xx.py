# 1
class ColouredDoors():
    """ """
    colour = 'blue'
    status = 'closed'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    def openDoor(self):
        self.status = 'open'
    
    def closeDoor(self):
        self.status = 'closed'
    
    def toggle(self):
        if self.status == 'closed':
            self.status = 'open'
        else:
            self.status = 'closed'
        

door1 = ColouredDoors(1, 'closed')

print(door1.status)
door1.toggle()
print(door1.status)


# 2
class Door():
    """
    Example for classmethod and how it works
    """
    colour = 'blue'
    
    def __init__(self, number, status):
        self.number = number
        self.status = status
    
    @classmethod
    def paint(cls, colour):
        cls.colour = colour
    
    def statusOpen(self):
        self.status = 'open'
        
    def statusClose(self):
        self.status = 'closed'
    
    def toggle(self):
        if self.status == 'open':
            self.status = 'closed'
        else:
            self.status = 'open'
            
door1 = Door(1,'closed')
print(door1.status) # closed
door1.toggle()
print(door1.status) # open

print(door1.colour) #blue
door1.colour = 'red'
print(door1.colour) #red

print(Door.colour) #blue
Door.colour = 'red'
print(Door.colour) #red
Door.paint('white')
print(Door.colour) #white

