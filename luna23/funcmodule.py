import json
# Import a json file with all characters replacements.
with open("data.json") as file:
    encrypt_dic = json.load(file)["encrypt"]
with open("data.json") as file:
    decrypt_dic = json.load(file)["decrypt"]

def encrypt(text_to_encrypt):
    '''print('text from my_function :: {}'.format(text_to_encrypt))'''
    print('encrypt')
def decrypt(text_to_decrypt):
    '''print('text from my_function :: {}'.format(text_to_decrypt))'''
    print('decrypt')



