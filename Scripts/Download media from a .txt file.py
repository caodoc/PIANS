import os
import time
import urllib.request

time_start = time.time()

class colors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
# Colors source: https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

def Get(path, container, log):
    with open(path, "r") as file:
        list = file.read().splitlines()
    cnt = 0
    name = "Media"
    time_start = time.time()
    check = 1
    for link in list:
        name = "Media"
        time_end = time.time()
        time_execution = round(time_end - time_start, 3)
        try:
            cnt += 1
            if ("_n.jpg" in link):
                name += f" {str(cnt)}.jpg"
            if ("_n.mp4" in link):
                name += f" {str(cnt)}.mp4"
            download_path = os.path.join(container, name)
            urllib.request.urlretrieve(link, download_path)
            log_1 = f"Downloaded: {link}"
            log_2 = f"Number of media downloaded successfully: {cnt}."
            if (log == True):
                with open("log.txt", "a") as file_log:
                    file_log.write(f"{log_1}\n{log_2}\n")
                if (time_execution > check):
                    check += 1
                    print(f"{colors.OKGREEN}Number of media downloaded successfully: {colors.OKCYAN}{cnt}.")
            else:
                print(log_1)
                print(log_2)
        except Exception as e:
            log_3 = f"Failed to download: {link}"
            log_4 = f"Error: {str(e)}."
            if (log == True):
                with open("log.txt", "a") as file_log:
                    file_log.write(f"{log_3}\n{log_4}\n")
            else:
                print(log_3)
                print(log_4)
    return cnt

line = ["Location of your .txt file\n(can be a file name if this script is in the same folder as the .txt file): ",
"Destination for the media\n(can be a folder name if this script is in the same folder as the folder destination): ",
"Do you want to save log into a file?\n(If no, then it will be printed on the terminal)\nY for Yes/N for No: "]
file_path = ""
folder_path = ""
log = True
file_name = ""
cnt = 0

for i in line:
    print(f"{colors.HEADER}{i}{colors.ENDC}", end = "")
    cnt += 1
    error = True
    if (cnt == 1):
        file_path = input()
        if (".txt" not in file_path):
            file_path += ".txt"
        try:
            with open(file_path, "r") as file:
                error = False
        except FileNotFoundError:
            error = True
        while (error == True):
            print(f"{colors.WARNING}Error: File not found\nPlease re-submit file path: {colors.ENDC}", end = "")
            file_path = input()
            if (".txt" not in file_path):
                file_path += ".txt"
            try:
                with open(file_path, "r") as file:
                    error = False
            except FileNotFoundError:
                error = True
    if (cnt == 2):
        folder_path = input()
        try:
            os.listdir(folder_path)
            error = False
        except FileNotFoundError:
            error = True
        while (error == True):
            print(f"{colors.WARNING}Error: Folder not found\nPlease re-submit folder path: {colors.ENDC}", end = "")
            folder_path = input()
            try:
                os.listdir(folder_path)
                error = False
            except FileNotFoundError:
                error = True
    if (cnt == 3):
        answer = input()
        while (answer != "Y" and answer != "N" and answer != "y" and answer != "n"):
            print(f"{colors.WARNING}Wrong format, please follow the format: Y for Yes/N for No: {colors.ENDC}", end = "")
            answer = input()
        if (answer.lower() == "y"):
            log = True
        else:
            log = False

#print(f"{file_path}\n{folder_path}\n{log}\n")

cnt = Get(file_path, folder_path, log)

print(f"{colors.OKGREEN}Total of media downloaded successfully: {colors.OKCYAN}{cnt}.")

time_end = time.time()
time_execution = time_end - time_start
hours = int(time_execution // 3600)
minutes = int((time_execution % 3600) // 60)
seconds = round((time_execution % 3600) % 60, 3)

print(f"{colors.OKGREEN}Time executed: {colors.HEADER}{hours}hrs, {minutes}mins, {seconds}secs.")