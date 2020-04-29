# 1
class Door():
    colour = 'white'
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
        super().__init__(number, status)
        self.locked = locked
        
    def open(self):
        if self.locked:
            return super().open()
            
    def close_and_lock(self):
        self.locked = True
        self.status = 'closed'
        
    def close(self, locked=True):
        self.status = 'closed'
        self.locked = locked
        
sdoor = LockedDoor(1, 'closed', True)
print(sdoor.__class__.__dict__)

# 1.1
class Door():
    
    colour = 'white'
    def __init__(self, number, status):
        self.number = number
        self.status = status
    
    def open(self):
        self.status = 'open'
    
    def close(self):
        self.status = 'closed'
    
class SecuredDoor(Door):
    locked = True
    colour = 'black'
    
    def __init__(self, number, status, locked=False):
        super().__init__(number, status)
        self.locked = locked
        
    def close(self):
        if not self.locked:
            return super().close()
        
    
    def close_and_lock(self):
        super().close()
        self.locked = True

sdoor = SecuredDoor(1, 'open')

print(sdoor.status)
sdoor.close_and_lock()
print(sdoor.status)



# 2
class Example():
    
    def __init__(self, value):
        self.value = value
    def __len__(self):
        return len(str(self.value))
    def contains(self, digit):
        if str(digit) in str(self.value):
            return True
        else:
            return False  
    def __str__(self):
        return super().__str__() + '[{}]'.format(self.value)
        
example = Example(213132)
print(example.__str__)
