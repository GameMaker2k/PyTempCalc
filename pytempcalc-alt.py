#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

"""
This program is free software; you can redistribute it and/or modify
it under the terms of the Revised BSD License.
"""

import math

__version__ = "0.4.0 RC 1"
__version_date__ = "2019.02.09"


def round_to_int(number):
    return int(round(number))


def convert_temp_units(temp, from_unit="Fahrenheit", to_unit="Celsius"):
    temp = float(temp)
    from_unit = from_unit.capitalize()
    to_unit = to_unit.capitalize()
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (temp - 32) * 5 / 9
    elif from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (temp * 9 / 5) + 32
    else:
        return temp


def convert_wind_units(speed, from_unit="MPH", to_unit="KMH"):
    if from_unit == "MPH" and to_unit == "KMH":
        return speed * 1.609344
    elif from_unit == "KMH" and to_unit == "MPH":
        return speed / 1.609344
    else:
        return speed


def wind_chill(
        temp,
        wind_speed,
        temp_unit="Fahrenheit",
        wind_unit="MPH",
        new_wind_chill=True):
    temp = float(temp)
    wind_speed = float(wind_speed)
    if temp_unit == "Celsius":
        temp = convert_temp_units(temp, "Celsius", "Fahrenheit")
    if wind_unit == "KMH":
        wind_speed = convert_wind_units(wind_speed, "KMH", "MPH")

    if new_wind_chill:
        chill = 35.74 + 0.6215 * temp - 35.75 * \
            math.pow(wind_speed, 0.16) + 0.4275 * temp * math.pow(wind_speed, 0.16)
    else:
        chill = 0.0817 * (3.71 * math.sqrt(wind_speed) +
                          5.81 - 0.25 * wind_speed) * (temp - 91.4) + 91.4

    return round_to_int(convert_temp_units(chill, "Fahrenheit", temp_unit))


def generate_windchill_xml(
        temp_unit="Fahrenheit",
        wind_unit="MPH",
        new_wind_chill=True,
        output_file="-"):
    temp_unit = temp_unit.capitalize()
    wind_unit = wind_unit.upper()
    result = '<?xml version="1.0" encoding="UTF-8"?>\n<noaawcc>\n'

    for wind_speed in range(5, 65, 5):
        for temp in range(40, -46, -5):
            wind_chill_value = wind_chill(
                temp, wind_speed, temp_unit, wind_unit, new_wind_chill)
            result += f' <wcc windspeedmph="{wind_speed}" temperature{
                temp_unit.lower()}="{temp}" windchill{
                temp_unit.lower()}="{wind_chill_value}" />\n'

    result += "</noaawcc>\n"

    if output_file != "-":
        with open(output_file, 'w') as file:
            file.write(result)
    return result


def generate_heat_index_xml(temp_unit="Fahrenheit", output_file="-"):
    temp_unit = temp_unit.capitalize()
    result = '<?xml version="1.0" encoding="UTF-8"?>\n<noaahic>\n'

    for humidity in range(40, 105, 5):
        for temp in range(80, 112, 2):
            heat_index_value = heat_index(temp, humidity, temp_unit)
            result += f' <hic temperature{
                temp_unit.lower()}="{temp}" humidity="{humidity}" heatindex{
                temp_unit.lower()}="{heat_index_value}" />\n'

    result += "</noaahic>\n"

    if output_file != "-":
        with open(output_file, 'w') as file:
            file.write(result)
    return result


def heat_index(temp, humidity, temp_unit="Fahrenheit"):
    temp = float(temp)
    if temp_unit == "Celsius":
        temp = convert_temp_units(temp, "Celsius", "Fahrenheit")

    if temp < 80:
        return temp

    heat_index_value = (-42.379 + 2.04901523 * temp + 10.14333127 * humidity
                        - 0.22475541 * temp * humidity - 6.83783e-3 * temp ** 2
                        - 5.481717e-2 * humidity ** 2 + 1.22874e-3 * temp ** 2 * humidity
                        + 8.5282e-4 * temp * humidity ** 2 - 1.99e-6 * temp ** 2 * humidity ** 2)

    return round_to_int(
        convert_temp_units(
            heat_index_value,
            "Fahrenheit",
            temp_unit))


def main():
    generate_windchill_xml()
    generate_heat_index_xml()


if __name__ == "__main__":
    main()
