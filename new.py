import re
from tkinter.filedialog import askopenfilename
from tkinter import Tk

'''
This is a surprise tool that might help us later:
pip install googletrans
'''

# This makes it so the empty root window is hidden
root = Tk()
root.withdraw()

# This makes the file select window always show up on top
root.attributes("-topmost", True)

def process_file(file_path):

    # Opens the file
    # lines is an array that contains every line of the text file
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()


    for i in range(len(lines)):
        # Search for "mm:ss" at line
        match2 = re.search(r'\d{2}:\d{2}', lines[i])

        # Search for " mm:ss" at line 
        matchspace2 = re.search(r'\s\d{2}:\d{2}', lines[i])

        # Search for " m:ss" at line
        matchspace1 = re.search(r'\s\d{1}:\d{2}', lines[i])
        
        # These bottom two conditions just remove the space before the timestamps
        if matchspace2:
            timestamp = matchspace2.group(0)
            lines[i] = lines[i].replace(timestamp, timestamp.strip())

        if matchspace1:
            timestamp = matchspace1.group(0)
            lines[i] = lines[i].replace(timestamp, timestamp.strip())

        # If a "mm:ss" timestamp was found at line[i], do this.
        '''This must be checked first because "m:ss" still counts as "mm:ss"'''
        if match2:
            # Changes "mm:ss" to "h:mm:ss,"" in lines[i]
            timestamp = match2.group(0)
            lines[i] = lines[i].replace(timestamp, "0:" + timestamp + ',')

            # Checks the next lines to find the ending timestamp
            for j in range(i + 1, len(lines)):
                # Looks for "mm:ss" in the next lines
                match2 = re.search(r'\d{2}:\d{2}', lines[j])
                if match2:
                    # Changes "h:mm:ss," to "h:mm:ss,ending timestamp"
                    next_timestamp = match2.group(0)
                    lines[i] = lines[i].replace(timestamp + ',', timestamp + ',' + next_timestamp)
                    
                    # Changes "h:mm:ss,ending timestamp" to "h:mm:ss,h:ending timestamp"
                    end_timestamp = match2.group(0)
                    lines[i] = lines[i].replace(end_timestamp, '0:' + end_timestamp)
                    break 
        
        # This would execute if a "mm:ss" was not found 
        else:
            # Looks for "m:ss" in lines[i]
            match1 = re.search(r'\d{1}:\d{2}', lines[i])

            # If "m:ss" was found, do this. Else, it's a text line so insert newline character 
            # at the end of it for srt formatting purposes.
            if match1:
                # Changes "m:ss" to "h:mm:ss,"
                timestamp = match1.group(0)
                lines[i] = lines[i].replace(timestamp, "0:0" + timestamp + ',')

                # Checks the next lines to find the ending timestamp
                for j in range(i + 1, len(lines)):
                    # Checks if the ending timestamp is "m:ss" or "mm:ss"
                    match1coma = re.search(r'\d{1}:\d{2}', lines[j])
                    match1 = re.search(r'\d{1}:\d{2}', lines[j])
                    match2 = re.search(r'\d{2}:\d{2}', lines[j])

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
    
'''
Code starts execution here
'''
while True:
    # User chooses text file
    file_path = askopenfilename()

    # If none was chosen, terminate program
    if file_path == '':
        break

    # Try to format & save as new file. Else, program terminates
    try:
        process_file(file_path)
        break
    except:
        print("File not found")

 




