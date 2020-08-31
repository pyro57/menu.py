#!/usr/bin/python3
class option:
    def __init__(self, function, name):
        self.function = function
        self.name = name

    def run(self):
        self.function()


class menu:
    def __init__(self, options, name):
        self.options = options
        self.name = name
    def display(self):
        while True:
            print("\n"*100)
            print("+++++++++++++++ {} ++++++++++++++++++".format(self.name))
            optioncount = 1
            optiondict = {}
            for option in self.options:
                print("{}.) {}".format(optioncount, option.name))
                optiondict[optioncount] = option.run
                optioncount = optioncount + 1
            print("{}.) exit".format(optioncount))
            optiondict[optioncount] = 'exit'
            selection = int(input("$>"))
            if selection in optiondict.keys():
                if optiondict[selection] == 'exit':
                    break
                else:
                    optiondict[selection]()
                    input("press enter to continue")
            else:
                print('invalid selection')
                input("press enter to continue")
