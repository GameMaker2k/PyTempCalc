#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-

'''
    This program is free software; you can redistribute it and/or modify
    it under the terms of the Revised BSD License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    Revised BSD License for more details.

    Copyright 2016-2019 Game Maker 2k - https://github.com/GameMaker2k
    Copyright 2016-2019 Joshua Przyborowski - https://github.com/JoshuaPrzyborowski

    $FileInfo: pytempcalc.py - Last Update: 1/29/2019 Ver. 0.4.0 RC 1 - Author: joshuatp $
'''

# http://www.nws.noaa.gov/om/winter/windchill.shtml
# http://www.wpc.ncep.noaa.gov/html/windchill.shtml
# http://www.wpc.ncep.noaa.gov/html/dewrh.shtml
# http://www.wpc.ncep.noaa.gov/html/heatindex.shtml

import math;

__program_name__ = "PyTempCalc";
__project__ = __program_name__;
__project_url__ = "https://gist.github.com/JoshuaPrzyborowski";
__version_info__ = (0, 4, 0, "RC 1", 1);
__version_date_info__ = (2019, 1, 29, "RC 1", 1);
__version_date__ = str(__version_date_info__[0])+"."+str(__version_date_info__[1]).zfill(2)+"."+str(__version_date_info__[2]).zfill(2);
if(__version_info__[4]!=None):
 __version_date_plusrc__ = __version_date__+"-"+str(__version_date_info__[4]);
if(__version_info__[4]==None):
 __version_date_plusrc__ = __version_date__;
if(__version_info__[3]!=None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2])+" "+str(__version_info__[3]);
if(__version_info__[3]==None):
 __version__ = str(__version_info__[0])+"."+str(__version_info__[1])+"."+str(__version_info__[2]);

def RoundToInt(IntNum):
 return int(round(IntNum));

def ConvertTempUnits(Temperature, InTempUnit = "Fahrenheit", OutTempUnit = "Celsius"):
 InTempUnit = InTempUnit.capitalize();
 OutTempUnit = OutTempUnit.capitalize();
 retval = {};
 if(InTempUnit != "Fahrenheit" and InTempUnit != "Celsius"):
  return False;
 if(OutTempUnit != "Fahrenheit" and OutTempUnit != "Celsius"):
  return False;
 if(InTempUnit == "Fahrenheit" and OutTempUnit == "Celsius"):
  # retvaltmp = float(5.0 / 9.0) * (float(Temperature) - 32.0);
  retvaltmp = float(((float(Temperature) - 32) * 5) / 9);
  retval.update({
  'Fahrenheit': "{:0.2f}".format(float(Temperature)), 
  'Celsius': "{:0.2f}".format(float(retvaltmp)), 
  'Rankine': "{:0.2f}".format(float(Temperature) + float(273.15)), 
  'Kelvin': "{:0.2f}".format(float(retvaltmp) + float(273.15)), 
  'Delisle': "{:0.2f}".format(((float(Temperature) - 212) * 5) / 6), 
  'Newton': "{:0.2f}".format(((float(Temperature) - 32) * 11) / 60), 
  'Reaumur': "{:0.2f}".format(((float(Temperature) - 32) * 4) / 9), 
  'Romer': "{:0.2f}".format((((float(Temperature) - 32) * 7) / 24) + 7.5), 
  'FahrenheitFull': float(Temperature), 
  'CelsiusFull': float(retvaltmp), 
  'RankineFull': float(Temperature) + float(273.15), 
  'KelvinFull': float(retvaltmp) + float(273.15), 
  'DelisleFull': float(((float(Temperature) - 212) * 5) / 6), 
  'NewtonFull': float(((float(Temperature) - 32) * 11) / 60), 
  'ReaumurFull': float(((float(Temperature) - 32) * 4) / 9), 
  'RomerFull': float((((float(Temperature) - 32) * 7) / 24) + 7.5), 
  'FahrenheitRounded': RoundToInt(float(Temperature)), 
  'CelsiusRounded': RoundToInt(float(retvaltmp)), 
  'RankineRounded': RoundToInt(float(Temperature) + float(273.15)), 
  'KelvinRounded': RoundToInt(float(retvaltmp) + float(273.15)), 
  'DelisleRounded': RoundToInt(float(((float(Temperature) - 212) * 5) / 6)), 
  'NewtonRounded': RoundToInt(float(((float(Temperature) - 32) * 11) / 60)), 
  'ReaumurRounded': RoundToInt(float(((float(Temperature) - 32) * 4) / 9)), 
  'RomerRounded': RoundToInt(float((((float(Temperature) - 32) * 7) / 24) + 7.5))
  });
 elif(InTempUnit == "Celsius" and OutTempUnit == "Fahrenheit"):
  # retvaltmp = float(5.0 * 9.0) / (float(Temperature) - 32.0);
  retvaltmp = float(((float(Temperature) * 9) / 5) + 32);
  retval.update({
  'Fahrenheit': "{:0.2f}".format(float(retvaltmp)), 
  'Celsius': "{:0.2f}".format(float(Temperature)), 
  'Rankine': "{:0.2f}".format(float(retvaltmp) + float(273.15)), 
  'Kelvin': "{:0.2f}".format(float(Temperature) + float(273.15)), 
  'Delisle': "{:0.2f}".format(((float(Temperature) - 100) * 3) / 2), 
  'Newton': "{:0.2f}".format((float(Temperature) * 3) / 2), 
  'Reaumur': "{:0.2f}".format((float(Temperature) * 4) / 5), 
  'Romer': "{:0.2f}".format(float(((float(Temperature) * 21) / 40) + 7.5)), 
  'FahrenheitFull': float(retvaltmp), 
  'CelsiusFull': float(Temperature), 
  'RankineFull': float(retvaltmp) + float(273.15), 
  'KelvinFull': float(Temperature) + float(273.15), 
  'DelisleFull': float(((float(Temperature) - 100) * 3) / 2), 
  'NewtonFull': float((float(Temperature) * 3) / 2), 
  'ReaumurFull': float((float(Temperature) * 4) / 5), 
  'RomerFull': float(((float(Temperature) * 21) / 40) + 7.5), 
  'FahrenheitRounded': RoundToInt(float(retvaltmp)), 
  'CelsiusRounded': RoundToInt(float(Temperature)), 
  'RankineRounded': RoundToInt(float(retvaltmp) + float(273.15)), 
  'KelvinRounded': RoundToInt(float(Temperature) + float(273.15)), 
  'DelisleRounded': RoundToInt(float(((float(Temperature) - 100) * 3) / 2)), 
  'NewtonRounded': RoundToInt(float((float(Temperature) * 3) / 2)), 
  'ReaumurRounded': RoundToInt(float((float(Temperature) * 4) / 5)), 
  'RomerRounded': RoundToInt(float(((float(Temperature) * 21) / 40) + 7.5))
  });
 else:
  return False;
 return retval;

