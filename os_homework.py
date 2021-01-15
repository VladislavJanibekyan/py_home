import os
print("begining:", os.getcwd())
path = os.getcwd()
os.mkdir("Dir1")
os.chdir("Dir1")
os.mkdir("Dir2")
os.mkdir("Dir3")
os.chdir("Dir3")
os.mkdir("Dir4")
path_end = os.getcwd()
print(path_end)
path_list = path_end.split("/")
user_choice = input("do you want to delete all new created directories and test.rtf file? ")

while user_choice == "yes" and os.getcwd() != path:
    for i in path_list[:-4:-1]:
        if not os.listdir(): 
            try:
                os.rmdir()
            except:
                os.chdir("..")
        else:
            for item in os.listdir():
                if os.path.isdir(item) and item == "Dir1" or item == "Dir2" or item == "Dir3" or item == "Dir4":
                    os.rmdir(item)
                elif os.path.isfile(item) and item == "test.rtf":
                    os.remove(item)
                
                    
