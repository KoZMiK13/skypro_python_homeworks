class Smartphone:


    def __init__(self, name, model, number):
        self.name = name
        self.model = model
        self.number = number

    
    def info(self):
        print(f"{self.name} - {self.model}, {self.number}")