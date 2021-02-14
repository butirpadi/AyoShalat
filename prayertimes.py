#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
------------------------ Copyright Block -----------------------

Prayer Times Calculator improved by Sid-Ali TEIR.

Original used :
praytimes.py: Prayer Times Calculator (ver 2.3)
Copyright (C) 2007-2011 PrayTimes.org

Python Code: Saleem Shafi, Hamid Zarrabi-Zadeh
Original js Code: Hamid Zarrabi-Zadeh

License: GNU LGPL v3.0

TERMS OF USE:
* Permission is granted to use this code, with or
* without modification, in any website or application
* provided that credit is given to the original work
* with a link back to PrayTimes.org.

This program is distributed in the hope that it will
be useful, but WITHOUT ANY WARRANTY.

PLEASE DO NOT REMOVE THIS COPYRIGHT BLOCK.

------------------------ Help and Manual ------------------------

User's Manual:
http://praytimes.org/manual

Calculation Formulas:
http://praytimes.org/calculation

Compatibility:
Compatible with Python 2.x and 3.x

------------------------ User Interface -------------------------

* get_times (date, coordinates, timeZone [, dst [, timeFormat]])

* set_method (method)      -- Set calculation method
* adjust (parameters)      -- Adjust calculation parameters
* tune (offsets)           -- Tune times by given offsets

| Format | Description                   | Example |
|--------|-------------------------------|---------|
| 24h    | 24-hour time format           | 16:45   |
| 12h    | 12-hour time format           | 4:45 pm |
| 12hNS  | 12-hour format with no suffix | 4:45    |
| Float  | Floating point number         | 16.75   |

