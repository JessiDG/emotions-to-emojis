#This is a chatbot that helps people think about their emotions

import csv

class emoji_reader:

    def __init__(self, filename):
        self.emoji_database = list(csv.reader(open(filename)))

    def print_all(self):
        for i in self.emoji_database:
            print(str(i) + "\n")
        return

    def print_all_twitter(self):
        for i in self.emoji_database:
            try:
                print(str(i[4]) + "\n")
            except IndexError:
                pass

    def print_all_flags(self):
        start_of_flags = 1718
        for i in range(start_of_flags):
            try:
                print(str(self.emoji_database[start_of_flags + i]))
            except IndexError:
                pass

    def print_specific_flag0(self, country_name):
        start_of_flags = 1718
        new_str = 'flag: ' + str(country_name)
        for i in range(start_of_flags):
            try:
                for n in self.emoji_database[start_of_flags + i]:
                    if n == new_str:
                        print(self.emoji_database[start_of_flags + i][2])
            except IndexError:
                pass

    def print_specific_flag1(self, country_name):
        start_of_flags = 1718
        position_of_name = 14
        position_of_flag = 2
        new_str = 'flag: ' + str(country_name)
        for line_count in range(start_of_flags):
            # print("made it" + str(line_count))
            try:
                # print(self.emoji_database[start_of_flags + line_count][position_of_name])
                if self.emoji_database[start_of_flags + line_count][position_of_name] == new_str:
                    # print("made it")
                    print(self.emoji_database[start_of_flags + line_count][position_of_flag])
            except IndexError:
                pass

    def return_emoji_by_keyword(self, keyword):
        start = 0
        position_of_name = 14
        position_of_emoji = 2
        for line_count in range(len(self.emoji_database)):
            try:
                # print("made it")
                if str(keyword) in str(self.emoji_database[start + line_count][position_of_name]):
                    return self.emoji_database[start + line_count][position_of_emoji]
            except IndexError:
                pass
                # return "there isn't an emoji that fits that keyword. Sorry! \n"

    def return_list_of_emoji_by_keyword(self, keyword):
        start = 0
        position_of_name = 14
        position_of_emoji = 2
        emojis = []
        for line_count in range(len(self.emoji_database)):
            try:
                # print("made it")
                if str(keyword) in str(self.emoji_database[start + line_count][position_of_name]):
                    emojis.append(self.emoji_database[start + line_count][position_of_emoji])
            except IndexError:
                pass
                # emojis.append('there isn\'t an emoji that fits that keyword. Sorry! \n')
        return emojis

    def chat_bot(self):
        question = input("what are you feeling, in one word? \n")
        while question != 'no':
            print("it sounds like you're feeling: " + str(self.return_list_of_emoji_by_keyword(
                question)) + "\n"+ 'type \'no\' if you want to stop')
            question = input("what are you feeling, in one word? \n")


# if __name__ == 'main':
er = emoji_reader('emojis.csv')
# er.print_all()
# er.print_all_twitter()
# er.print_all_flags()
# print(er.emoji_database[1718])
# er.print_specific_flag0("Zambia")
# er.print_specific_flag0("Wales")
# er.print_specific_flag1("Wales")
# er.print_specific_flag1("Botswana")
# print(er.emoji_database[1718][2])
# er.print_emoji_by_keyword("watch")
# er.print_emoji_by_keyword("sad")
# er.print_emoji_by_keyword("clock")
# print(er.return_emoji_by_keyword("radio"))
# print(er.return_emoji_by_keyword("dancing"))
er.chat_bot()
