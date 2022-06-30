class Test:
    def __init__(self, _thing):
        self.thing = _thing
    
    def give_type(self):
        return type(self.thing)