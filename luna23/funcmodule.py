import json
# Import a json file with all characters replacements.
with open('data.json', 'r') as arq_encrypt:
    encrypt = json.load(arq_encrypt)['encrypt']
with open('data.json', 'r') as arq_decrypt:
    decrypt = json.load(arq_decrypt)['decrypt']


def encrypt_text(text_to_encrypt):
    i = 0
    output_text = ""
    while i < len(text_to_encrypt):
        output_text = output_text + encrypt[text_to_encrypt[i]]
        i += 1
    print("―――――――――――――――――――――――――――――――\nOUTPUT: "+output_text)
def decrypt_text(text_to_decrypt):
    while i < len(text_to_decrypt):
        output_text = output_text + decrypt[text_to_decrypt[i]]
        i += 1
    print("―――――――――――――――――――――――――――――――\nOUTPUT: "+output_text)

