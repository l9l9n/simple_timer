import time


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = f'{mins}:{secs}'
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1
    print("Timer Ended")

countdown(120) # Example 2 min >> countdown(120) 