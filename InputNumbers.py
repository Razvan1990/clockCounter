class InputNumbers:


    def __init__(self):
        self.hour = "0"
        self.minute = "00"
        self.seconds = "00"


    def introduce_element(self):
        list_clock = list()
        hour = int(input("Please introduce the desired hour "))
        while hour > 24 or hour < 0:
            print("Not a correct hour. Please introduce again ")
            hour = int(input(""))
        minute = int(input("Please introduce the desired minute "))
        while minute > 59 or minute < 0:
            print("Not a correct minute. Please introduce again ")
            minute = int(input(""))
        second = int(input("Please introduce the desired seconds "))
        while second > 59 or second < 0:
            print("Not a correct second. Please introduce again ")
            second = int(input(""))
        list_clock.append(hour);
        list_clock.append(minute);
        list_clock.append(second)
        return list_clock


    def show_clock(self, list_clock):
        if len(list_clock) == 3:
            hour = list_clock[0]
            minute = list_clock[1]
            second = list_clock[2]
        else:
            raise Exception("SOmething went wrong in the tuple clock formation")

        hour_string = self.get_digit_numbers(hour)
        minute_string = self.get_digit_numbers(minute)
        second_string = self.get_digit_numbers(second)

        clock_value = hour_string + ":" + minute_string + ":" + second_string
        return clock_value


    def get_digit_numbers(self, number):
        counter_numbers = 0
        number_initial = number
        if number_initial == 0:
            number_converted = '0' + str(number_initial)
            return number_converted
        while (number != 0):
            digit = number % 10
            counter_numbers += 1
            number = number // 10
        if counter_numbers == 1:
            number_converted = '0' + str(number_initial)
        else:
            number_converted = str(number_initial)
        return number_converted






