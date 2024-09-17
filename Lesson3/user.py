class User:


    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    
    def inf_fname(self):
        print("Имя: ", self.first_name)


    def inf_lname(self):
        print("Фамилмя: ", self.last_name)

    
    def inf_names(self):
        print("Вас зовут", self.first_name, self.last_name)


