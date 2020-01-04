#Fun with GUI
#Taliyah Rivera


import tkinter
from tkinter import *
from tkinter import messagebox
class encrpty(object):

    
    def display(self):
        top =Tk()
        top.geometry("300x250")
        frame = Frame(top)
        botframe = Frame(top)
        
        frame.grid()
        botframe.grid()
        label1 = Label(frame, text = "Your Word")
        label1.grid(row = 0, column = 0, padx =4, pady= 4 )

        label2 = Label(frame, text = "Shift number")
        label2.grid(row = 1, column = 0, padx=4, pady =4)

        entry1 = Entry(frame , width = 15)
        entry1.grid(row = 0, column = 1)
        entry2 = Entry(frame, width =15)
        entry2.grid(row = 1, column=1)


        plain = "abcdefghijklmnopqrstuvwxzy"
        shifted=""
        lists= []
        cryptlist=[]
        decryptlist=[]
    #had to put the shifted alphabet in a list to save it for the decrypt function
        

        def encrpyt1():
            try:
                sentence= str(entry1.get())
            except:
                pass
            try:
                shift= int(entry2.get())
            except ValueError:
                encrpytion.config(text = "You must enter a number")
                return
            
            splain = slice(shift)
            extra = plain[splain]
            shifted = plain[shift:26] + extra
            #print ("this is your encrpyted alphabet: ",shifted)
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
            encrpytion.config(text=str(encrptyed))
                
        def decrypt1():
        #slice it back
            try:
                sentence= str(entry1.get())
            except:
                pass
            try:
                shift= int(entry2.get())
            except ValueError:
                pass
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
            decryption.config(text = str(decrypted))

        buttonencrypt = Button(frame, text= "encrypt", command = encrpyt1)
        buttonencrypt.grid(column = 0, row = 2)
        buttondecrpty = Button(frame, text = "decrypt", command= decrypt1)
        buttondecrpty.grid(column = 0, row = 3)

        encrpytion = Label(frame , text="")
        encrpytion.grid(row = 2, column = 1, padx = 4,pady = 4)
        decryption = Label(frame, text="")
        decryption.grid(row = 3, column = 1, padx = 4,pady = 4)

        canvas= tkinter.Canvas(botframe, width = 200, height = 200)
        coord= 0,0,200,200
        arc = canvas.create_arc(coord, start=0, extent=70, fill="red")
        canvas.grid( row = 5)
        top.mainloop()

if __name__ == '__main__':
    encry = encrpty()
    encry.display()
