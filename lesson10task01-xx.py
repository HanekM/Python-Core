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

