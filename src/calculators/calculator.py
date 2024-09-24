from typing import Dict
from flask import request as FlaskRequest

from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator1:
    """
    This class is responsible for calculating methods.
    """

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        split_number = input_data / 3

        first_process_result = self.__first_process(split_number)
        second_process_result = self.__second_process(split_number)
        final_result = first_process_result + second_process_result + split_number
        response = self.__format_response(final_result)
        return response

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("Number is required!")
        input_data = body["number"]
        return input_data

    def __first_process(self, number: float) -> float:
        first_part = (number / 4) + 7
        second_part = (first_part**2) * 0.257
        return second_part

    def __second_process(self, number: float) -> float:
        first_part = number**2.121
        second_part = (first_part / 5) + 1
        return second_part

    def __format_response(self, result: float) -> Dict:
        return {"data": {"Calculator": 1, "result": round(result, 2)}}
