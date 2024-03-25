current_hours = float(input("""What is your current time/hours (24 hour clock)?
Note: Give the hours as a single number with decimals (ex: 23.30 for 23:30)"""))
alarm_hours = float(input("How many hours do you wish to wait until the alarm goes off?: "))


def findHours(time, alarm):
    days = alarm_hours // 24
    hours = (current_hours + alarm_hours) % 24
    return "The alarm will go off in {} days, at {}.".format(int(days), round(hours, 2))


print(findHours(current_hours, alarm_hours))
