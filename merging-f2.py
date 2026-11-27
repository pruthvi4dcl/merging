from abc import ABC, abstractmethod

class Dollor(ABC):
    def __init__(self,val):
        self.val=val
    @abstractmethod
    def __add__(self, other):
        pass

obj=object()