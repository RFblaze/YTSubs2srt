# YTSubs2srt
###### Yes, I know the name is weird (I've never been good at naming projects)
#
## What is this for?
When you are watching a youtube video, you can enable the transcript to play alongside the video. You can then copy the transcript and save into a text document. This program is meant to take that txt file as input, format its text into valid srt (SubRip Subtitle file) syntax, and save it into a new txt file with the word "_new" appended to the original file name.

## Instructions
- The program requires you to select the file you want to format. Ensure that the file in question is in the txt format as docx or other file formats won't work. 
- If all goes well, the program should terminate when done.
- There is both a Python file and an executable .exe file in the output directory. The executable was made using auto-py-to-exe so as to not require python being installed the computer that runs it.

## A few comments
- This program has been tested on Python 3.9.7
- There are no external libraries that are needed.
- This program has not been tested with videos that are an hour or longer and as such might not work properly with those transcripts.
- The executable might not always be up to date with the Python file (I might forget to remake the executable after the Python file is changed).

## Issues
1. For the moment, this program does not distinguish the difference between actual timestamps where the subtitles occur and time in sentences. For example:

> 4:00

> Is the current time 2:47pm, Harry? Dumbledore asked calmly.

&nbsp;&nbsp;&nbsp;&nbsp;In this case, the program will recognize both 4:00 and 2:47 as timestamps and will format it accordingly (which will not result in valid   srt syntax). This issue will be resolved eventually

2. The exported filename is not exactly correct. It appends the "_new" at the end of the .txt file extension when it should be before. For example: When "my_first_file.txt" is selected by the program, the new file is named "my_first_file.txt_new.txt" when it should be "my_first_file_new.txt".
