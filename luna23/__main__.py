import sys 
from .funcmodule import encrypt_text
from .funcmodule import decrypt_text
def main():
    args = sys.argv[1:]
    if args != []:
        if args[0] == 'encrypt' and len(args) == 1:
            text = input('INPUT: ')
            encrypt_text(text)
        elif args[0] == 'decrypt' and len(args) == 1:
            text = input('INPUT: ')
            decrypt_text(text)
        elif args[0] == 'info' and len(args) == 1:
            print('\n\n────────────────────────────────────────────────────────────────────────────────')
            print('Name: Luna23 Command Line Interface')
            print('Version: 0.1.0')
            print('Description: Program created to encrypt and decrypt texts in luna23 format')
            print('Created by: Luiz Guilherme Costa da Silva')
            print('Special thanks to my girlfriend who came up with the idea. Love you!')
            print('────────────────────────────────────────────────────────────────────────────────\n\n')
        else:
            print('\n\n────────────────────────────────────────\nYOU NEED TO PASS A VALID ARGUMENT LIKE:\nencrypt\ndecrypt\ninfo\n────────────────────────────────────────\n\n')
    else: 
        print('\n\n───────────────────────────────────────\nYOU NEED TO PASS A VALID ARGUMENT LIKE:\nencrypt\ndecrypt\ninfo\n────────────────────────────────────────\n\n')


if __name__ == '__main__':
    main()
