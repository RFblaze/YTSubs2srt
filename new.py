import re
from tkinter.filedialog import askopenfilename
from tkinter import Tk

root = Tk()
root.withdraw()
root.attributes("-topmost", True)
def process_file(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    for i in range(len(lines)):
        match2 = re.search(r'\d{2}:\d{2}', lines[i])
        matchspace2 = re.search(r'\s\d{2}:\d{2}', lines[i])
        matchspace1 = re.search(r'\s\d{1}:\d{2}', lines[i])
        
        if matchspace2:
            timestamp = matchspace2.group(0)
            lines[i] = lines[i].replace(timestamp, timestamp.strip())

        if matchspace1:
            timestamp = matchspace1.group(0)
            lines[i] = lines[i].replace(timestamp, timestamp.strip())

        if match2:
            timestamp = match2.group(0)
            lines[i] = lines[i].replace(timestamp, "0:" + timestamp + ',')

            for j in range(i + 1, len(lines)):
                match2 = re.search(r'\d{2}:\d{2}', lines[j])
                if match2:
                    next_timestamp = match2.group(0)
                    lines[i] = lines[i].replace(timestamp + ',', timestamp + ',' + next_timestamp)
                    
                    timestamp = match2.group(0)
                    lines[i] = lines[i].replace(timestamp, '0:' + timestamp)
                    break 
        
        else:
            match1 = re.search(r'\d{1}:\d{2}', lines[i])
            if match1:
                timestamp = match1.group(0)
                lines[i] = lines[i].replace(timestamp, "0:0" + timestamp + ',')

                for j in range(i + 1, len(lines)):
                    match1coma = re.search(r'\d{1}:\d{2}', lines[j])
                    match1 = re.search(r'\d{1}:\d{2}', lines[j])
                    match2 = match2 = re.search(r'\d{2}:\d{2}', lines[j])

                    if match2:
                        next_timestamp = match2.group(0)
                        lines[i] = lines[i].replace(timestamp + ',', timestamp + ',' + next_timestamp)
                        
                        timestamp = match2.group(0)
                        lines[i] = lines[i].replace(timestamp, '0:' + timestamp)

                    elif match1:
                        next_timestamp = match1.group(0)
                        lines[i] = lines[i].replace(timestamp + ',', timestamp + ',' + next_timestamp)

                        timestamp = match1.group(0)
                        lines[i] = lines[i].replace(timestamp, '0:0' + timestamp)
                        break
                    elif match1coma:
                        timestamp = match1coma.group(0)
                        lines[i] = lines[i].replace(timestamp, '0:0' + timestamp)
            else:
                lines[i] = lines[i].replace(lines[i], lines[i] + '\n')
                i += 1
            

    with open(f"{file_path}_new.txt", 'w', encoding="utf-8") as file:
        file.writelines(lines)
    

while True:
    file_path = askopenfilename()
    if file_path == '':
        break
    try:
        process_file(file_path)
        break
    except:
        print("File not found")

 




