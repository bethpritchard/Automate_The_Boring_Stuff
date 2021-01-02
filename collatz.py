def collatz():
    number = 0
    while number != 1:
        number = input('Enter number:')
        try:
            number = int(number)
            while number > 1:

                if number % 2 == 0:
                    number = number / 2
                else:
                    number = (3*number)+1
                print(round(number))

        except ValueError:
            print('Please enter an integer')
            continue
collatz()
