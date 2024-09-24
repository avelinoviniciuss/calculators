"""
This module defines the Calculator3 class, responsible for calculating the variance of a list of numbers.
"""
from typing import Dict, List

from flask import request as FlaskRequest

from src.errors.http_bad_request import HttpBadRequestError
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        """
        This class is responsible for calculating the variance of a list of numbers.
        :param driver_handler:  DriverHandlerInterface
        """
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        """
        This method is responsible for calculating the result.
        :param request: FlaskRequest
        :return: Dict
        """
        body = request.json
        input_data = self.__validate_body(body)

        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__verify_results(variance, multiplication)
        return self.__format_response(variance)

    @staticmethod
    def __validate_body(body: Dict) -> List[float]:
        """
        This method is responsible for validating the body.
        :param body: Dict
        :return: List[float]
        """
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Body is not as expected!")

        input_data = body["numbers"]
        return input_data

    def __calculate_variance(self, numbers: List[float]) -> float:
        """
        This method is responsible for calculating the variance.
        :param numbers: List[float]
        :return: float
        """
        return self.__driver_handler.variance(numbers)

    @staticmethod
    def __calculate_multiplication(numbers: List[float]) -> float:
        """
        This method is responsible for calculating the multiplication.
        :param numbers: List[float]
        :return: float
        """
        multiplication = 1
        for num in numbers:
            multiplication *= num
        return multiplication

    @staticmethod
    def __verify_results(variance: float, multiplication: float) -> None:
        """
        This method is responsible for verifying the results.
        :param variance: float
        :param multiplication: float
        :return: None
        """
        if variance < multiplication:
            raise HttpBadRequestError("Error: Variance is less than multiplication!")

    @staticmethod
    def __format_response(variance: float) -> Dict:
        """
        This method is responsible for formatting the response.
        :param variance: float
        :return: Dict
        """
        return {"data": {"Calculator": 3, "result": variance, "Success": True}}
