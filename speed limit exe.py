speed = int(input('Enter the speed:'))
speed_limit = 70
if speed <=speed_limit:
    print('ok')
else:
    excess_speed = speed -speed_limit
    points = excess_speed// 5
    #points = int(excess_speed / 5)
    print(f'point:{points}') 
    if points > 12:
        print ('license suspended')
        