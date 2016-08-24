
def main():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45''BaseInterpreterInterface', 'BaseStdIn',
                 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    is_valid_answer = False
    while not is_valid_answer:
        username = input("Enter Your User Name (blank to Exit):")
        if username == "":
            break
        else:
            if username in usernames:
                print("Access granted")
                is_valid_answer = True
            else:
                print("Access denied")
main()