from src.drivers.numpy_handler import NumpyHandler
from src.calculators.calculator_3 import Calculator3


def calculator3_factory() -> Calculator3:
    numpy_handler = NumpyHandler()
    return Calculator3(numpy_handler)
