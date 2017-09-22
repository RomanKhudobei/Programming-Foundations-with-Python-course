import sys
import time
import webbrowser
import winsound

def reminder(repeat, period):
    try:
        repeat = int(repeat)
        period = int(period)
    except:
        print('Programm takes only numbers!')
    else:
        counter = 0
        while counter < repeat:
            time.sleep(period)
            webbrowser.open_new_tab("http://blimb.su/")
            winsound.PlaySound('SystemExit', winsound.SND_ALIAS)
            counter += 1


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python break_time.py how_many_times_repeat period_in_seconds')
        sys.exit(1)
    arg = sys.argv[1:]
    reminder(arg[0], arg[1])