class Time:
    """Blueprint for the Time Object"""
    def __init__(self):
        self.__hour = 0
        self.__minute = 0
        self.__second = 0


    def set_time(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def print_time(self):
        print (self.__hour, ":", self.__minute, ":", self.__second)

    def set_second(self, second):
        self.__second = second
        while self.__second > 59:
            self.__second = eval(input("Select an appropriate second 0-59: ")) 

    def get_second(self):
        return self.__second

    def set_hour(self, hour):
        self.__hour = hour
        while self.__hour > 23:
            self.__hour = eval(input("Select an appropriate hour 0-23: "))             

    def get_hour(self):
        return self.__hour

    def set_minute(self, minute):
        self.__minute = minute
        while self.__minute > 59:
            self.__minute = eval(input("Select an appropriate minute 0-59: "))

    def get_minute(self):
        return self.__minute

    def tick_second(self):
        """Adds one to the seconds and checks minutes / hours"""
        import time
        while self.__second != 61:
            if self.__second == 60:
                self.__second = 0
                self.__minute = self.__minute + 1
                if self.__minute == 60:
                    self.__minute = 0
                    self.__hour = self.__hour + 1
                    if self.__hour == 24:
                        self.__hour == 0
                print (self.__hour, ":", self.__minute, ":", self.__second)
                time.sleep(1)
            else:
                print (self.__hour, ":", self.__minute, ":", self.__second)
            self.__second = self.__second + 1
            time.sleep(1)
        
                
        
    
        