| Method  | Description                                   |
|---------|-----------------------------------------------|
| MWL     | Muslim World League                           |
| ISNA    | Islamic Society of North America              |
| Egypt   | Egyptian General Authority of Survey          |
| Makkah  | Umm al-Qura University                        |
| Karachi | University of Islamic Sciences, Karachi       |
| Tehran  | Institute of Geophysics, University of Tehran |
| Jafari  | Shia Ithna Ashari (Ja`fari)                   |

| Parameter | Values        | Description                   | Sample Value |
|-----------|---------------|-------------------------------|--------------|
| imsak     | degrees       | twilight angle                | 18           |
| minutes   | minutes       | minutes before fajr           | 10 min       |
| fajr      | degrees       | twilight angle                | 15           |
| dhuhr     | minutes       | minutes after mid-day         | 1 min        |
| asr       | method        | asr juristic method *         | Standard     |
| factor    | shadow length | factor for realizing asr      | 1.7          |
| maghrib   | degrees       | twilight angle                | 4            |
| minutes   | minutes       | minutes after maghrib         | 15 min       |
| isha      | degrees       | twilight angle                | 18           |
| minutes   | minutes       | minutes after maghrib         | 90 min       |
| midnight  | method        | midnight method *             | Standard     |
| highLats  | method        | higher latitudes adjustment * | None         |

\* means see the following tables.

###asr methods
| Method   | Description (More Info)                                |
|----------|--------------------------------------------------------|
| Standard | Shafii, Maliki, Jafari and Hanbali (shadow factor = 1) |
| Hanafi   | Hanafi school of tought (shadow factor = 2)            |

###midnight methods
| Method   | Description                          |
|----------|--------------------------------------|
| Standard | The mean time from Sunset to Sunrise |
| Hanafi   | The mean time from Maghrib to Fajr   |

###higher latitudes methods
| Method      | Description (More Info)              |
|-------------|--------------------------------------|
| None        | No adjustments                       |
| NightMiddle | The middle of the night method       |
| OneSeventh  | The 1/7th of the night method        |
| AngleBased  | The angle-based method (recommended) |

------------------------- Sample Usage --------------------------

* Get prayer times from a date
>> PT = PrayTimes('ISNA')
>> times = PT.get_times((2011, 2, 9), (43, -80), -5)
>> times['sunrise']
07:26

* Set calculation method
>> PT.set_method('ISNA')

* Adjust fajr and Isha using different degrees
>> PT.adjust({'fajr': 12, 'isha': 12})

* Tune prayer times setting minutes adjustments
>> PT.tune({'fajr': +10, 'dhuhr': -10, 'asr': -10, 'maghrib': -10, 'isha': +10,
            'midnight': 5, 'sunrise': -2, 'sunset': +9, 'imsak': +15})

* print PT.offset
* print PT.calc_method
* print PT.settings

"""

import math
import re
import datetime


class PrayTimes(object):
    """
    PrayTimes class

    Pray Times, an Islamic project aimed at providing an open-source library for calculating Muslim prayers times.
    This is an improved version PEP8 compliant.

    """

    # Time Names
    time_names = ['imsak', 'fajr', 'sunrise', 'dhuhr', 'asr', 'sunset', 'maghrib', 'isha', 'midnight']

    # Calculation Methods
    methods = {
        'MWL': {
            'name': 'Muslim World League',
            'params': {'fajr': 18, 'isha': 17}},
        'ISNA': {
            'name': 'Islamic Society of North America (ISNA)',
            'params': {'fajr': 15, 'isha': 15}},
        'Egypt': {
            'name': 'Egyptian General Authority of Survey',
            'params': {'fajr': 19.5, 'isha': 17.5}},
        'Makkah': {
            'name': 'Umm Al-Qura University, Makkah',
            'params': {'fajr': 18.5, 'isha': '90 min'}},  # Fajr was 19 degrees before 1430 hijri
        'Karachi': {
            'name': 'University of Islamic Sciences, Karachi',
            'params': {'fajr': 18, 'isha': 18}},
        'Tehran': {
            'name': 'Institute of Geophysics, University of Tehran',
            'params': {'fajr': 17.7, 'isha': 14, 'maghrib': 4.5, 'midnight': 'Jafari'}},
        # Isha is not explicitly specified in this method
        'Jafari': {
            'name': 'Shia Ithna-Ashari, Leva Institute, Qum',
            'params': {'fajr': 16, 'isha': 14, 'maghrib': 4, 'midnight': 'Jafari'}},
        'UOIF': {
            'name': 'Union des Organisations Islamiques de France',
            'params': {'fajr': 12, 'isha': 12}}
    }

    # Default Parameters added in Calculation Methods <METHODS> if not already there
    method_defaults = {
        'maghrib': '0 min', 'midnight': 'Standard'
    }

    # Do not change anything here,
    # Use adjust method instead
    # Add last settings needed to final configuration
    settings = {
        "imsak": '10 min',
        "dhuhr": '0 min',
        "asr": 'Standard',  # Standard or Hanafi
        "highLats": 'NightMiddle'
    }

    offset = {}

    def __init__(self, method="MWL", format_time="24h", **kwargs):

        # Initialize coordinates
        coords = kwargs.get("coords", (0, 0, 0))
        self.lat = coords[0]
        self.lng = coords[1]
        self.elv = coords[2]

        # Initialize timezone
        timezone = kwargs.get("timezone", 0)
        self.timezone = timezone

        # Initialize date
        date = kwargs.get("date", datetime.date.today())
        self.julian_date = self.julian(date.year, date.month, date.day) - self.lng / (15 * 24.0)

        # Add default parameters (maghrib and midnight) to methods if not defined.
        for _, config_ in self.methods.items():
            for name_, value_ in self.method_defaults.items():
                if name_ not in config_['params'] or config_['params'][name_] is None:
                    config_['params'][name_] = value_

        # Initialize settings.
        self.calc_method = method if method in self.methods else 'MWL'
        params = self.methods[self.calc_method]['params']

        # Fill the final settings with params
        for name, value in params.items():
            self.settings[name] = value

        # Initialize time offsets.
        for name in self.time_names:
            self.offset[name] = 0

        # Initialize time format (24h, 12h ...)
        if format_time is not None:
            self.time_format = format_time

    def set_method(self, method):
        """
        Set the calculation method.
        :param method:
        * MWL
        * ISNA
        * Egypt
        * Makkah
        * Karachi
        * Tehran
        * Jafari
        * UOIF
        :return:
        """
        if method in self.methods:
            self.adjust(self.methods[method]['params'])
            self.calc_method = method

    def adjust(self, params):
        """
        Adjust settings on prayer times.
        :param params:
        :return:
        """
        self.settings.update(params)

    def tune(self, time_offsets):
        """
        Tune prayer times and add offsets (in minutes).
        :param time_offsets:
        :return:
        """
        self.offset.update(time_offsets)

    def get_times(self, date, coords, utc_offset):
        """
        Return prayer times for a given date.
        :param utc_offset:
        :param date:
        :param coords:
        :return:
        """
        self.lat = coords[0]
        self.lng = coords[1]
        self.elv = coords[2] if len(coords) > 2 else 0

        # self.timezone = timezone + (1 if dst else 0)
        self.timezone = utc_offset
        self.julian_date = self.julian(date.year, date.month, date.day) - self.lng / (15 * 24.0)
        return self.compute_times()

    def get_formatted_time(self, time_, format_, suffixes=None):
        """
        Convert float time to the given format (see timeFormats).
        :param time_:
        :param format_:
        :param suffixes:
        :return:
        """
        if math.isnan(time_):
            # Invalid time
            return '-----'
        if format_ == 'Float':
            return time_
        if suffixes is None:
            suffixes = ['AM', 'PM']

        time_ = self.fixhour(time_ + 0.5 / 60)  # add 0.5 minutes to round
        hours = math.floor(time_)

        minutes = math.floor((time_ - hours) * 60)
        suffix = suffixes[0 if hours < 12 else 1] if format_ == '12h' else ''
        formatted_time = "%02d:%02d" % (hours, minutes) if format_ == "24h" else "%d:%02d" % (
            (hours + 11) % 12 + 1, minutes)
        return "{time} {suffix}".format(time=formatted_time, suffix=suffix)

    def mid_day(self, time_):
        """
        Compute mid-day time.
        :param time_:
        :return:
        """
        eqt = self.sun_position(self.julian_date + time_)[1]
        return self.fixhour(12 - eqt)

    def sun_angle_time(self, angle, time_, direction=None):
        """
        Compute the time at which sun reaches a specific angle below horizon.
        :param angle:
        :param time_:
        :param direction:
        :return:
        """
        try:
            decl = self.sun_position(self.julian_date + time_)[0]
            noon = self.mid_day(time_)
            t = 1 / 15.0 * self.arccos((-self.sin(angle) - self.sin(decl) * self.sin(self.lat)) /
                                       (self.cos(decl) * self.cos(self.lat)))
            return noon + (-t if direction == 'ccw' else t)
        except ValueError:
            return float('nan')

    def asr_time(self, factor, time_):
        """
        Compute asr time.
        :param factor:
        :param time_:
        :return:
        """
        decl = self.sun_position(self.julian_date + time_)[0]
        angle = -self.arccot(factor + self.tan(abs(self.lat - decl)))
        return self.sun_angle_time(angle, time_)

    def sun_position(self, jd):
        """
        Compute declination angle of sun and equation of time.
        Ref: http://aa.usno.navy.mil/faq/docs/SunApprox.php
        :param jd:
        :return:
        """
        d = jd - 2451545.0
        g = self.fixangle(357.529 + 0.98560028 * d)
        q = self.fixangle(280.459 + 0.98564736 * d)
        l = self.fixangle(q + 1.915 * self.sin(g) + 0.020 * self.sin(2 * g))

        # R = 1.00014 - 0.01671 * self.cos(g) - 0.00014 * self.cos(2 * g)
        e = 23.439 - 0.00000036 * d

        ra = self.arctan2(self.cos(e) * self.sin(l), self.cos(l)) / 15.0
        eqt = q / 15.0 - self.fixhour(ra)
        decl = self.arcsin(self.sin(e) * self.sin(l))

        return decl, eqt

    @staticmethod
    def julian(year, month, day):
        """
        Convert Gregorian date to Julian day.
        Ref: Astronomical Algorithms by Jean Meeus.
        :param year:
        :param month:
        :param day:
        :return:
        """
        if month <= 2:
            year -= 1
            month += 12
        a = math.floor(year / 100)
        b = 2 - a + math.floor(a / 4)
        return math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + b - 1524.5

    def compute_prayertimes(self, times):
        """
        Compute prayer times at given julian date.
        :param times:
        :return:
        """
        times = self.day_portion(times)
        params = self.settings

        imsak = self.sun_angle_time(self.eval(params['imsak']), times['imsak'], 'ccw')
        fajr = self.sun_angle_time(self.eval(params['fajr']), times['fajr'], 'ccw')
        sunrise = self.sun_angle_time(self.rise_set_angle(self.elv), times['sunrise'], 'ccw')
        dhuhr = self.mid_day(times['dhuhr'])
        asr = self.asr_time(self.asr_factor(params['asr']), times['asr'])
        sunset = self.sun_angle_time(self.rise_set_angle(self.elv), times['sunset'])
        maghrib = self.sun_angle_time(self.eval(params['maghrib']), times['maghrib'])
        isha = self.sun_angle_time(self.eval(params['isha']), times['isha'])

        return {
            'imsak': imsak, 'fajr': fajr, 'sunrise': sunrise, 'dhuhr': dhuhr,
            'asr': asr, 'sunset': sunset, 'maghrib': maghrib, 'isha': isha
        }

    def compute_times(self):
        """
        Compute prayer times.
        :return:
        """
        times = {'imsak': 5, 'fajr': 5, 'sunrise': 6, 'dhuhr': 12,
                 'asr': 13, 'sunset': 18, 'maghrib': 18, 'isha': 18}

        # main iterations
        times = dict(self.compute_prayertimes(times))
        times = dict(self.adjust_times(times))

        # add midnight time
        if self.settings['midnight'] == 'Jafari':
            times['midnight'] = times['sunset'] + self.time_diff(times['sunset'], times['fajr']) / 2
        else:
            times['midnight'] = times['sunset'] + self.time_diff(times['sunset'], times['sunrise']) / 2

        times = self.tune_times(times)
        return self.modify_formats(times)

    def adjust_times(self, times):
        """
        Adjust times in a prayer time array.
        :param times:
        :return:
        """
        params = self.settings
        tz_adjust = self.timezone - self.lng / 15.0

        for t in times.keys():
            times[t] += tz_adjust

        if params['highLats'] != 'None':
            times = dict(self.adjust_high_lats(times))

        if self.is_min(params['imsak']):
            times['imsak'] = times['fajr'] + self.eval(params['imsak']) / 60.0
        # need to ask about 'min' settings
        if self.is_min(params['maghrib']):
            times['maghrib'] = times['sunset'] + self.eval(params['maghrib']) / 60.0

        if self.is_min(params['isha']):
            times['isha'] = times['maghrib'] + self.eval(params['isha']) / 60.0

        times['dhuhr'] += self.eval(params['dhuhr']) / 60.0

        return times

    def asr_factor(self, asr_param):
        """
        Get asr shadow factor.
        :param asr_param:
        :return:
        """
        methods = {'Standard': 1, 'Hanafi': 2}
        return methods[asr_param] if asr_param in methods else self.eval(asr_param)

    @staticmethod
    def rise_set_angle(elevation=0):
        """
        Return sun angle for sunset/sunrise.
        :param elevation:
        :return:
        """
        elevation = 0 if elevation is None else elevation
        return 0.833 + 0.0347 * math.sqrt(elevation)  # an approximation

    def tune_times(self, times):
        """
        Apply offsets to the times.
        :param times:
        :return:
        """
        for name in times.keys():
            times[name] += self.offset[name] / 60.0
        return times

    def modify_formats(self, times):
        """
        Convert times to given time format.
        :param times:
        :return:
        """
        for name in times.keys():
            times[name] = self.get_formatted_time(times[name], self.time_format)
        return times

    def adjust_high_lats(self, times):
        """
        Adjust times for locations in higher latitudes.
        :param times:
        :return:
        """
        params = self.settings
        night_time = self.time_diff(times['sunset'], times['sunrise'])  # sunset to sunrise
        times['imsak'] = self.adjust_hl_time(times['imsak'], times['sunrise'], self.eval(params['imsak']), night_time,
                                             'ccw')
        times['fajr'] = self.adjust_hl_time(times['fajr'], times['sunrise'], self.eval(params['fajr']), night_time,
                                            'ccw')
        times['isha'] = self.adjust_hl_time(times['isha'], times['sunset'], self.eval(params['isha']), night_time)
        times['maghrib'] = self.adjust_hl_time(times['maghrib'], times['sunset'], self.eval(params['maghrib']),
                                               night_time)
        return times

    def adjust_hl_time(self, time_, base, angle, night, direction=None):
        """
        Adjust a time for higher latitudes.
        :param time_:
        :param base:
        :param angle:
        :param night:
        :param direction:
        :return:
        """
        portion = self.night_portion(angle, night)
        diff = self.time_diff(time_, base) if direction == 'ccw' else self.time_diff(base, time_)
        if math.isnan(time_) or diff > portion:
            time_ = base + (-portion if direction == 'ccw' else portion)
        return time_

    def night_portion(self, angle, night):
        """
        The night portion used for adjusting times in higher latitudes.
        :param angle:
        :param night:
        :return:
        """
        method = self.settings['highLats']
        portion = 1 / 2.0  # midnight
        if method == 'AngleBased':
            portion = 1 / 60.0 * angle
        if method == 'OneSeventh':
            portion = 1 / 7.0
        return portion * night

    @staticmethod
    def day_portion(times):
        """
        Convert hours to day portions.
        :param times:
        :return:
        """
        for element in times:
            times[element] /= 24.0
        return times

    def time_diff(self, time1, time2):
        """
        Compute the difference between two times.
        :param time1:
        :param time2:
        :return:
        """
        return self.fixhour(time2 - time1)

    @staticmethod
    def eval(st):
        """
        Convert given string into a number.
        :param st:
        :return:
        """
        val = re.split('[^0-9.+-]', str(st), 1)[0]
        return float(val) if val else 0

    @staticmethod
    def is_min(arg):
        """
        Detect if input contains 'min'.
        :param arg:
        :return:
        """
        return isinstance(arg, str) and arg.find('min') > -1

    @staticmethod
    def sin(d):
        return math.sin(math.radians(d))

    @staticmethod
    def cos(d):
        return math.cos(math.radians(d))

    @staticmethod
    def tan(d):
        return math.tan(math.radians(d))

    @staticmethod
    def arcsin(x):
        return math.degrees(math.asin(x))

    @staticmethod
    def arccos(x):
        return math.degrees(math.acos(x))

    @staticmethod
    def arctan(x):
        return math.degrees(math.atan(x))

    @staticmethod
    def arccot(x):
        return math.degrees(math.atan(1.0 / x))

    @staticmethod
    def arctan2(y, x):
        return math.degrees(math.atan2(y, x))

    def fixangle(self, angle):
        return self.fix(angle, 360.0)

    def fixhour(self, hour):
        return self.fix(hour, 24.0)

    @staticmethod
    def fix(a, mode):
        if math.isnan(a):
            return a
        a -= mode * (math.floor(a / mode))
        return a + mode if a < 0 else a


def print_begin(calc_method):
    """
    Print function. Improve readability.
    """
    intro = 'Prayer Times for today using {meth} method'.format(meth=calc_method)

    print('')
    print('=' * len(intro))
    print(intro)
    print('=' * len(intro))


def main():
    """
    Main function - Execute a test code.
    """

    # Some bugs on some calculation method like "Makkah" ...
    praytimes = PrayTimes('Makkah', format_time="24h")

    today = datetime.date.today()

    paris_lat, paris_long = 48.866, 2.33
    # Change this parameter according to the city
    paris_utc = 1

    print_begin(praytimes.calc_method)

    times = praytimes.get_times(date=today, coords=(paris_lat, paris_long), utc_offset=paris_utc)
    for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
        print("{0:<10} | {1:^12}".format(i, times[i.lower()]))

    praytimes.adjust({"asr": "Hanafi"})
    praytimes.set_method("ISNA")

    print_begin(praytimes.calc_method)

    times = praytimes.get_times(date=today, coords=(paris_lat, paris_long), utc_offset=paris_utc)
    for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
        print("{0:<10} | {1:^12}".format(i, times[i.lower()]))

    print_begin(praytimes.calc_method)

    praytimes.tune({'fajr': +10, 'dhuhr': -10, 'asr': -10, 'maghrib': -10, 'isha': +10,
                    'midnight': 5, 'sunrise': -2, 'sunset': +9, 'imsak': +15})

    times = praytimes.get_times(date=today, coords=(paris_lat, paris_long), utc_offset=paris_utc)
    for i in ['Fajr', 'Sunrise', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
        print("{0:<10} | {1:^12}".format(i, times[i.lower()]))


# Sample code to run in standalone mode only
if __name__ == "__main__":
    main()