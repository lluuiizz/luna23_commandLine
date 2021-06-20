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
        else:
            print('YOU NEED TO PASS A VALID ARGUMENT LIKE:\nencrypt\ndecrypt\n--------------------------------------')
    else: 
        print('YOU NEED TO PASS A VALID ARGUMENT LIKE:\nencrypt\ndecrypt\n--------------------------------------')



if __name__ == '__main__':
    main()
