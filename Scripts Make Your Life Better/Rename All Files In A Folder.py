import os

#Destination Folder
folder = ""             #Example: ./Image
#New File's Extension
file_ext = ".png"       #Example: .png
#New File's Name
name = ""               #Example: Artwork

cnt = 0
list = os.listdir(folder)

for file_name in list:
    cnt += 1
    #Format of new name
    new_name = f"{name}_{str(cnt)}{file_ext}"
    #Example: Artwork_1.png
    path = os.path.join(folder, file_name)
    new_path = os.path.join(folder, new_name)
    os.rename(path, new_path)
    print(f"Renamed {file_name} to {new_name}")