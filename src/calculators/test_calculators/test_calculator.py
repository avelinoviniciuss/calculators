from typing import Dict, List

import pytest
from pytest import raises

from src.calculators.calculator_4 import Calculator4
from src.calculators.calculator import Calculator1
from src.calculators.calculator_2 import Calculator2
from src.calculators.calculator_3 import Calculator3
from src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandler:
    """
    This class is responsible for handling the numpy library
    """

    def standard_deviation(self, numbers: List[float]) -> float:
        """
        This method is responsible for calculating the standard deviation.
        :param numbers:
        :return:
        """
        return 3


class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        """
        This method is responsible for calculating the variance.
        :param numbers: List[float]
        :return: float
        """
        return 3


class MockDriverHandlerVariance:
    def variance(self, numbers: List[float]) -> float:
        """
        This method is responsible for calculating the variance.
        :param numbers: List[float]
        :return: float
        """
        return 100000


class MockDriverHandlerMean:
    def mean(self, numbers: List[float]) -> float:
        """
        This method is responsible for calculating the mean.
        :param numbers: List[float]
        :return: float
        """
        return 3


def test_calculate() -> None:
    calc = Calculator1()
    mock_request = MockRequest(body={"number": 3})
    response = calc.calculate(mock_request)
    assert response == {"data": {"Calculator": 1, "result": 15.71}}
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "result" in response["data"]

    assert response["data"]["Calculator"] == 1
    assert response["data"]["result"] == 15.71


def test_calculate_with_body_error() -> None:
    mock_request = MockRequest(body={})
    calc = Calculator1()

    with pytest.raises(ValueError) as exc:
        calc.calculate(mock_request)

    assert str(exc.value) == "Number is required!"


# Integração entre NumpyHandler e Calculator2
def test_calculator2_integration() -> None:
    driver = NumpyHandler()
    calc = Calculator2(driver)
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    formatted_response = calc.calculate(mock_request)
    print(formatted_response)


def test_calculator2() -> None:
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = MockDriverHandler()
    calc = Calculator2(driver)
    formatted_response = calc.calculate(mock_request)

    assert isinstance(formatted_response, dict)
    assert formatted_response == {"data": {"Calculator": 2, "result": 0.33}}


# Testes calculadora 3
def test_calculator3_with_variance_error() -> None:
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandlerError())

    with raises(Exception) as exc:
        calculator_3.calculate(mock_request)

    assert str(exc.value) == "Error: Variance is less than multiplication!"


def test_calculator3_successfully() -> None:
    mock_request = MockRequest(body={"numbers": [1, 1, 1, 1, 100]})
    calculator_3 = Calculator3(MockDriverHandlerVariance())

    response = calculator_3.calculate(mock_request)

    assert response == {"data": {"Calculator": 3, "Success": True, "result": 100000}}


def test_calculator4_successfully() -> None:
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})
    calculator_4 = Calculator4(MockDriverHandlerMean())

    response = calculator_4.calculate(mock_request)

    assert response == {"data": {"Calculator": 4, "Success": True, "result": 3}}
