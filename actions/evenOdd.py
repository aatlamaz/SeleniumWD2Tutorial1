import shutil

myList = [1,2,3]

myFile = open("ahmet.txt", "w")

for item in myList:
    myFile.write(str(item))

myFile.close()


shutil.copy("/Users/ahmetatlamaz/PycharmProjects/SeleniumWD2Tutorial/actions/ahmet.txt", "/Users/ahmetatlamaz/PycharmProjects/SeleniumWD2Tutorial/base/ahmet.txt")






