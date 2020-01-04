#Assignment 1
#Taliyah Rivera
#CSCI 3351

plain = "abcdefghijklmnopqrstuvwxzy"
shifted=""
lists= []
cryptlist=[]
decryptlist=[]
#had to put the shifted alphabet in a list to save it for the decrypt function

shift= int(input("What is the number you would like to shift by? "))
sentence= input("What do you want to encrpyt?")
def encrpyt1():
    splain = slice(shift)
    extra = plain[splain]
    shifted = plain[shift:26] + extra
    print ("this is your encrpyted alphabet: ",shifted)
    lists.append(shifted)
    for letters in sentence:
        if letters in plain:
            plainindex = plain.index(letters)
            cipherindex = (plainindex+shift)%26
            extra2 = plain[cipherindex]
        else:
            extra2 = letters
        cryptlist.append(extra2)
    encrptyed = ''.join(cryptlist)
    print ("Here is your encryption method 1: ",encrptyed)
        
def decrypt1():
   #slice it back
    shifted=lists[0]
    splain =slice(-shift)
    extra = shifted[splain]
    unshifted = shifted[-shift:]+extra
    for letters in cryptlist:
        if letters in shifted:
            cypherindex= shifted.index(letters)
            plainindex=(cypherindex-shift)%26
            extra2=shifted[plainindex]
        else:
            extra2=letters
        decryptlist.append(extra2)
    decrypted = "".join(decryptlist)
    print("Here is the decryption method 1:", decrypted)
    
    

#Method 2
my_dic= {'plainalpha':"abcdefghijklmnopqrstuvwxyz" , 'cipheralpha':"" , 'encrptedw':"" , 'decryptedw:':""}

def encrpyt2():
    splain = slice(shift)
    planstr=my_dic.get("plainalpha")
    extra = planstr[splain]
    cipstr=my_dic.get('cipheralpha') 
    cipstr= (planstr[shift:26]) + extra
    my_dic['cipheralpha']= cipstr
    enc=[]
    for letters in sentence:
        if letters in planstr:
            plainindex = planstr.index(letters)
            cipherindex = (plainindex+shift)%26 
            encrpytedw=my_dic.get('encrptedw')
            encrpytedw = planstr[cipherindex]
        else:
            encrpytedw = letters
        enc.append(encrpytedw) #put it in a list because the dictonary didn't take mutiple keys
    encj=''.join(enc)
    my_dic['encrptedw']=encj 
    print ("Here is your encryption method 2: ",my_dic['encrptedw'])
    
     
def decrypt2():
    splain =slice(-shift)
    shifty=my_dic.get("cipheralpha")
    extra = shifty[splain]
    planstr=my_dic.get('plainalpha')
    planstr = shifty[-shift:]+extra
    dec=[]
    for letters in my_dic['encrptedw']:
        if letters in shifty:
            cypherindex= shifty.index(letters)
            plainindex=(cypherindex-shift)%26
            decryptedw=my_dic.get('decryptedw')
            decryptedw=shifty[plainindex]
        else:
            decryptedw=letters
        dec.append(decryptedw)
    decrypted = "".join(dec)
    my_dic['decryptedw']=decrypted
    print("Here is the decryption method 2:", my_dic['decryptedw'])

encrpyt1()
decrypt1()
encrpyt2()   
decrypt2()
