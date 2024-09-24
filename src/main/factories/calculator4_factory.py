from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_4 import Calculator4


def calculator4_factory() -> Calculator4:
    """
    This method is a factory responsible for creating a Calculator4 object.
    :return: A Calculator4 object.
    """
    numpy_handler = NumpyHandler()
    return Calculator4(numpy_handler)
