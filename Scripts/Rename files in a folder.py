import os
import time

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

def Job(folder, name, log):
    list = os.listdir(folder)
    cnt = 0
    check = 1
    time_start = time.time()
    for file_name in list:
        time_end = time.time()
        time_execution = round(time_end - time_start, 3)
        cnt += 1
        file_ext = file_name[-4:]
        new_name = f"{name} {str(cnt)}{file_ext}"
        path = os.path.join(folder, file_name)
        new_path = os.path.join(folder, new_name)
        os.rename(path, new_path)
        log_print = f"Renamed {file_name} to {new_name}"
        if (log == True):
            with open("log.txt", "a") as file_log:
                file_log.write(f"{log_print}\n")
            if (time_execution > check):
                check += 1
                print(f"{colors.OKGREEN}Number of files renamed successfully: {colors.OKCYAN}{cnt}.")
        else:
            print(f"{log_print}\n")
    return cnt

line = ["Path to the folder which contains the files\n(can be a folder name if this script is in the same folder as the folder destination): ",
"What do you want to be your new file name? ",
"Do you want to save log into a file?\n(If no, then it will be printed on the terminal)\nY for Yes/N for No: "]
folder_path = ""
file_name = ""
cnt = 0
log = False

for i in line:
    print(f"{colors.HEADER}{i}{colors.ENDC}", end = "")
    error = True
    cnt += 1
    if (cnt == 1):
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
    if (cnt == 2):
        check = False
        print_check = True
        file_name = input()
        while (check == False):
            if (print_check == False):
                print(f"{colors.HEADER}{i}{colors.ENDC}", end = "")
                file_name = input()
            print(f"{colors.WARNING}Are you sure your new file name to be: {colors.ENDC}{file_name}{colors.WARNING}?{colors.ENDC}")
            print(f"{colors.WARNING}Y for Yes/N for No: {colors.ENDC}", end = "")
            answer = input()
            while (answer != "Y" and answer != "N" and answer != "y" and answer != "n"):
                print(f"{colors.WARNING}Wrong format, please follow the format: Y for Yes/N for No: {colors.ENDC}", end = "")
                answer = input()
            if (answer.lower() == "y"):
                check = True
            else:
                print_check = False
    if (cnt == 3):
        answer = input()
        while (answer != "Y" and answer != "N" and answer != "y" and answer != "n"):
            print(f"{colors.WARNING}Wrong format, please follow the format: Y for Yes/N for No: {colors.ENDC}", end = "")
            answer = input()
        if (answer.lower() == "y"):
            log = True
        else:
            log = False

#print(f"{folder_path}\n{file_name}\n{log}")

cnt = Job(folder_path, file_name, log)

time_end = time.time()
time_execution = time_end - time_start
hours = int(time_execution // 3600)
minutes = int((time_execution % 3600) // 60)
seconds = round((time_execution % 3600) % 60, 3)

print(f"{colors.OKGREEN}Time executed: {colors.HEADER}{hours}hrs, {minutes}mins, {seconds}secs.")