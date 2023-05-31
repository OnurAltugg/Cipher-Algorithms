def rc4_encrypt(plain_text, key):
    
    S = [] #S-Box
    K = [] #for Convert Key into ASCII form.
    j = 0
    temp = 0
    plain_text_ascıı_form = []
    key_stream_ascıı_form = []
    for i in range(256):
        S.append(i)
        
        
    for i in plain_text:
        plain_text_ascıı_form.append(ord(i))
        
    while(len(K) != 256):
       for i in key:
           K.append(ord(i))
           if(len(K) == 256):
               break
           
    for i in range(256):
        j = (j + S[i] + K[i]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        
    j = 0
    for i in range(len(plain_text_ascıı_form)):
        j = (j + S[i]) % 256
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        t = (S[i] + S[j]) % 256
        key_stream_ascıı_form.append(S[t])
    
    create_cipher_text(plain_text_ascıı_form, key_stream_ascıı_form)
        
def create_cipher_text(plain_text, key_stream):
    cipher_text_ascii_form = []
    cipher_text = ''
    counter = 0
    while (counter != len(plain_text)):
        cipher_text_ascii_form.append(plain_text[counter] ^ key_stream[counter])
        counter+=1
    cipher_text = ''.join([chr(code) for code in cipher_text_ascii_form])
    return cipher_text
     
plain_text = "Robbi Rahim"
key = "narutokeren"
cipher_text = rc4_encrypt(plain_text, key)
print(cipher_text)
