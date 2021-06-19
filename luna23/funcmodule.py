import json
# Import a json file with all characters replacements.
with open('./json/encrypt-decrypt.json', 'r') as arq_encrypt:
    encrypt = json.load(arq_encrypt)['encrypt']
with open('./json/encrypt-decrypt.json', 'r') as arq_decrypt:
    decrypt = json.load(arq_decrypt)['decrypt']

def encrypt(text_to_encrypt):
    '''print('text from my_function :: {}'.format(text_to_encrypt))'''
    i = 0
    output_text = ""
    while i < len(text_to_encrypt):
        output_text = output_text + encrypt[text_to_encrypt[i]]
        i += 1
    print('OUTPUT: ' + output_text)
def decrypt(text_to_decrypt):
    '''print('text from my_function :: {}'.format(text_to_decrypt))'''



