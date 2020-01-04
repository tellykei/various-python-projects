

class MyDocument(object):
    def __init__(self,txtpath="E:\\Users\\taliy\\Documents\\School pro\\python\\lessons\\file1.txt"):
        self.txtpath = txtpath
        try:
            self.txtpath=open(self.txtpath).read()
        except(FileNotFoundError, IOError):
            print("wrong path was detected or filedoes not exist: " + self.txtpath)
        


        
    def __str__(self): 
        return self.txtpath

    def  __repr__(self):
        return self.__str__()

    def __add__(self,txtpath2):
        newfile = open("file3.txt","r+")
        results = self.txtpath + txtpath2.txtpath
        newfile.write(results)
        return newfile.read()

mydoc= MyDocument()
mydoc2 = MyDocument("E:\\Users\\taliy\\Documents\\School pro\\python\\lessons\\file2.txt")
mydoc3=MyDocument("E:fakefolder")
print(mydoc)
print(mydoc2.__str__())
print(mydoc.__add__(mydoc2))
'''
wrong path was detected or filedoes not exist: E:fakefolder
hi
there
you

hi2
there2
you2p

hi
there
you
hi2
there2
you2p
'''
