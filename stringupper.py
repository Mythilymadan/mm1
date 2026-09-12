class IOString:

    def __init__(self):
        self.str1=""


    def get_str(self):
        self.str1=input("Enter the String:")

    
    def print_str(self):
        print("Result is ",self.str1.upper())

str2=IOString()

str2.get_str()
str2.print_str()
