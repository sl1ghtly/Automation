import time

# IMPORTANT: MAKE SURE THAT YOU ARE IN THE DIRECTORY
# "I:\Year 2\Semester 4\Automation\Scripts\CA1" 
# USE THE EXAMPLE COMMANDS BELOW
# I:
# cd I:\Year 2\Semester 4\Automation\Scripts\CA1
# IF USING A DIFFERENT PATH, PLEASE ADJUST SO NO ERRORS

# PART 1 METHOD
def password_check(password):
    # declare instantly true and change it if something is not present
    val = True
    # if any letter is a digit
    if not any(letter.isdigit() for letter in password):
        val = False
        print("No Numbers in password! ")
    # if any letter is an upper character
    if not any(letter.isupper() for letter in password):
        val = False
        print("No Capital Letters in password! ")
    # if any letter is a special character
    if not any(not letter.isalnum() for letter in password):
        val = False
        print("No Symbols in password! ")
    # return boolean value
    return val

# PART 1
# ask for whatever required
fname = input(">Enter your first name: ")
lname = input(">Enter your last name: ")
username = input(">Enter your username: ")
emailID = input(">Enter email ID: ")
pw = input(">Input password: ")

# while loop to check if password is good enough
while (password_check(pw) != True):
    pw = input(">Input password: ")
# save password into txt file with username on a brand new line
with open("data.txt", "a+") as f:
    #create password string and then append it to file
    text = fname + "," + lname + "," + emailID + "," + username + "," + pw + "\n"
    f.write(text)

# PART 2
# declare attempts variable, ask for login and declare lines list/array
attempts = 3
loginName = input(">Enter your Login: ")
lines = []

# open data.txt in read only format
with open("data.txt", "r") as f:
    # take each line without newline character into lines list/array
    lines = [line.rstrip("\n") for line in f]

# for loop to check if the loginName is in lines list/array
for line in lines:
    # if it is, take that line as loginString
    if loginName in line:
        loginString = line

# split loginString into separate list/array
partsOfLoginData = loginString.split(",")
# and take last part of LoginData as it's the password
loginPassData = partsOfLoginData[4]

# while loop to loop over while attempts are not 0
while (attempts != 0):
    loginPassword = input (">Enter your Password: ")
    # if password matches, login successful and break out of the loop
    if loginPassData == loginPassword:
        print("Login Successful! ")
        break
    # if password doesn't match, login failed, decrement attempts
    else:
        print("Login Not Successful! ")
        attempts = attempts - 1
        # if attempts are 0, notify that user ran out of attempts
        if attempts == 0:
            print("You have run out of attempts! Wait for 2 minutes! ")
            # using time library, sleep for 120s and after that restore attempts to 3
            time.sleep(120)
            attempts = 3
