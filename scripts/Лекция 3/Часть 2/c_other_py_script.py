import sys
import time


def clear_console():
    sys.stdout.flush()
    sys.stderr.flush()
    time.sleep(0.5)


sys.stdout.write("Script output 1\n")
sys.stdout.write("Script output 2\n")
sys.stdout.write("Script output 3\n")
sys.stderr.write("Total time: 00:05:00\n")
sys.stderr.write("Total complete: 10%\n")
clear_console()

sys.stdout.write("name=Vlad\n")
sys.stdout.write("Script stdout 4\n")
sys.stdout.write("Script stdout 5\n")
sys.stderr.write("Total complete: 30%\n")
clear_console()

sys.stderr.write("Elapsed time: 00:00:10\n")
sys.stderr.write("Elapsed time: 00:00:50\n")
sys.stderr.write("Total complete: 50%\n")
sys.stdout.write("country=Russia\n")
clear_console()

sys.stderr.write("Elapsed time: 00:01:10\n")
sys.stderr.write("Total complete: 100%\n")
sys.stdout.write("Script stdout 6\n")
sys.stdout.write("Script stdout 7\n")
sys.stdout.write("website=www.google.com\n")
clear_console()
