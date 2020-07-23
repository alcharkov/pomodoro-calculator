import sys

pomodoro_count = 4
pomodoro_length = 25
short_break_length = 5
long_break_length = 15

def main():
    minutes = sys.argv[1]
    total = int(minutes)
    session_cnt = pomodoro_count

    pomodoros = 0
    short_breaks = 0
    long_breaks = 0
    while total >= 0:
        if session_cnt == 0:
            session_cnt = 4
            if total - long_break_length < 0:
                break
            else:
                total -= long_break_length
                long_breaks += 1
                continue

        if total - pomodoro_length < 0:
            break
        else:
            total -= pomodoro_length
            pomodoros += 1
            session_cnt -= 1

        if total - short_break_length < 0:
            break
        else:
            if session_cnt >= 1:
                total -= short_break_length
                short_breaks += 1

    print("Pomodoros: ", pomodoros)
    print("Short breaks: ", short_breaks)
    print("Long breaks: ", long_breaks)
    print("Minutes left: ", total)

if __name__ == "__main__":
    main()
