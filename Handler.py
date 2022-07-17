from InputNumbers import InputNumbers
from Functuions import Functions
class Handler:

    def __init__(self):
        self.inputer = InputNumbers()
        self.function = Functions()


    def chooose_operation(self):
        print("Please insert the first clock time")
        list_clock =self.inputer.introduce_element()
        print(self.inputer.show_clock(list_clock))

        while True:
            print("Please choose what opeartion you would like")
            print("1. Insert a new time")
            print("2. Let the clock tick")
            print("3.Reset the clock")

            option = int(input(""))

            if option ==1:
                list_new_clock = self.inputer.introduce_element()
                print(self.inputer.show_clock(list_new_clock))
            if option==2:
                self.function.count_clock(list_clock)
            if option==3:
                reseted_clock =self.function.reset_clock(list_clock)
                print(reseted_clock)

