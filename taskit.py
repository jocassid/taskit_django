
from django_init import django_init
django_init()

if True:
    from main.models import Task


import cmd, sys
from taskit import *

class TaskitShell(cmd.Cmd):
    intro = 'Welcome to the taskit shell.   Type help or ? to list commands.\n'
    prompt = '(taskit) '
    file = None

    def do_create(self, arg):
        """create a task"""

        description = input("Enter description: ")
        priority = input("Enter priority (1-4, 4 is highest): ")
        due_date = input("Enter due date (YYYY-MM-DD) or enter to leave blank: ")

        ok = input("Is this correct? (y/n) ")
        if not ok:
            return

        task = Task.objects.create(
            description=description,
            priority=priority,
            due_date=due_date,
        )
        print("Task created successfully.")




    # def do_right(self, arg):
    #     'Turn taskit right by given number of degrees:  RIGHT 20'
    #     right(*parse(arg))
    # def do_left(self, arg):
    #     'Turn taskit left by given number of degrees:  LEFT 90'
    #     left(*parse(arg))
    # def do_goto(self, arg):
    #     'Move taskit to an absolute position with changing orientation.  GOTO 100 200'
    #     goto(*parse(arg))
    # def do_home(self, arg):
    #     'Return taskit to the home position:  HOME'
    #     home()
    # def do_circle(self, arg):
    #     'Draw circle with given radius an options extent and steps:  CIRCLE 50'
    #     circle(*parse(arg))
    # def do_position(self, arg):
    #     'Print the current taskit position:  POSITION'
    #     print('Current position is %d %d\n' % position())
    # def do_heading(self, arg):
    #     'Print the current taskit heading in degrees:  HEADING'
    #     print('Current heading is %d\n' % (heading(),))
    # def do_color(self, arg):
    #     'Set the color:  COLOR BLUE'
    #     color(arg.lower())
    # def do_undo(self, arg):
    #     'Undo (repeatedly) the last taskit action(s):  UNDO'
    # def do_reset(self, arg):
    #     'Clear the screen and return taskit to center:  RESET'
    #     reset()
    # def do_bye(self, arg):
    #     'Stop recording, close the taskit window, and exit:  BYE'
    #     print('Thank you for using taskit')
    #     self.close()
    #     bye()
    #     return True
    #
    # # ----- record and playback -----
    # def do_record(self, arg):
    #     'Save future commands to filename:  RECORD rose.cmd'
    #     self.file = open(arg, 'w')
    # def do_playback(self, arg):
    #     'Playback commands from a file:  PLAYBACK rose.cmd'
    #     self.close()
    #     with open(arg) as f:
    #         self.cmdqueue.extend(f.read().splitlines())
    # def precmd(self, line):
    #     line = line.lower()
    #     if self.file and 'playback' not in line:
    #         print(line, file=self.file)
    #     return line
    # def close(self):
    #     if self.file:
    #         self.file.close()
    #         self.file = None

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    TaskitShell().cmdloop()