import datetime

def check_changes(driver):
    print("previous saved transcript detected!")          
    # read the file for comparing
    saved = open("saved", "r").read().split("\n")
    i = 0
    body = ""
    print ("Comparing to the previous transcript......")
    for course in driver.find_elements_by_class_name("courses"):
        if course.text != saved[i].strip():
            string = "Before: " + saved[i].strip() + "\n" + "Now: " + course.text
            print(string)
            body+=string
        i+=1
    if len(body)==0:
        print(">>> No changes found")
    else:
        make_new_file(driver)
    return body
    
def make_new_file(driver):
    # make a file to save the grades
    body = ""
    f = open('saved', 'w')
    print ("Updating the existing transcript......")
    print("*************************************** ACORN Transcript ***************************************")
    for course in driver.find_elements_by_class_name("courses"):
        string = course.text+"\n"
        f.write(string)
        body+=string
        print(course.text)
    f.close()
    print("******************************************************************************************")
    print("ACORN transcript saved!")
    return body

def update_file(update,driver):
    
    print ("Logged in at: " + str(datetime.datetime.now()))
    if update == False:
        body = make_new_file(driver) 
    else:
        body = check_changes(driver)
        if len(body)==0:
            update = False
    return (update,body)