def ConvertTempUnitsFromFahrenheitToCelsius(Temperature):
 return ConvertTempUnits(Temperature, "Fahrenheit", "Celsius");

def ConvertTempUnitsFromCelsiusToFahrenheit(Temperature):
 return ConvertTempUnits(Temperature, "Celsius", "Fahrenheit");

def ConvertWindUnits(WindSpeed, InWindUnit = "MPH", OutWindUnit = "KMH"):
 InWindUnit = InWindUnit.upper();
 OutWindUnit = OutWindUnit.upper();
 retval = {};
 if(InWindUnit != "MPH" and InWindUnit != "KMH"):
  return False;
 if(OutWindUnit != "MPH" and OutWindUnit != "KMH"):
  return False;
 if(InWindUnit == "MPH" and OutWindUnit == "KMH"):
  retvaltmp = float(float(WindSpeed) * 1.609344);
  retval.update({
  'MPH': "{:0.2f}".format(float(WindSpeed)), 
  'KMH': "{:0.2f}".format(float(retvaltmp)), 
  'MPHFull': float(WindSpeed), 
  'KMHFull': float(retvaltmp), 
  'MPHRounded': RoundToInt(float(WindSpeed)), 
  'KMHRounded': RoundToInt(float(retvaltmp))
  });
 elif(InWindUnit == "KMH" and OutWindUnit == "MPH"):
  retvaltmp = float(float(WindSpeed) / 1.609344);
  retval.update({
  'MPH': "{:0.2f}".format(float(retvaltmp)), 
  'KMH': "{:0.2f}".format(float(WindSpeed)), 
  'MPHFull': float(retvaltmp), 
  'KMHFull': float(WindSpeed), 
  'MPHRounded': RoundToInt(float(retvaltmp)), 
  'KMHRounded': RoundToInt(float(WindSpeed))
  });
 else:
  return False;
 return retval;

def ConvertWindUnitsFromMPHToKMH(Temperature):
 return ConvertWindUnits(WindSpeed, "MPH", "KMH");

def ConvertWindUnitsFromKMHToMPH(Temperature):
 return ConvertWindUnits(WindSpeed, "KMH", "MPH");

