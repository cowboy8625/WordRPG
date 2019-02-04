""" Module for working with 'game time' """

import time
from datetime import datetime, timedelta



class Game_Time:
    def __init__(self, year=2050, month=4, day=14, hour=12, minute=0, second=0):
        self.datetime = datetime(year, month, day,
                                 hour=hour, minute=minute, second=second)
        

    def add_time(self, weeks=0, days=0, hours=0, minutes=0, seconds=0):
        """ adds time to self """
        self.datetime += timedelta(weeks=weeks, days=days, minutes=minutes,
                                    seconds=seconds)

    def get_date_string(self):
        """ returns the date as M/D/YEAR """
        y = str(self.datetime.year)
        m = str(self.datetime.month).zfill(2)

        d = str(self.datetime.day).zfill(2)
        return f"{m}/{d}/{y}"


    def get_time_string(self):
        """ returns the time as HH:MM AM/PM """
        h = str(self.datetime.hour).zfill(2)
        m = str(self.datetime.minute).zfill(2)
        d = datetime.strptime(f"{h}:{m}", "%H:%M")
        return d.strftime("%I:%M %p")


    def __repr__(self):
        y = str(self.datetime.year)
        m = str(self.datetime.month).zfill(2)
        d = str(self.datetime.day).zfill(2)
        h = str(self.datetime.hour).zfill(2)
        m = str(self.datetime.minute).zfill(2)
        s = str(self.datetime.second).zfill(2)
        return f"Game_Time(year={y}, month={m}, day={d}, hour={h}, minute={m}, second={s})"


    def __str__(self):
        return str(self.datetime)
