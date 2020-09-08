import mysql.connector
from datetime import datetime,date

MYDB_CONNECTION = mysql.connector.connect(
    host = "localhost",
    user = "Anshuman",
    passwd = "Anshuman@10",
    database = "testDB"
)

mycurser = MYDB_CONNECTION.cursor()

STATUS = True

# mycurser.execute("CREATE DATABASE testDB")

# mycurser.execute("SHOW DATABASES")

# for db in mycurser:
#     print(db)

# mycurser.execute("CREATE TABLE user_test (name VARCHAR(30), DOB DATE, gender VARCHAR(10),skills VARCHAR(20),hobbies VARCHAR(20))")


# mycurser.execute("SHOW TABLES")
# for tb in mycurser:
#     print(tb)


''' All the functions for performing CRUD operation'''

def stopOperation():
    return False

def addUser(name,dob,gender,skills,hobbies):
    if('' in [name,dateofbirth,gender,skills,hobbies]):
        print("Please fill all the data")
    else:
        dataTOBeInsterted = "INSERT INTO user_test (name, DOB, gender, skills, hobbies) VALUES (%s,%s,%s,%s,%s)"
        userRecord = (name,dob,gender,skills,hobbies)
        mycurser.execute(dataTOBeInsterted, userRecord)
        MYDB_CONNECTION.commit()
        print("User Registred.....")

def showData(name):
    showAllData = "SELECT * FROM user_test WHERE name = %s"   
    try:

        mycurser.execute(showAllData,(name,))
        userData = mycurser.fetchone()
        labels = ["Name","DOB","Gender","Skills","Hobbies"]
        
        for data in range(len(userData)):
            print(labels[data],":",userData[data])
        
        today = date.today()
        print("Age:",today.year-userData[1].year - ((today.month, today.day) < (userData[1].month, userData[1].day)))
    
    except:
        print("User not Registered")
    
        

def updateUser(name,uname,dateofbirth,gender,skills,hobbies):
    try:
        updateUserData = "UPDATE user_test SET name=%s,DOB=%s,gender=%s,skills=%s,hobbies=%s WHERE name=%s"
        updateData = (uname,dateofbirth,gender,skills,hobbies,name)
        mycurser.execute(updateUserData,updateData)
        MYDB_CONNECTION.commit()
        print("User Data Updated")

    except:
        print("Some error Occured Please try again...")
    
def removeUser(name):
    
    try:
        removeUserData = "DELETE FROM user_test WHERE name = %s"
        mycurser.execute(removeUserData,(name,))
        MYDB_CONNECTION.commit()
        print("User Removed")

    except:
        print("Some Error Occured please try again")

  
    
#Converts the date which is in String format to Date
def dateConvert(dob):
    
    dob = str(dob)
    try:
        formatstr = '%Y-%m-%d'
        return datetime.strptime(dob,formatstr).date()
    except:
        print("Please Enter Date in Year-Month-Day Format by going to update User Data")


if __name__ == "__main__":
  # Menu of the CRUD OPERATION
    while(STATUS):
        
        print("-------------------Welcome----------------------")
        print("\n")
        print("1. Add User")
        print("2. Show User Details")
        print("3. Update User Data")
        print("4. Remove User")
        print("5. EXIT")

        choice = eval(input("Please Enter your choice:"))
        if(choice==1):
            name = input("Enter UserName:")
            dob = input("Enter Date of Birth(YYYY-MM-DD):")
            dateofbirth = dateConvert(dob) 
            gender = input("Enter gender:")
            skills = input("Enter your skills:")
            hobbies = input("Enter your hobbies:")
            addUser(name,dateofbirth,gender,skills,hobbies)
            
        
        elif (choice == 2):
            name = input("Enter UserName:")
            showData(name)

        elif (choice == 3):
            name = input("Enter UserName:")
            print("Enter the data it will be updated")
            uname = input("Enter UserName:")
            dob = input("Enter Date of Birth(YYYY-MM-DD):")
            dateofbirth = dateConvert(dob) 
            gender = input("Enter gender:")
            skills = input("Enter your skills:")
            hobbies = input("Enter your hobbies:")
            updateUser(name,uname,dateofbirth,gender,skills,hobbies)
            

        elif (choice ==4):
            name = input("Enter UserName:")
            removeUser(name)
            

        elif (choice == 5):
            print("-------------------Thank You----------------------")
            STATUS = stopOperation()
            