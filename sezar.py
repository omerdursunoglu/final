maksimum_deger_araligi=26
def getType():
    while True:
        type = input("Şifreleme yapmak için 'sifrele' şifre çözmek için 'sifrecoz' yazınız:")
        if(type=="sifrele" or type=="sifrecoz"):
            return type
        else:
            print("Lütfen şifrelemek için, 'sifrele' şifre çözmek için 'sifrecoz' yazınız:")
def getKey():
    while True:
        key = int(input("Bu değer aralığında bir anahtar sayı giriniz 1-{}:".format(maksimum_deger_araligi)))
        if(key>=1 and key<=26):
            return key
        else:
            print("Bu değer aralığında bir anahtar sayı giriniz 1-{}:".format(maksimum_deger_araligi))
def getMessage(message,key,type):
    if type == "sifrecoz":
        key = -key
    translated = ""
    for letter in message:
        if letter.isalpha():
            newLetter = ord(letter)
            newLetter += key
            if letter.isupper():
                if newLetter > ord("Z"):
                    newLetter -= 26
                elif newLetter < ord("A"):
                    newLetter += 26
            elif letter.islower():
                if newLetter > ord("z"):
                    newLetter -= 26
                elif newLetter < ord("a"):
                    newLetter += 26
            translated +=chr(newLetter)
        else:
            translated+=letter
    return translated
type = getType()
key = getKey()
message = input("Şifrelemek veya çözmek istediğiniz mesajınız: ")
print("Çevrilen mesaj: {}".format(getMessage(message,key,type)))
