import json
import os
# Get the path of the directory 
dir_path = os.path.dirname(os.path.abspath(__file__))

# Import a json file with all characters replacements.
with open(dir_path +'/data.json', 'r') as arq_encrypt:
    encrypt = json.load(arq_encrypt)['encrypt']
with open(dir_path +'/data.json', 'r') as arq_decrypt:
    decrypt = json.load(arq_decrypt)['decrypt']


def encrypt_text(text_to_encrypt):
    i = 0
    output_text = ""
    while i < len(text_to_encrypt):
        output_text = output_text + encrypt[text_to_encrypt[i]]
        i += 1
    print("\n\nOUTPUT: "+output_text+'\n────────────────────────────────────────')


def decrypt_text(text_to_decrypt):
    i = 0
    output_text = ""
    while i < len(text_to_decrypt):
        output_text = output_text + decrypt[text_to_decrypt[i]]
        i += 1
    print("\n\nOUTPUT: "+output_text+'\n────────────────────────────────────────')

