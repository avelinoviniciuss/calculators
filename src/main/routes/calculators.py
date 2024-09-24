"""
This module is responsible for the routes of the calculators.
"""
from flask import Blueprint, request, jsonify

from src.errors.error_controller import handle_errors
from src.main.factories.calculator4_factory import calculator4_factory
from src.main.factories.calculator3_factory import calculator3_factory
from src.main.factories.calculator1_factory import calculator1_factory
from src.main.factories.calculator2_factory import calculator2_factory

calculators_route = Blueprint("calc_routes", __name__)


@calculators_route.route("/calculator/1", methods=["POST"])
def calculator_1():
    """
    This method is responsible for calculating the result of the calculator 1.
    :param request: The request with the number to be calculated.
    :return: The result of the calculation.
    """
    try:
        calc = calculator1_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calculators_route.route("/calculator/2", methods=["POST"])
def calculator_2():
    """
    This method is responsible for calculating the result of the calculator 2.
    :param request: The request with the numbers to be calculated.
    :return: The result of the calculation.
    """
    try:
        calc = calculator2_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calculators_route.route("/calculator/3", methods=["POST"])
def calculator_3():
    """
    This method is responsible for calculating the result of the calculator 3.
    :param request: The request with the numbers to be calculated.
    :return: The result of the calculation.
    """
    try:
        calc = calculator3_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]


@calculators_route.route("/calculator/4", methods=["POST"])
def calculator_4():
    """
    This method is responsible for calculating the result of the calculator 4.
    :param request: The request with the numbers to be calculated.
    :return: The result of the calculation.
    """
    try:
        calc = calculator4_factory()
        response = calc.calculate(request)
        return jsonify(response), 200
    except Exception as exception:
        error_response = handle_errors(exception)
        return jsonify(error_response["body"]), error_response["status_code"]
