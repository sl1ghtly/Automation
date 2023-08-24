import openpyxl
from pathlib import Path
import smtplib, ssl
from email.message import EmailMessage
# declare arrays to store emails and the dues and their indexes
emails = []
may_dues = []
nums = []
# set path of the xlsx file, change the path if program elsewhere
list_file = Path('I:\Year 2\Semester 4\Automation\Scripts\CA2', 'task3list.xlsx')
# read from the excel file
excel_file = openpyxl.load_workbook(list_file)
# take the excel file into a variable 
sheet = excel_file.active
# add emails and the dues into an array
for row in sheet.rows:
    emails.append(row[3].value)
    may_dues.append(row[8].value)
# remove first 4 useless rows that are not needed
for x in range(3, -1, -1):
    emails.pop(x)
    may_dues.pop(x)
# remove last 2 useless rows (because of the line 18 and 19 added)
for x in range(0, 2):
    emails.pop()
    may_dues.pop()
# get index of None in may_dues
nums = [i for i in range(len(may_dues)) if may_dues[i] == None]
# declare receivers
receivers = []
# add receivers
for i in range(len(nums)):
    receivers.append(emails[nums[i]])
# send message loop to send as much is in receivers array
for i in range(len(nums)):
    message = EmailMessage()
    # set content, subject, from(login email) and to
    message.set_content("""
    This is an automated message.
    You have not paid your dues yet.
    Please do so.

    Thank you for reading this message!
    """)
    message['Subject'] = 'Dues Not Paid!'
    # change this to your login email, used below to login
    message['From'] = 'l00157413@gmail.com'
    message['To'] = emails[nums[i]]
    # create ssl context
    context = ssl.create_default_context()
    # login into gmail account(THIS IS IMPORTANT: make sure that access for less secure apps
    # is turned off using this link: https://myaccount.google.com/lesssecureapps )
    with smtplib.SMTP('smtp.gmail.com', port = 587) as smtp:
        smtp.starttls(context = context)
        # login(change the !ZAQ!2wsx to your own password, google recommended)
        smtp.login(message['From'], '!ZAQ!2wsx')
        # finally send message
        smtp.send_message(message)