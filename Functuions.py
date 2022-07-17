import sys
import time
import os
import keyboard
from InputNumbers import InputNumbers


class Functions:

    # clear = lambda: os.system('cls')  # On Windows System

    def __init__(self):
        self.input = InputNumbers()
        self.zero_adding = '0'

    def screen_clear(self):
        # for mac and linux(here, os.name is 'posix')
        if os.name == 'posix':
            _ = os.system('clear')
        else:
            # for windows platfrom
            _ = os.system('cls')

    def reset_clock(self, list_clock):
        list_clock[0] = 0
        list_clock[1] = 0
        list_clock[2] = 0

        reseted_clock = self.zero_adding + str(list_clock[0]) + ":" + self.zero_adding + str(
            list_clock[1]) + ":" + self.zero_adding + str(list_clock[2])
        return reseted_clock

    def update_list(self, lista, element1, element2, element3):
        lista.clear()
        lista.append(element1);
        lista.append(element2);
        lista.append(element3);

    def interrupt_clock(self):
        pass

    def count_clock(self, list_clock):

        # first have the hour
        print("Current hour is")
        current_hour = self.input.show_clock(list_clock)
        print(current_hour)
        time.sleep(1)
        print("In order to interrupt current script press End")
        time.sleep(2)
        hour = list_clock[0]
        minute = list_clock[1]
        second = list_clock[2]
        while True:
            # start counting
            # print("Current hour is")
            second += 1
            self.update_list(list_clock, hour, minute, second)
            time.sleep(0.1)
            print(self.input.show_clock(list_clock))
            # self.screen_clear()
            time.sleep(0.3)
            if second > 58:
                minute += 1
                second = 0
                self.update_list(list_clock, hour, minute, second)
                time.sleep(1)
                print(self.input.show_clock(list_clock))
            if minute > 58:
                hour += 1
                minute = 0
                second = 0
                self.update_list(list_clock, hour, second, second)
                time.sleep(1)
                print(self.input.show_clock(list_clock))
            if hour > 23:
                hour = 0
                minute = 0
                second = 0
                self.update_list(list_clock, hour, minute, second)
                time.sleep(1)
                print(self.input.show_clock(list_clock))
            if keyboard.is_pressed("End"):
                print("Program terminated")
                break



















