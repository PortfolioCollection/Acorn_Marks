def read_credentials():
    # read config file
    student_number, pin, gmail_address, gmail_password, to_address = "","","","",""

    login = open("config.txt", "r").read().split("\n")

    for line in login:
        if line.startswith('UTORID'):
            student_number = line[line.find("=") + 1:]
        if line.startswith('password'):
            pin = line[line.find("=") + 1:]
        if line.startswith('your_gmail_address'):
            gmail_address = line[line.find("=") + 1:]
        if line.startswith('your_gmail_password'):
            gmail_password = line[line.find("=") + 1:]
        if line.startswith('to_email_address'):
            to_address = line[line.find("=") + 1:]
    return (student_number, pin, gmail_address, gmail_password, to_address)
