"""
This module is responsible for calculating the result of the calculator 2.
"""
from typing import Dict, List
from flask import request as FlaskRequest

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface


class Calculator2:
    """
    This class is responsible for calculating methods.
    """

    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        """
        This method is responsible for calculating the result.
        :param request: FlaskRequest
        :return: Dict
        """
        body = request.json
        input_data = self.__validate_body(body)
        calculated_number = self.__process_data(input_data)
        return self.__format_response(calculated_number)

    @staticmethod
    def __validate_body(body: Dict) -> List[float]:
        """
        This method is responsible for validating the body.
        :param body: Dict
        :return: List[float]
        """
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Numbers is required!")
        input_data = body["numbers"]
        return input_data

    def __process_data(self, input_data: List[float]) -> float:
        """
        This method is responsible for processing the data.
        :param input_data:
        :return: List[float]
        """
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = self.__driver_handler.standard_deviation(first_process_result)
        return 1 / result

    @staticmethod
    def __format_response(result: float) -> Dict:
        """
        This method is responsible for formatting the response.
        :param result: float
        :return: Dict
        """
        return {"data": {"Calculator": 2, "result": round(result, 2)}}
