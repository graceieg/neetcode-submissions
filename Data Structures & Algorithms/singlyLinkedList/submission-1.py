class LinkedList:
    
    def __init__(self):
        self.items = []
    
    def get(self, index: int) -> int:
        if 0 <= index < len(self.items):
            item = self.items[index]
            return item
        else: 
            return -1

    def insertHead(self, val: int) -> None:
        if val is not None:
            self.items.insert(0, val)
        else:
            return None

    def insertTail(self, val: int) -> None:
        if val is not None: 
            self.items.append(val)
        else:
            return None

    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.items):
            del self.items[index]
            return True
        else:
            return False

    def getValues(self):
        for index in self.items:
            print(index)
        return self.items
