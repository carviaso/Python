from abc import abstractmethod, ABC

class FiguraAbstracta(ABC):
    @abstractmethod
    def calcularArea(self):
        pass

    @abstractmethod
    def calcularPerimetro(self):
        pass

