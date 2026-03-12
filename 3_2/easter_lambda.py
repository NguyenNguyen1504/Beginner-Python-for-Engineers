import datetime
def main():
    # Write your code here
    easter_check = lambda dt: dt.month == 4
    easter_countdown = lambda dt: 4 - dt.month
    hunt_check = lambda dt: dt.hour >= 9
    hunt_countdown = lambda dt: (8 - dt.hour, 59 - dt.minute, 59 - dt.second)

    print("Welcome to Easter countdown!")
    print("Is Easter this month?")
    now = datetime.datetime.now()
    if not easter_check(now):
        days = easter_countdown(now)
        print(f"Nope, but the number of months until April is: {days:d}")
    else:
        print("Yes!")
    print("Let's get ready for the Easter egg hunt!")
    if not hunt_check(now):
        hours, mins, secs = hunt_countdown(now)
        print(f"You have {hours:d} hours, {mins:d} minutes, and {secs:d} seconds until the egg hunt.")
    else:
        print("It's already time for the egg hunt! Let's go!")

    # Write your code here

main()