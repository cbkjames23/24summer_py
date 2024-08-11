import sqlite3
def opendb():
    conn = sqlite3.connect("D:\mydb.db")
    conn.execute("""CREATE TABLE IF NOT EXISTS tongxinlu (
                       usernum INTEGER PRIMARY KEY, 
                       username VARCHAR(128), 
                       password VARCHAR(128), 
                       address VARCHAR(128), 
                       telnum VARCHAR(128)
                   )""")
    return conn

def showalldb():
    print("--------------------处理后的数据--------------------")
    hel = opendb()
    cur = hel.cursor()
    cur.execute("select * from tongxinlu")
    res = cur.fetchall()
    for line in res:
        print("usernum:{}, username:{}, password:{}, address:{}, telnum:{}".format(line[0], line[1], line[2], line[3], line[4]))
    cur.close()
    
def into():
    usernum = input("请输入学号：")
    username = input("请输入姓名：")
    password = input("请输入密码：")
    address = input("请输入地址：")
    telnum = input("请输入联系电话：")
    return usernum, username, password, address, telnum

def adddb():
    print("--------------------欢迎使用添加数据功能--------------------")
    person = into()
    hel = opendb()
    hel.execute("insert into tongxinlu(usernum, username, password, address, telnum)values(?,?,?,?,?)",
                    (person[0], person[1], person[2], person[3], person[4]))
    hel.commit()
    print("--------------------恭喜你，数据添加成功--------------------")
    showalldb()
    hel.close()
    
def deldb():
    print("--------------------欢迎使用删除数据功能--------------------")
    delchoice = input("请输入你想要删除的学号：")
    hel = opendb()
    hel.execute("delete from tongxinlu where usernum = " + delchoice)
    hel.commit()
    showalldb()
    hel.close()
    
def alter():
    print("--------------------欢迎使用修改数据功能--------------------")
    changechoice = input("请输入你要修改的学生的学号：")
    hel = opendb()
    person = into()
    hel.execute("update tongxinlu set usernum = ?, username = ?, password = ?, address = ?, telnum = ? where usernum = " + changechoice,
                   (person[0], person[1], person[2], person[3], person[4]))
    hel.commit()
    showalldb()
    hel.close()

def searchdb():
    print("--------------------欢迎使用查找数据功能--------------------")
    serchoice = input("请输入你要查询的学生的学号：")
    hel = opendb()
    cur = hel.cursor()
    cur.execute("select * from tongxinlu where usernum = " + serchoice)
    hel.commit()
    print("--------------------查找成功，您所查找的数据如下--------------------")
    for person in cur:
        print(person[0], person[1], person[2], person[3], person[4])
    cur.close()
    hel.close()
 
def conti(a):
    choice = input("是否选择继续？(y/n)")
    if choice == 'y':
        a = 1
    else:
        a = 0

if __name__ == "__main__":
    flag = 1
    while flag:
        print("--------------------欢迎使用数据库--------------------")
        choiceshow = """
请选择您的操作：
a.向数据库中添加某些内容
b.删除数据库中的某些内容
c.修改数据库中的某写内容
d.查询数据库中的某些内容
请选择您的操作："""
        choice = input(choiceshow)
        if choice == 'a':
            adddb()
            conti(flag)
        elif choice == 'b':
            deldb()
            conti(flag)
        elif choice == 'c':
            alter()
            conti(flag)
        elif choice == 'd':
            searchdb()
            conti(flag)
        else:
            print("你的输入有误，请重新输入")