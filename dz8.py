class worker():
    def __init__(self,salary=30):
        self.salary=salary
    def work(self,salary):
        print('зарплата человека',self.salary)
    def __del__(self):
        print("object deleted")

class driver(worker):
    def __init__(self,salary=50):
        self.salary=salary
        def work(self):
            print("driver deleted")
    __has_car= True
john=worker()
john.work