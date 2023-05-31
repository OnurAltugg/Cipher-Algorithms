def breakk(encrypted_str):
    return;
    
def encryption(text, key):
    new_text = ""
    count = 0
    for i in text:
        if i.isalpha == False :
            continue;
        for j in alphabet:
            if j==i.lower():
                new_text = new_text + alphabet[(count+key)%26].upper()
            else:
                count += 1
                continue; 
        count = 0
    return new_text;

def decryption(text, key):
    new_text = ""
    count = 0
    for i in text:
        for j in alphabet:
            if j==i.lower():
                new_text = new_text + alphabet[(count-key)%26]
            else :    
                count += 1
                continue; 
        count = 0
    return new_text;
    return;
    
alphabet = "abcdefghijklmnopqrstuvwxyz"
text = "gaul is divided into three parts"
text = encryption(text, 3)
print("cipherext -> " + text)
text = decryption(text, 3)
print("plaintext -> " + text)



                
                
                