def WindChill(Temperature, WindSpeed, TempUnit = "Fahrenheit", WindUnit = "MPH"):
 TempUnit = TempUnit.capitalize();
 WindUnit = WindUnit.upper();
 windchillret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(WindUnit != "MPH" and WindUnit != "KMH"):
  return False;
 if(TempUnit == "Fahrenheit" and WindUnit == "MPH"):
  windchill = float(35.74 + 0.6215 * float(Temperature) - 35.75 * math.pow(float(WindSpeed), 0.16) + 0.4275 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Fahrenheit': "{:0.2f}".format(float(windchill)), 
  'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull'])), 
  'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RankineFull'])), 
  'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull'])), 
  'Delisle': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['DelisleFull'])), 
  'Newton': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['NewtonFull'])), 
  'Reaumur': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['ReaumurFull'])), 
  'Romer': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RomerFull'])), 
  'FahrenheitFull': float(windchill), 
  'CelsiusFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RankineFull']), 
  'KelvinFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull']), 
  'DelisleFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['DelisleFull']), 
  'NewtonFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['NewtonFull']), 
  'ReaumurFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['ReaumurFull']), 
  'RomerFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RomerFull']), 
  'FahrenheitRounded': RoundToInt(float(windchill)), 
  'CelsiusRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RankineFull']), 
  'KelvinRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull']), 
  'DelisleRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['DelisleFull']), 
  'NewtonRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['NewtonFull']), 
  'ReaumurRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['ReaumurFull']), 
  'RomerRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RomerFull'])
  });
 if(TempUnit == "Fahrenheit" and WindUnit == "KMH"):
  WindSpeed = 0.621371 * float(WindSpeed);
  windchill = float(35.74 + 0.6215 * float(Temperature) - 35.75 * math.pow(float(WindSpeed), 0.16) + 0.4275 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Fahrenheit': "{:0.2f}".format(float(windchill)), 
  'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull'])), 
  'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RankineFull'])), 
  'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull'])), 
  'Delisle': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['DelisleFull'])), 
  'Newton': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['NewtonFull'])), 
  'Reaumur': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['ReaumurFull'])), 
  'Romer': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RomerFull'])), 
  'FahrenheitFull': float(windchill), 
  'CelsiusFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RankineFull']), 
  'KelvinFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull']), 
  'DelisleFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['DelisleFull']), 
  'NewtonFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['NewtonFull']), 
  'ReaumurFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['ReaumurFull']), 
  'RomerFull': float(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RomerFull']), 
  'FahrenheitRounded': RoundToInt(float(windchill)), 
  'CelsiusRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['CelsiusFull']), 
  'RankineRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RankineFull']), 
  'KelvinRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['KelvinFull']), 
  'DelisleRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['DelisleFull']), 
  'NewtonRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['NewtonFull']), 
  'ReaumurRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['ReaumurFull']), 
  'RomerRounded': RoundToInt(ConvertTempUnits(float(windchill), "Fahrenheit", "Celsius")['RomerFull'])
  });
 if(TempUnit == "Celsius" and WindUnit == "KMH"):
  windchill = float(13.12 + 0.6215 * float(Temperature) - 11.37 * math.pow(float(WindSpeed), 0.16) + 0.3965 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Celsius': "{:0.2f}".format(float(windchill)), 
  'Fahrenheit': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull'])), 
  'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull'])), 
  'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['KelvinFull'])), 
  'Delisle': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['DelisleFull'])), 
  'Newton': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['NewtonFull'])), 
  'Reaumur': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['ReaumurFull'])), 
  'Romer': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RomerFull'])), 
  'CelsiusFull': float(windchill), 
  'FahrenheitFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull']), 
  'RankineFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull']), 
  'KelvinFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['KelvinFull']), 
  'DelisleFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['DelisleFull']), 
  'NewtonFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['NewtonFull']), 
  'ReaumurFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['ReaumurFull']), 
  'RomerFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RomerFull']), 
  'CelsiusRounded': RoundToInt(float(windchill)), 
  'FahrenheitRounded': RoundToInt(ConvertTempUnits(float(windchill)), "Celsius", "Fahrenheit")['FahrenheitFull'], 
  'RankineRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull']), 
  'KelvinRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['KelvinFull']), 
  'DelisleRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['DelisleFull']), 
  'NewtonRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['NewtonFull']), 
  'ReaumurRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['ReaumurFull']), 
  'RomerRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RomerFull'])
  });
 if(TempUnit == "Celsius" and WindUnit == "MPH"):
  WindSpeed = 1.609344 * float(WindSpeed);
  windchill = float(13.12 + 0.6215 * float(Temperature) - 11.37 * math.pow(float(WindSpeed), 0.16) + 0.3965 * float(Temperature) * math.pow(float(WindSpeed), 0.16));
  windchillret.update({
  'Celsius': "{:0.2f}".format(float(windchill)), 
  'Fahrenheit': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull'])), 
  'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull'])), 
  'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['KelvinFull'])), 
  'Delisle': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['DelisleFull'])), 
  'Newton': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['NewtonFull'])), 
  'Reaumur': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['ReaumurFull'])), 
  'Romer': "{:0.2f}".format(float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RomerFull'])), 
  'CelsiusFull': float(windchill), 
  'FahrenheitFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull']), 
  'RankineFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull']), 
  'KelvinFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['KelvinFull']), 
  'DelisleFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['DelisleFull']), 
  'NewtonFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['NewtonFull']), 
  'ReaumurFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['ReaumurFull']), 
  'RomerFull': float(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RomerFull']), 
  'CelsiusRounded': RoundToInt(float(windchill)), 
  'FahrenheitRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['FahrenheitFull']), 
  'RankineRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RankineFull']), 
  'KelvinRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['KelvinFull']), 
  'DelisleRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['DelisleFull']), 
  'NewtonRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['NewtonFull']), 
  'ReaumurRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['ReaumurFull']), 
  'RomerRounded': RoundToInt(ConvertTempUnits(float(windchill), "Celsius", "Fahrenheit")['RomerFull'])
  });
 return windchillret;

def WindChillFahrenheitMPH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Fahrenheit", "MPH");

def WindChillFahrenheitKMH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Fahrenheit", "KMH");

def WindChillCelsiusKMH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Celsius", "KMH");

def WindChillCelsiusMPH(Temperature, WindSpeed):
 return WindChill(Temperature, WindSpeed, "Celsius", "MPH");

