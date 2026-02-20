import os
import config
import sys

from time import asctime


def CLEAR_TERMINAL():
    print('\n' * os.get_terminal_size().lines)
PROGRAM_VERSION = "0.0.1v"


def PRINT_PROGRAM_SYMBOL():
    print("osy> ", end='')

# input_command = dict({
#     "help": 0, "force"
# })


def print_help():
    print('''
    You can write your command as chatting or as the olny one line

    help                    print help command
    range                   set range of the time for create files
    date_format             set custom format of date
                                (will be used in title and date in org-file)
    category                set category name
    default                 set default org-template
    output                  set path to folder
            --force                 force create new files (overwrite)

    day                     set day of a week
    week                    set number of a week
    type_week               set week type (numerator or denominator)
                                example: n1/n2/d1/d2
    b_time                  set time of the beginning classes
    e_time                  set time of the end classes
    teacher                 set teacher of the selected classes

    config                  set new config path

    print_selected          print current line
    print_default           print default template
    print_day               print current working day
    print_week              print current working week
    print_config            print current used config

    clear                   clear the area
    quit or q               exit the program''')


def print_default_template():
    print('''
#+TITLE:2025-09-02 Tuesday
#+DATE: 2025-09-02
#+CATEGORY: category_name

* Schedule [0/0]
** ...

* Deadline [0/0]
** ...

* Tasks [0/0]
** ...

* Events [0/0]
** ...

* Notes
** ...''')


def safe_exit():
    pass


def update() -> str:
    PRINT_PROGRAM_SYMBOL()
    return input()


def match_input(user_input: str):
    match(user_input[0]):
        case "help":
            print_help()
        case "default":
            config.set_default_config(config.DEFAULT_CONFIG_PATH)
        case "config":
            config.create_config(user_input[1])
        case "print_config":
            print(config.read_config(config.DEFAULT_CONFIG_PATH))
        case "print_default":
            print(config.DEFAULT_ORG_BODY)
        case "help":
            pass
        case "help":
            pass
        case "help":
            pass
        case "help":
            pass
        case "help":
            pass
        case "clear":
            CLEAR_TERMINAL()
            # PRINT_PROGRAM_SYMBOL()
        case _:
            return False


def hello_print():
    CLEAR_TERMINAL()
    print("org-schedule-yeargen" + ' ' + PROGRAM_VERSION + ' ' + asctime())
    print("Enter \"help\" to get hints")
    sys.stdout.flush()
    PRINT_PROGRAM_SYMBOL()


def cli_session():
    hello_print()
    user_input = "c"

    while (user_input[0] != 'q'):
        if match_input(user_input) is False:
            print("Incorrect input: Try again")

        user_input = update().split(' ')
    exit(0)
