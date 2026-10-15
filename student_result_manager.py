student = {}

while True:
    print('\n --------WELCOME TO STUDENT RESULT MANAGER--------')

    print('Add Student : 1')
    print('View Students : 2')
    print('View Result : 3')
    print('Exit : 4')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter Name: ')
        marks = int(input('Enter marks: '))

        student[name] = marks
        print(f'{name} successfully Added')

    elif choice == '2':
        if not student:
            print('No student Exist')
        else:
            for name, marks in student.items():
                print(f'{name} : {marks}')

    elif choice == '3':
        name = input('Enter Student Name : ')
        if name in student:
            marks = student[name]

            if marks >= 45:
                print('Pass')
            else:
                print('Fail')

    elif choice == '4':
        print('Exiting...')
        break

    else:
        print('Invalid choice')