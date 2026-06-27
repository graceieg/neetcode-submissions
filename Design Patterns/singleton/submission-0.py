class Singleton:

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if not hasattr(cls, '_instance'):
        # Use super() to call the object allocator
            cls._instance = super().__new__(cls)
        return cls._instance
        
    def getValue(self) -> str:
        return self.attribute
    def setValue(self, value: str):
        self.attribute = value
