def encrypt(message):
 words=[]
 for char in message:
  encrypted_char=ord(char)
  words.append(chr(encrypted_char-3))
  words_string="".join(words)
 print(words_string)
def decrypt(message):
 words=[]
 for char in message:
  decrypted_char=ord(char)
  words.append(chr(decrypted_char+3))
  words_string="".join(words)
 print(words_string)
decrypt(" fjfppvlrtebk`^kvlr`ljb_^`h+++")