import sys
import time

id = input("ENTER YOUR ID \n")
while True :
    if not id.isdigit() :
        id = input("PLEASE ENTER A VALID ID \n")

    elif int(id) == 55:
        file2 = open(r"C:\Intel\MyFile2.txt", "w+")
        file2.write(str(id))
        file2.close()

        # file2 = open(r"C:\Intel\MyFile2.txt", "r")
        # print(file2.read())
        # print()
        # file2.close()
        print("REGISTERATION DONE !")
        time.sleep(3)
        break
    elif int(id) != 55 :
        id = input("PLEASE ENTER A VALID ID \n")
