class Cell:
    def __init__(self):
        self.value = None
        self.directions = None
    
    
    def __str__(self):
        value = "None" if self.value is None else str(self.value)
        direction = "None" if self.directions is None else str(self.directions)
        return f"Value: {value}, Direction: {direction}"