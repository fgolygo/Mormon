from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle, prompt

show_my_id = 'show_my_id'
do_exit = 'exit'

colleague_command_completer = WordCompleter([
    show_my_id, do_exit,
], meta_dict={
    do_exit: 'exit colleague context',
    show_my_id: 'show current colleague id',
}, ignore_case=True)


class ColleagueContext:

    def __init__(self, colleague_id):
        self.colleagueId = colleague_id

    def show_my_id(self):
        print("colleagueId: {}".format(self.colleagueId))

    def main(self):
        while True:
            command = prompt(
                'colleague context:> ',
                completer=colleague_command_completer,
                complete_style=CompleteStyle.COLUMN
            )

            if command == do_exit:
                return

            if command == show_my_id:
                self.show_my_id()
