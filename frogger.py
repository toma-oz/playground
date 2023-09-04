import time
import sys

indent = 0
indent_increasing = True

try:
    while True:
        print(" " * indent, end="")
        print("🐸🐸🐸🐸🐸🐸")
        time.sleep(0.035)

        if indent_increasing:
            indent += 1
            if indent == 20:
                indent_increasing = False

        if not indent_increasing:
            indent -= 1
            if indent == 0:
                indent_increasing = True

except KeyboardInterrupt:
    print("Bye!")
