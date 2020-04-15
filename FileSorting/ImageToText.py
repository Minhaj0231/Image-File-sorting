from abc import ABC, abstractmethod
class ImageToText(ABC):
    @abstractmethod
    def toText(self):
        pass