def WindChillGenXML(TempUnit = "Fahrenheit", WindUnit = "MPH", OutputFile = "-"):
 TempUnit = TempUnit.capitalize();
 WindUnit = WindUnit.upper();
 mintemp = -45;
 maxtemp = 40;
 tempstart = 40;
 minwind = 5;
 maxwind = 60;
 windstart = 5;
 windchillout = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE noaawcc [\n<!ELEMENT noaawcc (wcc)*>\n<!ELEMENT wcc EMPTY>\n<!ATTLIST wcc windspeedmph CDATA #REQUIRED>\n<!ATTLIST wcc windspeedkhm CDATA #REQUIRED>\n<!ATTLIST wcc temperaturef CDATA #IMPLIED>\n<!ATTLIST wcc temperaturec CDATA #IMPLIED>\n<!ATTLIST wcc temperaturer CDATA #IMPLIED>\n<!ATTLIST wcc temperaturek CDATA #IMPLIED>\n<!ATTLIST wcc temperatured CDATA #IMPLIED>\n<!ATTLIST wcc temperaturen CDATA #IMPLIED>\n<!ATTLIST wcc temperaturere CDATA #IMPLIED>\n<!ATTLIST wcc temperaturero CDATA #IMPLIED>\n<!ATTLIST wcc windchillf CDATA #IMPLIED>\n<!ATTLIST wcc windchillc CDATA #IMPLIED>\n<!ATTLIST wcc windchillr CDATA #IMPLIED>\n<!ATTLIST wcc windchillk CDATA #IMPLIED>\n<!ATTLIST wcc windchilld CDATA #IMPLIED>\n<!ATTLIST wcc windchilln CDATA #IMPLIED>\n<!ATTLIST wcc windchillre CDATA #IMPLIED>\n<!ATTLIST wcc windchillro CDATA #IMPLIED>\n<!ATTLIST wcc frostbitelevel CDATA #IMPLIED>\n<!ATTLIST wcc frostbitemin CDATA #IMPLIED>\n]>\n<noaawcc>\n";
 while(windstart <= maxwind):
  tempstart = 40;
  while(tempstart >= mintemp):
   getwcval = WindChill(tempstart, windstart, TempUnit, WindUnit);
   if(TempUnit == "Fahrenheit"):
    gettuval = ConvertTempUnits(tempstart, "Fahrenheit", "Celsius");
   if(TempUnit == "Celsius"):
    gettuval = ConvertTempUnits(tempstart, "Celsius", "Fahrenheit");
   if(WindUnit == "MPH"):
    getwuval = ConvertWindUnits(tempstart, "MPH", "KMH");
   if(WindUnit == "KMH"):
    getwuval = ConvertWindUnits(tempstart, "KMH", "MPH");
    tempstart = getwuval['MPHRounded'];
   if((windstart == 5 and tempstart <= 40 and tempstart >= -5) or 
      (windstart == 10 and tempstart <= 40 and tempstart >= 0) or 
      (windstart == 15 and tempstart <= 40 and tempstart >= 5) or 
      (windstart == 20 and tempstart <= 40 and tempstart >= 5) or 
      (windstart == 25 and tempstart <= 40 and tempstart >= 5) or 
      (windstart == 30 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 35 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 40 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 45 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 50 and tempstart <= 40 and tempstart >= 10) or 
      (windstart == 55 and tempstart <= 40 and tempstart >= 15) or 
      (windstart == 60 and tempstart <= 40 and tempstart >= 15)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" windchilld=\""+str(getwcval['DelisleRounded'])+"\" windchilln=\""+str(getwcval['NewtonRounded'])+"\" windchillre=\""+str(getwcval['ReaumurRounded'])+"\" windchillro=\""+str(getwcval['RomerRounded'])+"\" frostbitelevel=\"0\" frostbitemin=\"-1\" />\n";
   if((windstart == 5 and tempstart <= -10 and tempstart >= -35) or 
      (windstart == 10 and tempstart <= -5 and tempstart >= -20) or 
      (windstart == 15 and tempstart <= 0 and tempstart >= -15) or 
      (windstart == 20 and tempstart <= 0 and tempstart >= -10) or 
      (windstart == 25 and tempstart <= 0 and tempstart >= -5) or 
      (windstart == 30 and tempstart <= 5 and tempstart >= -5) or 
      (windstart == 35 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 40 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 45 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 50 and tempstart <= 5 and tempstart >= 0) or 
      (windstart == 55 and tempstart <= 10 and tempstart >= 5) or 
      (windstart == 60 and tempstart <= 10 and tempstart >= 5)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" windchilld=\""+str(getwcval['DelisleRounded'])+"\" windchilln=\""+str(getwcval['NewtonRounded'])+"\" windchillre=\""+str(getwcval['ReaumurRounded'])+"\" windchillro=\""+str(getwcval['RomerRounded'])+"\" frostbitelevel=\"1\" frostbitemin=\"30\" />\n";
   if((windstart == 5 and tempstart <= -40 and tempstart >= -45) or 
      (windstart == 10 and tempstart <= -25 and tempstart >= -45) or 
      (windstart == 15 and tempstart <= -20 and tempstart >= -35) or 
      (windstart == 20 and tempstart <= -15 and tempstart >= -30) or 
      (windstart == 25 and tempstart <= -10 and tempstart >= -25) or 
      (windstart == 30 and tempstart <= -10 and tempstart >= -20) or 
      (windstart == 35 and tempstart <= -5 and tempstart >= -15) or 
      (windstart == 40 and tempstart <= -5 and tempstart >= -15) or 
      (windstart == 45 and tempstart <= -5 and tempstart >= -10) or 
      (windstart == 50 and tempstart <= -5 and tempstart >= -10) or 
      (windstart == 55 and tempstart <= 0 and tempstart >= -10) or 
      (windstart == 60 and tempstart <= 0 and tempstart >= 0)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" windchilld=\""+str(getwcval['DelisleRounded'])+"\" windchilln=\""+str(getwcval['NewtonRounded'])+"\" windchillre=\""+str(getwcval['ReaumurRounded'])+"\" windchillro=\""+str(getwcval['RomerRounded'])+"\" frostbitelevel=\"2\" frostbitemin=\"10\" />\n";
   if((windstart == 15 and tempstart <= -40 and tempstart >= -45) or 
      (windstart == 20 and tempstart <= -35 and tempstart >= -45) or 
      (windstart == 25 and tempstart <= -30 and tempstart >= -45) or 
      (windstart == 30 and tempstart <= -25 and tempstart >= -45) or 
      (windstart == 35 and tempstart <= -20 and tempstart >= -45) or 
      (windstart == 40 and tempstart <= -20 and tempstart >= -45) or 
      (windstart == 45 and tempstart <= -15 and tempstart >= -45) or 
      (windstart == 50 and tempstart <= -15 and tempstart >= -45) or 
      (windstart == 55 and tempstart <= -15 and tempstart >= -45) or 
      (windstart == 60 and tempstart <= -10 and tempstart >= -45)):
    windchillout = windchillout + " <wcc windspeedmph=\""+str(getwuval['MPHRounded'])+"\" windspeedkhm=\""+str(getwuval['KMHRounded'])+"\" temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" windchillf=\""+str(getwcval['FahrenheitRounded'])+"\" windchillc=\""+str(getwcval['CelsiusRounded'])+"\" windchillr=\""+str(getwcval['RankineRounded'])+"\" windchillk=\""+str(getwcval['KelvinRounded'])+"\" windchilld=\""+str(getwcval['DelisleRounded'])+"\" windchilln=\""+str(getwcval['NewtonRounded'])+"\" windchillre=\""+str(getwcval['ReaumurRounded'])+"\" windchillro=\""+str(getwcval['RomerRounded'])+"\" frostbitelevel=\"3\" frostbitemin=\"5\" />\n";
   tempstart = tempstart - 5;
  windstart = windstart + 5;
 windchillout = windchillout + "</noaawcc>\n";
 if(OutputFile!="-"):
  wcof = open(OutputFile, 'w');
  wcof.write(windchillout);
  wcof.close();
 return windchillout;

def WindChillGenXMLFahrenheitMPH(Temperature, WindSpeed):
 return WindChillGenXML("Fahrenheit", "MPH", OutputFile);

def WindChillGenXMLFahrenheitKMH(Temperature, WindSpeed):
 return WindChillGenXML("Fahrenheit", "KMH", OutputFile);

def WindChillGenXMLCelsiusKMH(Temperature, WindSpeed):
 return WindChillGenXML("Celsius", "KMH", OutputFile);

def WindChillGenXMLCelsiusMPH(Temperature, WindSpeed):
 return WindChillGenXML("Celsius", "MPH", OutputFile);

def HeatIndexByDewPoint(Temperature, DewPointTemp, TempUnit = "Fahrenheit"):
 TempUnit = TempUnit.capitalize();
 heatindexret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(TempUnit == "Celsius"):
  Temperature = ConvertTempUnits(float(Temperature), "Celsius", "Fahrenheit")['FahrenheitFull'];
  DewPointTemp = ConvertTempUnits(float(DewPointTemp), "Celsius", "Fahrenheit")['FahrenheitFull'];
  TempUnit = "Fahrenheit";
 if(TempUnit == "Fahrenheit"):
  tc2 = ConvertTempUnits(float(Temperature), "Fahrenheit", "Celsius")['CelsiusFull'];
  tdc2 = ConvertTempUnits(float(DewPointTemp), "Fahrenheit", "Celsius")['CelsiusFull'];
  vaporpressure = 6.11 * (math.pow(10, 7.5 * (tdc2 / (237.7 + tdc2))));
  satvaporpressure = 6.11 * (math.pow(10, 7.5 * (tc2 / (237.7 + tc2))));
  RHumidity2 = RoundToInt(100.0 * (vaporpressure / satvaporpressure));
  hitemp = 61.0 + ((Temperature - 68.0) * 1.2) + (RHumidity2 * 0.094);
  fptemp = float(Temperature);
  hifinal = 0.5 * (fptemp + hitemp);
  if(hifinal > 79.0):
   hi = -42.379 + 2.04901523 * float(Temperature) + 10.14333127 * RHumidity2 - 0.22475541 * float(Temperature) * RHumidity2 - 6.83783 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) - 5.481717 * (math.pow(10, -2)) * (math.pow(RHumidity2, 2)) + 1.22874 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) * RHumidity2 + 8.5282 * (math.pow(10, -4)) * float(Temperature) * (math.pow(RHumidity2, 2)) - 1.99 * (math.pow(10, -6)) * (math.pow(float(Temperature), 2)) * (math.pow(RHumidity2,2));
   if((RHumidity2 <= 13.0) and (Temperature >= 80.0) and (Temperature <= 112.0)):
    adj1 = (13.0 - RHumidity2) / 4.0;
    adj2 = math.sqrt((17.0 - abs(Temperature - 95.0)) / 17.0);
    adj = adj1 * adj2;
    hi = hi - adj;
   elif((RHumidity2 > 85.0) and (Temperature >= 80.0) and (Temperature <= 87.0)):
    adj1 = (RHumidity2 - 85.0) / 10.0;
    adj2 = (87.0 - float(Temperature)) / 5.0;
    adj = adj1 * adj2;
    hi = hi + adj;
  else:
   hi = hifinal;
 heatindexret.update({
 'Fahrenheit': "{:0.2f}".format(float(hi)), 
 'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull'])), 
 'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RankineFull'])), 
 'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull'])), 
 'Delisle': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['DelisleFull'])), 
 'Newton': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['NewtonFull'])), 
 'Reaumur': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['ReaumurFull'])), 
 'Romer': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RomerFull'])), 
 'FahrenheitFull': float(hi), 
 'CelsiusFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RankineFull']), 
 'KelvinFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull']), 
 'DelisleFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['DelisleFull']), 
 'NewtonFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['NewtonFull']), 
 'ReaumurFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['ReaumurFull']), 
 'RomerFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RomerFull']), 
 'FahrenheitRounded': RoundToInt(float(hi)), 
 'CelsiusRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RankineFull']), 
 'KelvinRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull']), 
 'DelisleRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['DelisleFull']), 
 'NewtonRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['NewtonFull']), 
 'ReaumurRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['ReaumurFull']), 
 'RomerRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RomerFull'])
 });
 return heatindexret;

