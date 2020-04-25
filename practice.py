
speed = int(input('>: '))


def speed_checker(speed):
    points = 0
    speed_limit = 70
    if speed <= speed_limit:
        print('You are OK!')
    elif speed >= speed_limit + 60:
        print('You have exceeded penalty points\nLicence Suspended!')
    elif speed >= speed_limit + 5:
        # speed_limit += 5
        points += 1
        print(f'You have {points} penalty points')

speed_checker(speed)