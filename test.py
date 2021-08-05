import os
import time
from datetime import datetime
#from typing_extensions import Required

# varibles
time_now = datetime.now()
weekend = ('Fri', 'Sat')

print('Welcome ^_^\n\n')

def plans():
    print('road map: 1')
    print('required tasks: 2')
    plansUser = int(input('choice: \t ( To Exit prees E ): '))
    try:
        if plansUser == 1:
            roadmapList = []
            roadmap = open('plans\qroadmap.txt', 'r')
            lines = roadmap.readlines()
            print('show road map: 1')
            print('edit road map: 2')
            plansUserSec = int(input('choice: \t ( To Exit prees E ): '))
            if plansUserSec == 1:
                for line in lines:
                    print(line)
            elif plansUserSec == 2:
                specialization = input('what\'s your Specialization: ')
                subjects = int(input('how muny subject: '))
                subjectsList = [specialization, '\n']
                for i in range(subjects):
                    subjectsList.append(input('subject: ')+'\n')
                with open('plans\qroadmap.txt', 'w') as roadmapw:
                    roadmapw.writelines(subjectsList)
            else:
                raise Exception('Error: Your choice is incorrect!')
            main()
        elif plansUser == 2:
            requiredTasksList = []
            print('daily required tasks: 1')
            print('weekly required tasks: 2')
            plansUserSec = int(input('choice: \t ( To Exit prees E ): '))
            if plansUserSec == 1:
                requiredTasksFile = open('plans\qdrequiredtasks', 'r')
                lines = requiredTasksFile.readlines()
                print('show required tasks: 1')
                print('edit required tasks: 2')
                plansUserSec = int(input('choice: \t ( To Exit prees E ): '))
                if plansUserSec == 1:
                    for line in lines:
                        print(line)
                elif plansUserSec == 2:
                    requiredTaskCount = int(input('How muny required tasks: '))        
            elif plansUserSec == 2:
                requiredTasksFile = open('plans\qwrequiredtasks', 'r')
                lines = requiredTasksFile.readlines()
                print('show required tasks: 1')
                print('edit required tasks: 2')
                plansUserSec = int(input('choice: \t ( To Exit prees E ): '))
                if plansUserSec == 1:
                    for line in lines:
                        print(line)
                elif plansUserSec == 2:
                    requiredTaskCount = int(input('How muny required tasks: '))


        else:
            raise Exception('Error: Your choice is incorrect!')
    except Exception as Error:
        print(Error)
        plans()


def attendees():
    pass

def reborts():
    pass

def main():
    print('For plans: 1')
    print('For attendees: 2')
    print('For aeborts: 3')
    try:
        user = int(input('( 1 OR 2 ): \t ( To Exit prees E ): '))
        if user == 1:
            plans()
            main()
        elif user == 2:
            day = time_now.strftime('%A')
            with open('attendees\days\{}.txt'.format(day), 'r') as attendees:
                lines = attendees.readlines()
                attendeesList = []
                for i in lines:
                    attendeesList.append(i+'')
            print('start day: 1')
            print('css: 2')
            print('django first: 3')
            print('django second: 4')
            attendeesUser = int(input('choice: \t ( To Exit prees E ): '))
            if attendeesUser == 1:
                if 'start day' in i:
                    temp_hour = time_now.hour
                    temp_minute = time_now.minute
                    attendeesList[2] = 'start day : done at {}:{}\n'.format(time_now.hour, time_now.minute)
                with open('attendees\days\{}.txt'.format(day), 'w') as attendeesw:
                    attendeesw.writelines(attendeesList)
                for i in attendeesList:
                    print(i)
                main()
            elif attendeesUser == 2:
                css = int(input('class 1 OR class 2'))
                if 'css' in i and css == 1:
                    attendeesList[3] = 'css : done at {}:{} , ----\n'.format(time_now.hour, time_now.minute)
                if 'css' in i and css == 2:
                    tempindix = attendeesList[3]
                    attendeesList[3] = tempindix.replace('----', 'done at {}:{}\n'.format(time_now.hour, time_now.minute))
                with open('attendees\days\{}.txt'.format(day), 'w') as attendeesw:
                    attendeesw.writelines(attendeesList)
                for i in attendeesList:
                    print(i)
                main()
            if attendeesUser == 3:
                count_attendeesListIndix = -1
                for i in attendeesList:
                    count_attendeesListIndix += 1
                    if 'django first' in i:
                        temp_hour = time_now.hour
                        temp_minute = time_now.minute
                        attendeesList[count_attendeesListIndix] = 'django first : done at {}:{}\n'.format(time_now.hour, time_now.minute)
                        break
                with open('attendees\days\{}.txt'.format(day), 'w') as attendeesw:
                    attendeesw.writelines(attendeesList)
                for i in attendeesList:
                    print(i)
                main()
            if attendeesUser == 4:
                count_attendeesListIndix = -1
                for i in attendeesList:
                    count_attendeesListIndix += 1
                    if 'django second' in i:
                        temp_hour = time_now.hour
                        temp_minute = time_now.minute
                        attendeesList[count_attendeesListIndix] = 'django second : done at {}:{}\n'.format(time_now.hour, time_now.minute)
                        break
                with open('attendees\days\{}.txt'.format(day), 'w') as attendeesw:
                    attendeesw.writelines(attendeesList)
                for i in attendeesList:
                    print(i)
                main()

        else:
            raise Exception('Error: Your choice is incorrect !')
    except Exception as Error:
        print(Error)
        main()


main()
input('any key to left: ')