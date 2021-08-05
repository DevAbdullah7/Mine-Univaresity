import os
import calendar
import time
from datetime import datetime

# variable
time_now = datetime.now()
month_days = calendar.monthrange(time_now.year, time_now.month)
this_week = 0
if time_now.day <= 7:
    this_week = 1
elif 8 <= time_now.day <= 14:
    this_week = 2
elif 15 <= time_now.day <= 21:
    this_week = 3
elif 22 <= time_now.day <= 31:
    this_week = 4


def Requireds():
    print('\nYearly Requirements: 1')
    print('Monthly Requirements: 2')
    print('Weekly Requirements: 3')
    print('Daily Requirements: 4')
    klint = int(input('\n( choice ): \t ( To Exit prees 0 ): '))
    try:
        if klint == 1:
            os.system('timeline\\\\{}\\\\Requirements.txt'.format(time_now.year))
        elif klint == 2:
            os.system('timeline\\\\{}\\\\{}\\\\Requirements.txt'.format(
                time_now.year, time_now.month))
        elif klint == 3:
            os.system('timeline\\\\{}\\\\{}\\\\{}\\\\Requirements.txt'.format(
                time_now.year, time_now.month, this_week))
        elif klint == 4:
            os.system('timeline\\\\{}\\\\{}\\\\{}\\\\{}\\\\Requirements.txt'.format(
                time_now.year, time_now.month, this_week, time_now.day))
        elif klint == 0:
            pass
        else:
            raise Exception('Error: Your choice is incorrect !')
    except Exception as Error:
        print(Error)
        time.sleep(2)
        Requireds()


def Attendees():
    pass


def Reports():
    pass


def Subjects():
    pass