def HeatIndexByDewPointFahrenheit(Temperature, DewPointTemp):
 return HeatIndexByDewPoint(Temperature, DewPointTemp, "Fahrenheit");

def HeatIndexByDewPointCelsius(Temperature, DewPointTemp):
 return HeatIndexByDewPoint(Temperature, DewPointTemp, "Celsius");

def HeatIndexByRelativeHumidity(Temperature, Humidity, TempUnit = "Fahrenheit"):
 TempUnit = TempUnit.capitalize();
 heatindexret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(TempUnit == "Celsius"):
  Temperature = ConvertTempUnits(float(Temperature), "Celsius", "Fahrenheit")['FahrenheitFull'];
  TempUnit = "Fahrenheit";
 if(TempUnit == "Fahrenheit"):
  hitemp = 61.0 + ((float(Temperature) - 68.0) * 1.2) + (float(Humidity) * 0.094);
  fptemp = float(float(Temperature));
  hifinal = 0.5 * (fptemp + hitemp);
  if(hifinal > 79.0):
   hi = -42.379 + 2.04901523 * float(Temperature) + 10.14333127 * float(Humidity) - 0.22475541 * float(Temperature) * float(Humidity) - 6.83783 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) - 5.481717 * (math.pow(10, -2)) * (math.pow(float(Humidity), 2))+1.22874 * (math.pow(10, -3)) * (math.pow(float(Temperature), 2)) * float(Humidity)+8.5282 * (math.pow(10, -4)) * float(Temperature) * (math.pow(float(Humidity), 2)) - 1.99 * (math.pow(10, -6)) * (math.pow(float(Temperature), 2)) * (math.pow(float(Humidity),2));
   if((float(Humidity) <= 13) and (float(Temperature) >= 80.0) and (float(Temperature) <= 112.0)):
    adj1 = (13.0 - float(Humidity)) / 4.0;
    adj2 = math.sqrt((17.0 - abs(float(Temperature) - 95.0)) / 17.0);
    adj = adj1 * adj2;
    hi = hi - adj;
   elif ((float(Humidity) > 85.0) and (float(Temperature) >= 80.0) and (float(Temperature) <= 87.0)):
    adj1 = (float(Humidity) - 85.0) / 10.0;
    adj2 = (87.0 - float(Temperature)) / 5.0;
    adj = adj1 * adj2;
    hi = hi + adj;
  else:
   hi = hifinal;
 heatindexret.update({
 'Fahrenheit': "{:0.2f}".format(float(hi)), 
 'Celsius': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull'])), 
 'Rankine': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RankineFull'])), 
 'Kelvin': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull'])), 
 'Delisle': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['DelisleFull'])), 
 'Newton': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['NewtonFull'])), 
 'Reaumur': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['ReaumurFull'])), 
 'Romer': "{:0.2f}".format(float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RomerFull'])), 
 'FahrenheitFull': float(hi), 
 'CelsiusFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RankineFull']), 
 'KelvinFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull']),
 'DelisleFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['DelisleFull']), 
 'NewtonFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['NewtonFull']), 
 'ReaumurFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['ReaumurFull']), 
 'RomerFull': float(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RomerFull']),  
 'FahrenheitRounded': RoundToInt(float(hi)), 
 'CelsiusRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['CelsiusFull']), 
 'RankineRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RankineFull']), 
 'KelvinRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['KelvinFull']), 
 'DelisleRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['DelisleFull']), 
 'NewtonRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['NewtonFull']), 
 'ReaumurRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['ReaumurFull']), 
 'RomerRounded': RoundToInt(ConvertTempUnits(float(hi), "Fahrenheit", "Celsius")['RomerFull'])
 });
 return heatindexret;

