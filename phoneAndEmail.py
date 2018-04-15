#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard

import pyperclip, re #imports copy and paste, and all that regex stuff

# Phone regex:
phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code, It is looking for 3 digits, or 3 digits in parentheses. The "\(" tells it that the parens should be looked for, rather than used in code. Optional.
    (\s|-|\.)?                      # separator, it looks for spaces, dots, or dashes. Optional
    (\d{3})                         # first three digits. It looks for three digits
    (\s|-|\.)                       # separator, it looks for spaces, dots, or dashes.
    (\d{4})                         # last four digits
    (\s*(ext|x|ext/)\s*(\d{2,5}))?  # extension, it looks for a space, then however many spaces there are, then "ext", "x", or "ext.", then it looks for the number of the extension, which has 2-5 digits. Optional.
    )''', re.VERBOSE)               #ends multiline string, allows you to comment at end of each line.

# Email regex:
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+              #username, which can be made up of any characters in the alphabet (capitalized or not), any digit, periods, underscores, percentage signs, plus signs, periods, and dashes.
    @                               # @ symbol. 
    [a-zA-Z0-9.-]+                  # domain name
    (\.[a-zA-Z]{2,4})              # .com, .org, etc.
    )''', re.VERBOSE)

# Find all matches in clipboard text (and format them too)
text = str(pyperclip.paste())       # Sets variable "textas" equal to the string of whatever is on the clipboard. I think.
matches = []                        # Sets list "matches" equal to nothing, I guess.
for groups in phoneRegex.findall(text): # For every group there is in the phone number found, do whatever comes next.
    phoneNum = '-'.join([groups[1],groups[3],groups[5]]) #joins all the groups of numbers in phone numbers with dashes. Excludes the separator groups.
    if groups[8] != '':             # if group 8 (the extension) is not equal to nothing
        phoneNum += ' x' + groups[8] # adds x in front of extension's number
    matches.append(phoneNum)        # adds extension to phone number
for groups in emailRegex.findall(text):
    matches.append(groups[0])       # adds the emails to group zero. 

# Copy results to clipboard (and join them too):
if len(matches) > 0:                # If you have at least one match
    pyperclip.copy('\n'.join(matches)) #Copies a new line, and a joined version of the list matches)
    print('copied to clipboard:')
    print('\n'.join(matches))       # Prints all the phone numbers found
else:                               # If there are no matches
    print("There are no phone numbers or emails. ")
                
