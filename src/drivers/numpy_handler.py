from typing import List
import numpy
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class NumpyHandler(DriverHandlerInterface):
    """
    This class is responsible for handling the numpy library.
    """

    def __init__(self) -> None:
        self.__np = numpy

    def standard_deviation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)

    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)

    def mean(self, numbers: List[float]) -> float:
        return self.__np.mean(numbers)
