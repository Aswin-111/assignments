def temp(temp):
    if temp > 100:
        print('It is hot')
    elif temp > 61 & temp < 99:
        print('It is just right.')
    elif temp < 60 & temp > 0:
        print('Its is cold')


while temp != 0:
    data = int(input('Enter the temperature '))
    if data == 0:
        break
    else:
        temp(data)
print('Good bye')