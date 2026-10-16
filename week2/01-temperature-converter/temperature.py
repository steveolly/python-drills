import math


def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * (9 / 5)) + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * (5 / 9)


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return (fahrenheit - 32) * (5 / 9) + 273.15


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    return (kelvin - 273.15) * (9 / 5) + 32


def convert_temperature(value, from_unit, to_unit):

    # Validate the temperature value
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("Temperature must be a number.")

    if not math.isfinite(value):
        raise ValueError("Temperature must be finite.")

    # Validate unit types
    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise ValueError("Units must be strings.")

    from_unit = from_unit.strip().lower()
    to_unit = to_unit.strip().lower()

    # Absolute-zero limits for each unit
    minimums = {
        "celsius": -273.15,
        "fahrenheit": -459.67,
        "kelvin": 0
    }

    # Validate supported units
    if from_unit not in minimums or to_unit not in minimums:
        raise ValueError("Unsupported temperature unit.")

    # Validate absolute zero using the original unit
    if value < minimums[from_unit]:
        raise ValueError("Temperature cannot be below absolute zero.")

    # Return the value if both units are the same
    if from_unit == to_unit:
        return round(value, 2)

    # Available conversion functions
    conversions = {
        ("celsius", "fahrenheit"): celsius_to_fahrenheit,
        ("fahrenheit", "celsius"): fahrenheit_to_celsius,
        ("celsius", "kelvin"): celsius_to_kelvin,
        ("fahrenheit", "kelvin"): fahrenheit_to_kelvin,
        ("kelvin", "celsius"): kelvin_to_celsius,
        ("kelvin", "fahrenheit"): kelvin_to_fahrenheit
    }

    result = conversions[(from_unit, to_unit)](value)

    return round(result, 2)
