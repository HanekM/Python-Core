class Door():
    colour = 'whire'
    def __init__(self, number, status):
        self.status = status
        self.number = number
    def open(self):
        self.status = 'open'
    def close(self):
        self.status = 'closed'

class LockedDoor(Door):
    colour = 'black'
    locked = True
    
    def __init__(self, number, status, locked):
        self.number = number
        self.status = status
        self.locked = locked
    def open(self):
        if not self.locked:
            self.status = 'open'
            
    def close_and_lock(self):
        self.locked = True
        self.status = 'closed'
        
    def close(self, locked=True):
        self.status = 'closed'
        self.locked = locked
    

sdoor = LockedDoor(1, 'closed', True)

