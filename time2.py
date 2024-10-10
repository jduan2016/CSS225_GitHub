
# str_time = input("What time is it now?")
# str_wait_time = input("What is the number of hours to wait? ")
# time = int(str_time)
# wait_time = int(str_wait_time)

# Adding input data validation
def get_time_input():
    while True:
        str_time = input("What time is it now?")
        try:
            time = int(str_time)
        except:
            print("Please enter number digits")
            continue
        if time < 0 or time > 12:
            print("Please enter a number between 0 and 12")
            continue
        break
    return time

def get_wait_time_input():
    while True:
        str_wait_time = input("What is the number of hours to wait?")
        try:
            wait_time = int(str_wait_time)
        except:
            print("Please enter number digits")
            continue
        if wait_time < 0:
            print("Please enter a positive number")
            continue
        break
    return wait_time

time = get_time_input()
wait_time = get_wait_time_input()


time_when_alarm_go_off = (time + wait_time) % 12 # Assume the alarm only has 12 hours
print(time_when_alarm_go_off)
