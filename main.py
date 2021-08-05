import methods


def main():
    print('\n\t{} {}/{}/{}\n'.format(methods.time_now.strftime('%A'),
          methods.time_now.day, methods.time_now.month, methods.time_now.year))
    print('For Requireds: 1')
    print('For Attendees: 2')
    print('For Reports: 3')
    print('For Subjects: 4')
    user = int(input('\n( choice ): \t ( To Exit prees 0 ): '))
    try:
        if user == 1:
            methods.Requireds()
            main()
        elif user == 2:
            methods.Attendees()
        elif user == 3:
            methods.Reports()
        elif user == 4:
            methods.Subjects()
        elif user == 0:
            pass
        else:
            raise Exception('Error: Your choice is incorrect !')
    except Exception as Error:
        print(Error)
        main()


main()
