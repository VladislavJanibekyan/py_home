import os
print("begining:", os.getcwd())
os.mkdir("Dir1")
os.chdir("Dir1")
path = os.getcwd()
os.mkdir("Dir2")
os.mkdir("Dir3")
os.chdir("Dir3")
os.mkdir("Dir4")
os.chdir("Dir4")
path_end = os.getcwd()
print(path_end)
path_end.split("/")
user_choice = input("which directory or file do you want to delete? ")

while user_choice == "yes" and os.getcwd() != path:
    for i in path_end[::-1]:
        if not os.listdir(): 
            try:
                os.rmdir()
            except:
                os.chdir("..")
        else:
            print(os.listdir())
            for item in os.listdir():
                print(item)
                if os.path.isdir(item):
                    os.rmdir(item)
                elif os.path.isfile(item) and item == "test.rtf":
                    os.remove(item)
                    break
                    
