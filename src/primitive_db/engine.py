import prompt

HELP_TEXT = (
    "<command> exit - выйти из программы\n"
    "<command> help - справочная информация"
)

def welcome() -> None:
    print (HELP_TEXT)
    command = prompt.string('Введите команду: ')
        
    match command:
            case 'exit':
                return
            case 'help':
                welcome()
            case _:
                return