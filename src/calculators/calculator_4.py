"""
This module contains the implementation of the fourth calculator, which calculates the mean.
"""
from typing import Dict, List

from flask import request as FlaskRequest

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        """
        This class is responsible for calculating the mean of a list of numbers.
        :param driver_handler: DriverHandlerInterface
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
        average = self.__calculate_mean(self, input_data)
        return self.__format_response(average)

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

    @staticmethod
    def __calculate_mean(self, numbers: List[float]) -> float:
        """
        This method is responsible for calculating the mean.
        :param self:
        :param numbers: List[float]
        :return: float
        """
        return self.__driver_handler.mean(numbers)

    @staticmethod
    def __format_response(average: float) -> Dict:
        """
        This method is responsible for formatting the response.
        :param average: float
        :return: Dict
        """
        return {"data": {"Calculator": 4, "result": average, "Success": True}}
