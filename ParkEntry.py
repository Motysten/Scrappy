class ParkEntry:
    def __init__(self, name, address, capacity, left, owner, link):
        self.name = name
        self.address = address
        self.capacity = capacity
        self.left = left
        self.owner = owner
        self.link = link
        
    def getDictEntry(self):
        return {
            "name":self.name,
            "address":self.address,
            "capacity":self.capacity,
            "left":self.left,
            "owner":self.owner,
            "link":self.link
        }