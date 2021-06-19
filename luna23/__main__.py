import sys 
from .classmodule import MyClass
from .funcmodule import encrypt
from .funcmodule import decrypt



def main():
    args = sys.argv[1:]
    if args != []:
        if args[0] == 'encrypt' and len(args) == 1:
            text = input('INPUT: ')
            encrypt(text)
        elif args[0] == 'decrypt' and len(args) == 1:
            text = input('INPUT: ')
        else:
            print('YOU NEED TO PASS A VALID ARGUMENT LIKE:\nencrypt\ndecrypt\n--------------------------------------')
    else: 
        print('YOU NEED TO PASS A VALID ARGUMENT LIKE:\nencrypt\ndecrypt\n--------------------------------------')
    '''print('count of args :: {}'.format(len(args)))
    for arg in args: 
        print ('passed argument :: {}'.format(arg))
    my_function('hello world')
    if len(args) != 0:
        my_object = MyClass('{}'.format(args[0]))
        my_object.say_name()
    else:
        print('No name inputed!!!')'''
    


if __name__ == '__main__':
    main()
