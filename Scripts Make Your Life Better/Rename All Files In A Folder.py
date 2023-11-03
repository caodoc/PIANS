import os

folder = "./Hina"
file_ext = ".png"
name = "Hina"

cnt = 0
list = os.listdir(folder)

for file_name in list:
    #print(f"{file_name}\n")
    cnt += 1
    new_name = f"{name}_{str(cnt)}{file_ext}"
    #print(f"{new_name} \n")
    path = os.path.join(folder, file_name)
    new_path = os.path.join(folder, new_name)
    os.rename(path, new_path)
    print(f"Renamed {file_name} to {new_name}")