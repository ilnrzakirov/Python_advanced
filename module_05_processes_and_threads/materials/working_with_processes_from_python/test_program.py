import sys
import time
import subprocess



# def main():
#     print('Start program and going to sleep')
#     time.sleep(5)
#     print('Done sleeping 5 seconds. Bye!')
#

def main():
   print('Print to stdout')
   print('Print to stderr', file=sys.stderr)
   user_input = input()
   input_line_1 = input()
   input_line_2 = input()
   input_line_3 = input()
   print('User input: "{}"'.format(user_input))
   print('User input: "{}"'.format(input_line_2))
   print('User input: "{}"'.format(input_line_1))
   print('User input: "{}"'.format(input_line_3))


if __name__ == '__main__':
    main()
