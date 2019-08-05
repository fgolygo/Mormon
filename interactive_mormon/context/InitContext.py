from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle, prompt

from context.ColleagueContext import ColleagueContext

get_colleague = 'get_colleague'
do_exit = 'exit'

initial_command_completer = WordCompleter([
    get_colleague, do_exit,
], meta_dict={
    get_colleague: 'fetches colleague and enters colleague context',
    do_exit: 'exit the application',
}, ignore_case=True)


class InitContext:

    @staticmethod
    def get_colleague():
        args = prompt('Provide args: ', bottom_toolbar='colleagueUUID')
        fetched_colleague = 'trn:tesco:12345'
        ColleagueContext(fetched_colleague).main()

    @staticmethod
    def get_customer():
        args = prompt('Provide args: ', bottom_toolbar='customerUUID')
        print(args)

    def main(self):
        while True:
            command = prompt(
                'init context:> ',
                completer=initial_command_completer,
                complete_style=CompleteStyle.COLUMN
            )

            if command == do_exit:
                return

            if command == get_colleague:
                self.get_colleague()
