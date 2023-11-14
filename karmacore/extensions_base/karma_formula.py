from math import fabs, sqrt


def calculate_karma_change_strength(
    karma_user_power: float, desired_amount: float = float("inf")
) -> float:
    """
    How huge is karma change for amount that user has.

    :param desired_amount: optionally limits users karma power to some amount. By default, is as strong as possible.
        Can be negative values, but functions as absolute value.
    :param karma_user_power: users karma.
    :return: karma change.
    :raises ValueError: if users karma level is below zero.
    """
    if karma_user_power <= 0:
        raise ValueError("Users karma level is too low to change others karma")

    karma_change = sqrt(karma_user_power)

    if fabs(desired_amount) <= karma_change:
        return karma_change

    else:
        return fabs(desired_amount)
