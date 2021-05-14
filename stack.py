class Stack(list):


    def __init__(self):
        self._type = "stack"


    def push(self, data):
        if self._type == "stack":
            self.insert(0, int(data))
        else:
            self.apped(int(data))


    def put_off(self):
        if self._type == "stack":
            self.pop(0)
        else:
            self.pop(len(self) - 1)


    def print_all(self):
        [print(value) for value in self]
