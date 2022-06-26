class Prompt:
    def __init__(self):
        self.input = input('> ')

    @property 
    def arguments(self):
        return self.input.split(' ')[1:]
    
    @property 
    def command(self):
        return self.input.split(' ')[0]