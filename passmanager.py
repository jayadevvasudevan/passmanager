dbase = "passmanager"
dhost = "localhost"
duser = input("Enter user name of data base: ")
dpass = input("enter password: ")
ch = "y"
import psycopg2
import random
import string

def get_random_password():
    random_source = string.ascii_letters + string.digits + string.punctuation
    pas = random.choice(string.ascii_lowercase)
    pas += random.choice(string.ascii_uppercase)
    pas += random.choice(string.digits)
    pas += random.choice(string.punctuation)

    for i in range(6):
        pas += random.choice(random_source)

    password_list = list(pas)
    random.SystemRandom().shuffle(password_list)
    pas = ''.join(password_list)
    return pas
try:
    conn = psycopg2.connect(dbname = dbase,user = duser,password = dpass,host = dhost )
    cur = conn.cursor()
    c = int(input('''1 : Add password
2: view All passwords 
3:view specific site
enter an option: '''))
    if c == 1:
        while ch =="y":
            sitename = input("Enter name of the site: ")
            uid  = input("Enter user id: ")
            chh = input("do you wanna generate a password for "+sitename+" ? : ")
            if chh == 'y':
                p = get_random_password()
            else:
                p = input("Enter password for the site "+ sitename + ": ")
            email = input("Enter email for the the site " + sitename + ": ")
            cur.execute("insert into pass values (%s,%s,%s,%s)",(sitename,uid,p,email,))
            conn.commit()
            ch  = input("want to enter more values? y/n: ")
    elif c == 2: 
        cur.execute("select * from pass;")
        rows = cur.fetchall()
        for row in rows:
            print("website = ", row[0])
            print("username = ", row[1])
            print("password = ", row[2])
            print("email = ", row[3], "\n")
        conn.commit()
    elif c == 3:
        site = input("Enter a site to find the password: ")
        cur.execute("select *  from pass ;")  
        passs = cur.fetchall()
        for p in passs:
            if site == p[0]:
                print("password is: "+str(p[2]))
                found = 1
        if found != 1: 
            print("password not found :  ")          
        conn.commit()
    else:
        print("invalid option:")
        print("exiting the manager..")
    conn.close()
except:
    print("!!!!invalid password or username!!!!")