def HeatIndexByRelativeHumidityFahrenheit(Temperature, Humidity):
 return HeatIndexByRelativeHumidity(Temperature, Humidity, "Fahrenheit");

def HeatIndexByRelativeHumidityCelsius(Temperature, Humidity):
 return HeatIndexByRelativeHumidity(Temperature, Humidity, "Celsius");

def HeatIndexByRelativeHumidityGenXML(TempUnit = "Fahrenheit", OutputFile = "-"):
 TempUnit = TempUnit.capitalize();
 mintemp = 80;
 maxtemp = 110;
 tempstart = 80;
 minhumid = 40;
 maxhumid = 100;
 humidstart = 40;
 humidityout = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!DOCTYPE noaahic [\n<!ELEMENT noaahic (hic)*>\n<!ELEMENT hic EMPTY>\n<!ATTLIST hic temperaturef CDATA #IMPLIED>\n<!ATTLIST hic temperaturec CDATA #IMPLIED>\n<!ATTLIST hic temperaturer CDATA #IMPLIED>\n<!ATTLIST hic temperaturek CDATA #IMPLIED>\n<!ATTLIST hic temperatured CDATA #IMPLIED>\n<!ATTLIST hic temperaturen CDATA #IMPLIED>\n<!ATTLIST hic temperaturere CDATA #IMPLIED>\n<!ATTLIST hic temperaturero CDATA #IMPLIED>\n<!ATTLIST hic humidity CDATA #IMPLIED>\n<!ATTLIST hic humidityf CDATA #IMPLIED>\n<!ATTLIST hic humidityc CDATA #IMPLIED>\n<!ATTLIST hic humidityr CDATA #IMPLIED>\n<!ATTLIST hic humidityk CDATA #IMPLIED>\n<!ATTLIST hic humidityd CDATA #IMPLIED>\n<!ATTLIST hic humidityn CDATA #IMPLIED>\n<!ATTLIST hic humidityre CDATA #IMPLIED>\n<!ATTLIST hic humidityro CDATA #IMPLIED>\n<!ATTLIST hic heatlevelnum CDATA #IMPLIED>\n<!ATTLIST hic heatlevel CDATA #IMPLIED>\n]>\n<noaahic>\n";
 while(humidstart <= maxhumid):
  tempstart = 80;
  while(tempstart <= maxtemp):
   getwcval = HeatIndexByRelativeHumidity(tempstart, humidstart, TempUnit);
   if(TempUnit == "Fahrenheit"):
    gettuval = ConvertTempUnits(tempstart, "Fahrenheit", "Celsius");
   if(TempUnit == "Celsius"):
    gettuval = ConvertTempUnits(tempstart, "Celsius", "Fahrenheit");
   if((humidstart == 40 and tempstart >= 80 and tempstart <= 88) or 
      (humidstart == 45 and tempstart >= 80 and tempstart <= 88) or 
      (humidstart == 50 and tempstart >= 80 and tempstart <= 86) or 
      (humidstart == 55 and tempstart >= 80 and tempstart <= 86) or 
      (humidstart == 60 and tempstart >= 80 and tempstart <= 84) or 
      (humidstart == 65 and tempstart >= 80 and tempstart <= 84) or 
      (humidstart == 70 and tempstart >= 80 and tempstart <= 82) or 
      (humidstart == 75 and tempstart >= 80 and tempstart <= 82) or 
      (humidstart == 80 and tempstart >= 80 and tempstart <= 82) or 
      (humidstart == 85 and tempstart >= 80 and tempstart <= 82) or 
      (humidstart == 90 and tempstart >= 80 and tempstart <= 80) or 
      (humidstart == 95 and tempstart >= 80 and tempstart <= 80) or 
      (humidstart == 100 and tempstart >= 80 and tempstart <= 80)):
    humidityout = humidityout + " <hic temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" humidity=\""+str(humidstart)+"\" humidityf=\""+str(getwcval['FahrenheitRounded'])+"\" humidityc=\""+str(getwcval['CelsiusRounded'])+"\" humidityr=\""+str(getwcval['RankineRounded'])+"\" humidityk=\""+str(getwcval['KelvinRounded'])+"\" humidityd=\""+str(getwcval['DelisleRounded'])+"\" humidityn=\""+str(getwcval['NewtonRounded'])+"\" humidityre=\""+str(getwcval['ReaumurRounded'])+"\" humidityro=\""+str(getwcval['RomerRounded'])+"\" heatlevelnum=\"0\" heatlevel=\"Caution\" />\n";
   if((humidstart == 40 and tempstart >= 90 and tempstart <= 96) or 
      (humidstart == 45 and tempstart >= 90 and tempstart <= 94) or 
      (humidstart == 50 and tempstart >= 88 and tempstart <= 94) or 
      (humidstart == 55 and tempstart >= 88 and tempstart <= 92) or 
      (humidstart == 60 and tempstart >= 86 and tempstart <= 90) or 
      (humidstart == 65 and tempstart >= 86 and tempstart <= 90) or 
      (humidstart == 70 and tempstart >= 86 and tempstart <= 88) or 
      (humidstart == 75 and tempstart >= 84 and tempstart <= 86) or 
      (humidstart == 80 and tempstart >= 84 and tempstart <= 86) or 
      (humidstart == 85 and tempstart >= 84 and tempstart <= 86) or 
      (humidstart == 90 and tempstart >= 82 and tempstart <= 84) or 
      (humidstart == 95 and tempstart >= 82 and tempstart <= 84) or 
      (humidstart == 100 and tempstart >= 82 and tempstart <= 84)):
    humidityout = humidityout + " <hic temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" humidity=\""+str(humidstart)+"\" humidityf=\""+str(getwcval['FahrenheitRounded'])+"\" humidityc=\""+str(getwcval['CelsiusRounded'])+"\" humidityr=\""+str(getwcval['RankineRounded'])+"\" humidityk=\""+str(getwcval['KelvinRounded'])+"\" humidityd=\""+str(getwcval['DelisleRounded'])+"\" humidityn=\""+str(getwcval['NewtonRounded'])+"\" humidityre=\""+str(getwcval['ReaumurRounded'])+"\" humidityro=\""+str(getwcval['RomerRounded'])+"\" heatlevelnum=\"1\" heatlevel=\"Extreme Caution\" />\n";
   if((humidstart == 40 and tempstart >= 98 and tempstart <= 106) or 
      (humidstart == 45 and tempstart >= 96 and tempstart <= 104) or 
      (humidstart == 50 and tempstart >= 96 and tempstart <= 102) or 
      (humidstart == 55 and tempstart >= 94 and tempstart <= 100) or 
      (humidstart == 60 and tempstart >= 92 and tempstart <= 98) or 
      (humidstart == 65 and tempstart >= 92 and tempstart <= 96) or 
      (humidstart == 70 and tempstart >= 90 and tempstart <= 94) or 
      (humidstart == 75 and tempstart >= 88 and tempstart <= 94) or 
      (humidstart == 80 and tempstart >= 88 and tempstart <= 92) or 
      (humidstart == 85 and tempstart >= 88 and tempstart <= 90) or 
      (humidstart == 90 and tempstart >= 86 and tempstart <= 90) or 
      (humidstart == 95 and tempstart >= 86 and tempstart <= 88) or 
      (humidstart == 100 and tempstart >= 86 and tempstart <= 88)):
    humidityout = humidityout + " <hic temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" humidity=\""+str(humidstart)+"\" humidityf=\""+str(getwcval['FahrenheitRounded'])+"\" humidityc=\""+str(getwcval['CelsiusRounded'])+"\" humidityr=\""+str(getwcval['RankineRounded'])+"\" humidityk=\""+str(getwcval['KelvinRounded'])+"\" humidityd=\""+str(getwcval['DelisleRounded'])+"\" humidityn=\""+str(getwcval['NewtonRounded'])+"\" humidityre=\""+str(getwcval['ReaumurRounded'])+"\" humidityro=\""+str(getwcval['RomerRounded'])+"\" heatlevelnum=\"2\" heatlevel=\"Danger\" />\n";
   if((humidstart == 40 and tempstart >= 108 and tempstart <= 110) or 
      (humidstart == 45 and tempstart >= 106 and tempstart <= 108) or 
      (humidstart == 50 and tempstart >= 104 and tempstart <= 106) or 
      (humidstart == 55 and tempstart >= 102 and tempstart <= 104) or 
      (humidstart == 60 and tempstart >= 100 and tempstart <= 102) or 
      (humidstart == 65 and tempstart >= 98 and tempstart <= 100) or 
      (humidstart == 70 and tempstart >= 96 and tempstart <= 98) or 
      (humidstart == 75 and tempstart >= 96 and tempstart <= 96) or 
      (humidstart == 80 and tempstart >= 94 and tempstart <= 94) or 
      (humidstart == 85 and tempstart >= 92 and tempstart <= 94) or 
      (humidstart == 90 and tempstart >= 92 and tempstart <= 92) or 
      (humidstart == 95 and tempstart >= 90 and tempstart <= 90) or 
      (humidstart == 100 and tempstart >= 90 and tempstart <= 90)):
    humidityout = humidityout + " <hic temperaturef=\""+str(gettuval['FahrenheitRounded'])+"\" temperaturec=\""+str(gettuval['CelsiusRounded'])+"\" temperaturer=\""+str(gettuval['RankineRounded'])+"\" temperaturek=\""+str(gettuval['KelvinRounded'])+"\" temperatured=\""+str(gettuval['DelisleRounded'])+"\" temperaturen=\""+str(gettuval['NewtonRounded'])+"\" temperaturere=\""+str(gettuval['ReaumurRounded'])+"\" temperaturero=\""+str(gettuval['RomerRounded'])+"\" humidity=\""+str(humidstart)+"\" humidityf=\""+str(getwcval['FahrenheitRounded'])+"\" humidityc=\""+str(getwcval['CelsiusRounded'])+"\" humidityr=\""+str(getwcval['RankineRounded'])+"\" humidityk=\""+str(getwcval['KelvinRounded'])+"\" humidityd=\""+str(getwcval['DelisleRounded'])+"\" humidityn=\""+str(getwcval['NewtonRounded'])+"\" humidityre=\""+str(getwcval['ReaumurRounded'])+"\" humidityro=\""+str(getwcval['RomerRounded'])+"\" heatlevelnum=\"3\" heatlevel=\"Extreme Danger\" />\n";
   tempstart = tempstart + 2;
  humidstart = humidstart + 5;
 humidityout = humidityout + "</noaahic>\n";
 if(OutputFile!="-"):
  wcof = open(OutputFile, 'w');
  wcof.write(humidityout);
  wcof.close();
 return humidityout;

def HeatIndexByRelativeHumidityGenXMLFahrenheitMPH(Temperature, WindSpeed):
 return HeatIndexByRelativeHumidityGenXML("Fahrenheit", "MPH", OutputFile);

def HeatIndexByRelativeHumidityGenXMLFahrenheitKMH(Temperature, WindSpeed):
 return HeatIndexByRelativeHumidityGenXML("Fahrenheit", "KMH", OutputFile);

def HeatIndexByRelativeHumidityGenXMLCelsiusKMH(Temperature, WindSpeed):
 return HeatIndexByRelativeHumidityGenXML("Celsius", "KMH", OutputFile);

def HeatIndexByRelativeHumidityGenXMLCelsiusMPH(Temperature, WindSpeed):
 return HeatIndexByRelativeHumidityGenXML("Celsius", "MPH", OutputFile);

def RelativeHumidity(Temperature, DewPointTemp, TempUnit = "Fahrenheit"):
 TempUnit = TempUnit.capitalize();
 relativehumidityret = {};
 if(TempUnit != "Fahrenheit" and TempUnit != "Celsius"):
  return False;
 if(TempUnit == "Celsius"):
  Temperature = ConvertTempUnits(float(Temperature), "Celsius", "Fahrenheit")['FahrenheitFull'];
  DewPointTemp = ConvertTempUnits(float(DewPointTemp), "Celsius", "Fahrenheit")['FahrenheitFull'];
  TempUnit = "Fahrenheit";
 if(TempUnit == "Fahrenheit"):
  a = float(Temperature);
  b = float(DewPointTemp);
  a_c = ConvertTempUnits(float(a), "Fahrenheit", "Celsius")['CelsiusFull'];
  b_c = ConvertTempUnits(float(b), "Fahrenheit", "Celsius")['CelsiusFull'];
  c = 6.11 * math.pow(10, ((7.5 * a_c / (237.7 + a_c))));
  d = 6.11 * math.pow(10, ((7.5 * b_c / (237.7 + b_c))));
  e = (d / c) * 100;
  f = (round(e * 100)) / 100;
  ffull = (e * 100) / 100;
 relativehumidityret.update({
 'RelativeHumidity': "{:0.2f}".format(float(ffull)), 
 'RelativeHumidityRounded': RoundToInt(float(ffull)), 
 'RelativeHumidityFull': float(ffull)
 });
 return relativehumidityret;

def RelativeHumidityFahrenheit(Temperature, DewPointTemp):
 return RelativeHumidity(Temperature, DewPointTemp, "Fahrenheit");

def RelativeHumidityCelsius(Temperature, Humidity):
 return RelativeHumidity(Temperature, DewPointTemp, "Celsius");
