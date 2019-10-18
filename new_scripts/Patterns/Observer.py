class Notifier(object):
    def __init__(self):
        self.__observers = list()
    
    def attach(self, observer : Observer):
        self.__observers.append(observer)
    
    def dettach(self, observer: Observer):
        self.__observers.remove(observer)
    
    def notify(self):
        map(lambda x: x.update(), self.__observers)
    
class Observer(object):
    def update(self):
        raise NotImplementedError