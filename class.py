class Car(object):

    def __init__(self,model,color,company, speed_limit):
        self.color= color
        self.model= model
        self.company= company
        self.speed_limit = speed_limit

    def start(self):
        print("started")

    def stop(self):
        print("Stopped")

    def accelarate(self):
        print("accelareted")

audi = Car("A6", "Red", "Audi", 80) 

print(audi.start())

print(audi.stop())