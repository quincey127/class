class Car(object):
    def __init__(self,model,color,company):
        self.color=color
        self.model=model
        self.company=company
    def start(self):
        print("car is started")
    def stop(self):
        print("car is stopped")

nachomobile=Car("n15","gold","nachoinc")
print(nachomobile.color)
nachomobile.start()
nachomobile.stop()
