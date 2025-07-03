# Importing libraries  
import mysql.connector   # for database connection  
import time # for time effect  
import sys  
  
print("-"*80)  
print("\t\t\tVISITOR IDENTITY")  
print("-"*80)  
  
# Function to add user's data into database  
def add_user():  
    # Establishing connection to database  
    mydb = mysql.connector.connect(  
        host='localhost',  
        user='root',  
        password='123456',  
        db='visitor'  
    )  
  
    print()  
    print("Fill out the details below")  
    print()  
    n = input("Enter your name here: ")  
    o = input("Enter your occupation here: ")  
    a = input("Enter your address here: ")  
    p = input("Enter a password here: ")  
  
    mycursor = mydb.cursor()  
  
    sql = "INSERT INTO visitortab (name, occupation, address, entrypass) VALUES (%s, %s, %s, %s)"  
  
    val = (n, o, a, p)  
  
    mycursor.execute(sql, val)  
  
    mydb.commit()  
  
    mydb.close()  
  
    print()  
    print("Your data has been successfully added :)")  
    print("You are allowed to enter")  
    print()  
    home_func()  
  
# Function: Those users who are identified  
def user_menu():  
    try:  
        print()  
        user_pass = input("Enter your password here: ")  
        user_pass2 = user_pass  
        user_pass = (user_pass,)  
  
        mydb = mysql.connector.connect(  
            host='localhost',  
            user='root',  
            password='123456',  
            db='visitor'  
        )  
  
        mycursor = mydb.cursor()  
  
  
        sql = "Select name from visitortab WHERE entrypass = %s"  
        mycursor.execute(sql, user_pass)  
        ans = mycursor.fetchall()  
        ans = ''.join(ans[0])  
  
        print("*" * 50)  
        print(f"Hey {ans}!")  
        print("A. Type '1' to check details")  
        print("B. Type '2' to modify data")  
        print("C. Type '3' to delete your account")  
        print("D. Type '4' to see all user's details")  
        print("E. Type '5' to return to main screen")  
        print()  
  
        what = ''  
        while what != '5':  
            print()  
            what = input("What do you want to do? ")  
            print()  
  
            if what == '1':  
                sql = "SELECT * FROM visitortab WHERE entrypass = %s"  
                mycursor.execute(sql, user_pass)  
                res = mycursor.fetchall()  
                print()  
                print(res)  
  
            elif what == '2':  
                print("""What do you want to modify:  
                n: Name  
                o: Occupation  
                a: Address  
                """)  
  
                user_mod = input("--> ").lower()  
                if user_mod == 'n':  
                    new_name = input("Enter new name here: ")  
                    sql = "UPDATE visitortab SET name=%s WHERE entrypass=%s"  
                    tup = (new_name, user_pass2)  
                    mycursor.execute(sql, tup)  
                    mydb.commit()  
  
                    print("Done! Your name has been changed")  
  
                elif user_mod == 'o':  
                    new_occupation = input("Enter your new occupation here: ")  
                    sql = "UPDATE visitortab SET occupation=%s WHERE entrypass=%s"  
                    tup = (new_occupation, user_pass2)  
                    mycursor.execute(sql, tup)  
                    mydb.commit()  
  
                    print("Done! Your occupation has been changed")  
  
                elif user_mod == 'a':  
                    new_address = input("Enter your new address here: ")  
                    sql = "UPDATE visitortab SET address=%s WHERE entrypass=%s"  
                    tup = (new_address, user_pass2)  
                    mycursor.execute(sql, tup)  
                    mydb.commit()  
  
                    print("Done! Your address has been changed")  
  
            elif what == '3':  
                sql = "DELETE FROM visitortab WHERE entrypass = %s"  
                mycursor.execute(sql, user_pass)  
                mydb.commit()  
  
                print()  
                print("Your account has been successfully deleted")  
                print()  
                home_func()  
  
            elif what == '4':  
                sql = "SELECT * FROM visitortab"  
                mycursor.execute(sql)  
                result = mycursor.fetchall()  
  
                for row in result:  
                    print(row)  
  
            elif what == '5':  
                print("-"*80)  
                home_func()  
  
            mydb.close()  
  
    except Exception as e:  
        print(e)  
        print("Invalid password or the user doesn't exist")  
        print("You are not allowed to enter")  
        print()  
        home_func()  
  
# Main function   
def home_func():  
    print("Hello there! Nice to meet you")  
    time.sleep(0.5)  
    print("If you are a new visitor please type 1 below else type 2")  
    time.sleep(0.5)  
    print("To quit type 'q' ")  
    print()  
    inp = input("Your answer: ")  
    if inp == "1":
        add_user()  
    if inp == "2":
        user_menu()  
    if inp == "q":
        sys.exit()  

home_func()