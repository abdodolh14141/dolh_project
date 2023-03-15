import sqlite3 # type: ignore
import sys
import numpy as np
import pylint.lint
import ascii_train
import pandas as pd
from pymongo import MongoClient
import pprint
db = sqlite3.connect("app.db")
cr = db.cursor()
cr = db.execute("select * from data_clint")
mongo_url = f'mongodb+srv://abdodolh14141:abdodolh14141@data.2n75kkb.mongodb.net/test'
clint = MongoClient(mongo_url) # type: ignore
abs = clint.list_database_names()
test_tryed = clint.tryed
colection = test_tryed.list_collection_names()
cl_1 = cr.fetchone()
cl_2 = cr.fetchone()
cl_3 = cr.fetchone()
cl_4 = cr.fetchone()
cl_5 = cr.fetchone()
cl_6 = cr.fetchone()
cl_7 = cr.fetchone()
cl_8 = cr.fetchone()
cl_9 = cr.fetchone()
cl_10 = cr.fetchone()
cl_11 = cr.fetchone()
cl_12 = cr.fetchone()
cl_13 = cr.fetchone()
frame_mongo = pd.DataFrame(people)
name_user = np.array([[cl_1[1],cl_2[1],cl_3[1],cl_4[1]],[cl_5[1],cl_6[1],cl_7[1],cl_8[1]],[cl_9[1],cl_10[1],cl_11[1],cl_12[1]]])
data_pass = [[cl_1[6],cl_2[6],cl_3[6],cl_4[6],cl_5[6]],[cl_6[6],cl_7[6],cl_8[6],cl_9[6],cl_10[6],cl_11[1],cl_12[1]]]
secart_password = np.array(["123456789","35651850","abdodolh14141"])
printer = pprint.PrettyPrinter()#to print all_data beatyprinter
production = clint.data_clint # type: ignore
data_clint = production.data_clint
class clint():
    def show_password(self):
        password_all = pd.DataFrame(data_pass)
        print(password_all)

    def rate_python(self):
        try:
            print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
            rate1 = ['project.py']
            pylint.lint.Run(rate1)
        except SyntaxError as er:
            print(f"error => {er}")
        finally:
            sys.exit()

    def copy_code(self):
        try:
            copy_file = open('project.py', "r")
            coping = copy_file.read()
            file_copy = open('E:\\skill_python\edit_extra.txt', "a")
            file_copy.write(coping)
        except TypeError as er:
            print(f"error => {er}")
        finally:
            copy_file.close
            file_copy.close
            print("sucess copy in text edit_extra".title())

    def calcalate(name):
        try:
            print(f"hello {name}")
            num1 = float(input("number =>"))
            opp = input("opp =>")
            num2 = float(input("number =>"))
            if opp == "+":
                answer = num1 + num2
                print(f"answer => {answer}")
            elif opp == "-":
                answer = num1 - num2
                print(f"answer => {answer}")
            elif opp == "*":
                answer = num1 * num2
                print(f"answer => {answer}")
            elif opp == "/":
                answer = num1 / num2
                print(f"answer => {answer}")
        except ValueError as ve:
            print(f"error => {ve}")
        finally:
            pass            
            
    def id_cl(name):
        print(f"hello {name}")
        input_id = input("name or user_id =>")

        if input_id == cl_1[1] or input_id == cl_1[0]:
            print(id(cl_1))

        elif input_id == cl_2[1] or input_id == cl_2[0]:
            print(id(cl_2))

        elif input_id == cl_3[1] or input_id == cl_3[0]:
            print(id(cl_3))

        elif input_id == cl_4[1] or input_id == cl_4[0]:
            print(id(cl_4))

        elif input_id == cl_5[1] or input_id == cl_5[0]:
            print(id(cl_5))

        elif input_id == cl_6[1] or input_id == cl_6[0]:
            print(id(cl_6))

        elif input_id == cl_7[1] or input_id == cl_7[0]:
            print(id(cl_7))

        elif input_id == cl_8[1] or input_id == cl_8[0]:
            print(id(cl_8))

        elif input_id == cl_9[1] or input_id == cl_9[0]:
            print(id(cl_9))

        elif input_id == cl_10[1] or input_id == cl_10[0]:
            print(id(cl_10))

        elif input_id == cl_11[1] or input_id == cl_11[0]:
            print(id(cl_11))

        elif input_id == cl_12[1] or input_id == cl_12[0]:
            print(id(cl_12))        

        else:
            print("i cant found it please put correct id".title())

class data_mongodb(clint):

    def insert_test_doc():
        collection = test_tryed.tryed
        text_doc = {
        }
        collection.insert_one(text_doc).inserted_id
        print(collection)

        
    def creat_table(): 
        data = []
        name = ['abdo dolh','adel soliman','esraa adel','ahmed omer',
                    'ziad yossif','omer adel','elon mark','elon mask','osama alzero']
        age = [32,45,20,22,25,19,33,50,29]
        married = [True,True,False,False,True,False,True,True,False]
        salary = [15000,12000,6000,8000,4800,3000,6200,11000,1800]
        country = ['canda','usa','iraq','france','german','egypt','india','german','soudia']
        password = ['abdo14141', 'adel14141', 'esraa14141', 'ahmed14141', 'ziad14141', 'omer14141', 'elon14141', 'elon14141', 'osama14141']
        skill = ['data anlysis','software engineer','cyber secirty','full-stack-frontend','php,js-express','mongo,react','cyber secuirty','machine learning','software engineer']
        
        for name,age,married,salary,country,password,skill in zip(name,age,married,salary,country,salary,skill):
            doc = {'name':name, 'age':age, 'married':married, 'salary':salary,
                    'country':country, 'password':password, 'skill':skill}
            data.append(doc)
        data_clint.insert_many(data)


    def reader_data():
        people = data_clint.find()
        for data in people:
            print(pd.DataFrame(people))

    def find(name):
        search = data_clint.find_one({'name':f'{name}'})
        printer.pprint(search)

    def get_id(person_id):
        from bson.objectid import ObjectId
        _id = ObjectId(person_id) # type: ignore
        person = data_clint.find_one({'_id':_id})
        printer.pprint(person)            

class data_base(clint):
    def database_all(self):
        try:
            cr = db.execute("select * from data_clint")
            all_data = pd.DataFrame(cr)
            print(all_data)
        except sqlite3.Error as er:
            print(f"reading => {er}")
        finally:
            print("*"*50)

    def anlysis_salary(name):   
        data = db.execute('select * from data_clint')
        frame = pd.DataFrame(data, columns=["user_id", "name", "age",
                                             "married", "salary", "country", "password", "genter", "skill"])
        print(f'please wait {name}')
        data_salary = frame['salary']
        return data_salary.describe()

    def anlysis_age(name):   
        data = db.execute('select * from data_clint')
        frame = pd.DataFrame(data, columns=["user_id", "name", "age", "married",
                               "salary", "country", "password", "genter", "skill"])
        print(f'please wait {name}')
        data_age = frame['age']
        return data_age.describe()

    def adit_cl(self):
        try:
            quision_base = input("whats are you edit: ")
            if quision_base == "name":
                id_user = input("user_id_user :".strip())
                new2 = input("new name :".strip())
                cr.execute(f"update data_clint set name = '{new2}' where user_id = {id_user}")

            elif quision_base == "age":
                id_user = input("user_id :".strip())
                new1 = input("new age :".strip())
                cr.execute(f"update data_clint set age = '{new1}' where user_id = {id_user}")

            elif quision_base == "salary":
                id_user = input("user_id :".strip())
                new1 = input("new salary :".strip())
                cr.execute(f"update data_clint set salary = '{new1}' where user_id = {id_user}")

            elif quision_base == "password":
                id_user = input("user_id :".strip())
                new1 = input("new password :".strip())
                cr.execute(f"update data_clint set password = '{new1}' where user_id = {id_user}")

            elif quision_base == "country":
                id_user = input("user_id :".strip())
                new1 = input("new country :".strip())
                cr.execute(f"update data_clint set country = '{new1}' where user_id = {id_user}")

            elif quision_base == "skill":
                id_user = int(input("user_id_user :".strip()))
                new_skill = input("new skill :".strip().title())
                cr.execute(f"update data_clint set skill = '{new_skill}' where user_id = {id_user}")

            elif quision_base == "id":
                id_change = input("old name :")
                new_id = int(input("new id :".strip()))
                cr.execute(f"update data_clint set user_id = {new_id} where name = '{id_change}'")
        except sqlite3.Error as er:
            print(f"Error => {er}")
        finally:
            db.commit()
            db.close()
            print("sucessful server is close")
            print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))

    def add_cl(self):
        try:
            new_user_id = input("id new to create => ")
            new_name1 = input("new name to creat => ")
            new_age = input("age =>")
            new_salary = input("salary =>")
            new_country = input("country =>")
            new_genter = input("genter =>")
            new_married = input("is_married =>")
            new_password = input("password =>")
            new_skill = input("new skill =>")
            cr = db.execute(f"insert into data_clint(user_id,name,age,married,salary,country,password,genter,skill) values({new_user_id},'{new_name1}', {new_age},'{new_married}', {new_salary},'{new_country}','{new_password}', '{new_genter}', '{new_skill}')")
        except sqlite3.Error as er:
            print(f"Error => {er}")
        finally:
            db.commit()
            db.close()
            print("sucessful server is close")
            print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))

    def delete_cl(self):
        try:
            id = input("id :".strip())
            cr = db.execute(f"delete from data_clint where user_id = {id}")
            print(f"succesfully delet")
        except sqlite3.Error as er:
            print(f"reading => {er}")
        finally:
            db.commit()
            db.close()
            print("sucessful server is close")
            print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))

print("hello this program is greatst i'made by <^Dolh^>".capitalize().title())
print("*" * 70)

print(name_user)
user_input = input("user_name :".strip().title())
while True:
        if  user_input == cl_6[1]:
            password = input("password :".strip())
            tried = 4
            while password != cl_6[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"correct password hello {cl_6[1]}".capitalize())
                print("*"*50)
            while True:
                reason = input("what can i help you boss :".strip().title())

                if reason == "all_password" or reason == "all_pass":
                    clint.show_password(cl_6)

                elif reason == "copy":
                    clint.copy_code(cl_6)   

                elif reason == "opp":
                    clint.calcalate(cl_6[1])    

                elif reason == "id":
                    clint.id_cl(cl_6[1])    

                elif reason == "rate":
                    clint.rate_python(cl_6)

                elif reason == "anlysis salary":
                    print(data_base.anlysis_salary(cl_6[1]))

                elif reason == "anlysis age":
                    print(data_base.anlysis_age(cl_6[1]))     

                elif reason == "all_data" or reason == "database":
                    data_base.database_all(cl_6)

                elif reason == "edit" or reason == "change":
                    data_base.adit_cl(cl_6[1])

                elif reason == "add":
                    data_base.add_cl(cl_6[1])

                elif reason == "delet" or reason == "del":
                    data_base.delete_cl(cl_6[1])

                elif reason == "skill cl1":
                    a = data_clint

                elif reason == "skill cl2":
                    print(cl_2[8])

                elif reason == "skill cl3":
                    print(cl_3[8])

                elif reason == "skill cl4":
                    print(cl_4[8])

                elif reason == "skill cl5":
                    print(cl_5[8])

                elif reason == "skill cl6":
                    print(cl_6[8])

                elif reason == "skill cl7":
                    print(cl_7[8])

                elif reason == "skill cl8":
                    print(cl_8[8])

                elif reason == "skill cl9":
                    print(cl_9[8])

                elif reason == "skill cl10":
                    print(cl_10[8])

                elif reason == "skill cl11":
                    print(cl_11[8])

                elif reason == "skill cl12":
                    print(cl_12[8])

                elif reason == "skill cl13":
                    print(cl_13[8])            

                elif reason == "age cl1":
                    print(cl_1[2])

                elif reason == "age cl2":
                    print(cl_2[2])

                elif reason == "age cl3":
                    print(cl_3[2])

                elif reason == "age cl4":
                    print(cl_4[2])

                elif reason == "age cl5":
                    print(cl_5[2])

                elif reason == "age cl6":
                    print(cl_6[2])

                elif reason == "age cl7":
                    print(cl_7[2])

                elif reason == "age cl8":
                    print(cl_8[2])

                elif reason == "age cl9":
                    print(cl_9[2])

                elif reason == "age cl10":
                    print(cl_10[2])

                elif reason == "age cl11":
                    print(cl_11[2])

                elif reason == "age cl12":
                    print(cl_12[2])

                elif reason == "age cl13":
                    print(cl_13[2])            

                elif reason == "country cl1":
                    print(cl_1[5])

                elif reason == "country cl2":
                    print(cl_2[5])

                elif reason == "country cl3":
                    print(cl_3[5])

                elif reason == "country cl4":
                    print(cl_4[5])

                elif reason == "country cl5":
                    print(cl_5[5])

                elif reason == "country cl6":
                    print(cl_6[5])

                elif reason == "country cl7":
                    print(cl_7[5])

                elif reason == "country cl8":
                    print(cl_8[5])

                elif reason == "country cl9":
                    print(cl_9[5])

                elif reason == "country cl10":
                    print(cl_10[5])

                elif reason == "country cl11":
                    print(cl_11[5])

                elif reason == "country cl12":
                    print(cl_12[5])

                elif reason == "country cl13":
                    print(cl_13[5])            

                elif reason == "all_data cl1":
                    print(cl_1)

                elif reason == "all_data cl2":
                    print(cl_2)

                elif reason == "all_data cl3":
                    print(cl_3)

                elif reason == "all_data cl4":
                    print(cl_4)

                elif reason == "all_data cl5":
                    print(cl_5)

                elif reason == "all_data cl6":
                    print(cl_6)

                elif reason == "all_data cl7":
                    print(cl_7)

                elif reason == "all_data cl8":
                    print(cl_8)

                elif reason == "all_data cl9":
                    print(cl_9)

                elif reason == "all_data cl10":
                    print(cl_10)

                elif reason == "all_data cl11":
                    print(cl_11)

                elif reason == "all_data cl12":
                    print(cl_12)

                elif reason == "all_data cl13":
                    print(cl_13)

                elif reason == "salary cl1":
                    print(cl_1[4])

                elif reason == "salary cl2":
                    print(cl_2[4])

                elif reason == "salary cl3":
                    print(cl_3[4])

                elif reason == "salary cl4":
                    print(cl_4[4])

                elif reason == "salary cl5":
                    print(cl_5[4])

                elif reason == "salary cl6":
                    print(cl_6[4])

                elif reason == "salary cl7":
                    print(cl_7[4])

                elif reason == "salary cl8":
                    print(cl_8[4])

                elif reason == "salary cl9":
                    print(cl_9[4])

                elif reason == "salary cl10":
                    print(cl_10[4])

                elif reason == "salary cl11":
                    print(cl_11[4])

                elif reason == "salary cl12":
                    print(cl_12[4])  

                elif reason == "salary cl13":
                    print(cl_13[4])          

                elif reason == "married cl1":
                    print(cl_1[3])

                elif reason == "married cl2":
                    print(cl_2[3])

                elif reason == "married cl3":
                    print(cl_3[3])

                elif reason == "married cl4":
                    print(cl_4[3])

                elif reason == "married cl5":
                    print(cl_5[3])

                elif reason == "married cl6":
                    print(cl_6[3])

                elif reason == "married cl7":
                    print(cl_7[3])

                elif reason == "married cl8":
                    print(cl_8[3])

                elif reason == "married cl9":
                    print(cl_9[3])

                elif reason == "married cl10":
                    print(cl_10[3])

                elif reason == "married cl11":
                    print(cl_11[3])

                elif reason == "married cl12":
                    print(cl_12[3])

                elif reason == "married cl13":
                    print(cl_13[3])            

                elif reason == "close" or reason == "exit":
                    sys.exit()

                else:
                    print("oh sorry try again if you need any more")
                    break
            else:
                break

        elif user_input == cl_1[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_1[6]:
                tried -= 1
                print(f"you have a {tried} to try agian")
                password = input('password: ').strip()
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_1[1]}")
                print("*"*50)
            while True:
                reason = input("can i help you manger : ".strip().title())
                if reason == "all_password" or reason == "all_pass":
                    clint.show_password(cl_1)

                elif reason == "copy":
                    clint.copy_code(cl_1)

                elif reason == "id":
                    clint.id_cl(cl_1[1])

                elif reason == "opp":
                    clint.calcalate(cl_1[1])        

                elif reason == "rate":
                    clint.rate_python(cl_1[1])

                elif reason == "all_data" or reason == "database":
                    data_base.database_all(cl_1)

                elif reason == "edit" or reason == "change":
                    data_base.adit_cl(cl_1[1])

                elif reason == "add":
                    data_base.add_cl(cl_1[1])

                elif reason == "delet" or reason == "del":
                    data_base.delete_cl(cl_1[1])    

                elif reason == "skill cl1":
                    print(cl_1[8])

                elif reason == "skill cl2":
                    print(cl_2[8])

                elif reason == "skill cl3":
                    print(cl_3[8])

                elif reason == "skill cl4":
                    print(cl_4[8])

                elif reason == "skill cl5":
                    print(cl_5[8])

                elif reason == "skill cl6":
                    print(cl_6[8])

                elif reason == "skill cl7":
                    print(cl_7[8])

                elif reason == "skill cl8":
                    print(cl_8[8])

                elif reason == "skill cl9":
                    print(cl_9[8])

                elif reason == "skill cl10":
                    print(cl_10[8])

                elif reason == "age cl1":
                    print(cl_1[2])

                elif reason == "age cl2":
                    print(cl_2[2])

                elif reason == "age cl3":
                    print(cl_3[2])

                elif reason == "age cl4":
                    print(cl_4[2])

                elif reason == "age cl5":
                    print(cl_5[2])

                elif reason == "age cl6":
                    print(cl_6[2])

                elif reason == "age cl7":
                    print(cl_7[2])

                elif reason == "age cl8":
                    print(cl_8[2])

                elif reason == "age cl9":
                    print(cl_9[2])

                elif reason == "age cl10":
                    print(cl_10[2])

                elif reason == "country cl1":
                    print(cl_1[5])

                elif reason == "country cl2":
                    print(cl_2[5])

                elif reason == "country cl3":
                    print(cl_3[5])

                elif reason == "country cl4":
                    print(cl_4[5])

                elif reason == "country cl5":
                    print(cl_5[5])

                elif reason == "country cl6":
                    print(cl_6[5])

                elif reason == "country cl7":
                    print(cl_7[5])

                elif reason == "country cl8":
                    print(cl_8[5])

                elif reason == "country cl9":
                    print(cl_9[5])

                elif reason == "country cl10":
                    print(cl_10[5])

                elif reason == "all_data cl1":
                    print(cl_1)

                elif reason == "all_data cl2":
                    print(cl_2)

                elif reason == "all_data cl3":
                    print(cl_3)

                elif reason == "all_data cl4":
                    print(cl_4)

                elif reason == "all_data cl5":
                    print(cl_5)

                elif reason == "all_data cl6":
                    print(cl_6)

                elif reason == "all_data cl7":
                    print(cl_7)

                elif reason == "all_data cl8":
                    print(cl_8)

                elif reason == "all_data cl9":
                    print(cl_9)

                elif reason == "all_data cl10":
                    print(cl_10)

                elif reason == "salary cl1":
                    print(cl_1[4])

                elif reason == "salary cl2":
                    print(cl_2[4])

                elif reason == "salary cl3":
                    print(cl_3[4])

                elif reason == "salary cl4":
                    print(cl_4[4])

                elif reason == "salary cl5":
                    print(cl_5[4])

                elif reason == "salary cl6":
                    print(cl_6[4])

                elif reason == "salary cl7":
                    print(cl_7[4])

                elif reason == "salary cl8":
                    print(cl_8[4])

                elif reason == "salary cl9":
                    print(cl_9[4])

                elif reason == "salary cl10":
                    print(cl_10[4])

                elif reason == "married cl1":
                    print(cl_1[3])

                elif reason == "married cl2":
                    print(cl_2[3])

                elif reason == "married cl3":
                    print(cl_3[3])

                elif reason == "married cl4":
                    print(cl_4[3])

                elif reason == "married cl5":
                    print(cl_5[3])

                elif reason == "married cl6":
                    print(cl_6[3])

                elif reason == "married cl7":
                    print(cl_7[3])

                elif reason == "married cl8":
                    print(cl_8[3])

                elif reason == "married cl9":
                    print(cl_9[3])

                elif reason == "married cl10":
                    print(cl_10[3])

                elif reason == "close" or reason == "exit":
                    sys.exit()

                else:
                    print("oh sorry try again if you need any more")
                    break
            else:
                break

        elif user_input == cl_2[1]:
            password = input('password :'.strip().title())
            tried = 4
            while password != cl_2[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
                else:
                    pass    
            else:
                print(f"sucess password hi {cl_2[1]}")
                print("*"*50)
            while True:
                reason = input("what are you want boss : ".strip().title())
                if reason == "all_password" or reason == "all_pass":
                    clint.show_password(cl_2)

                elif reason == "copy":
                    clint.copy_code(cl_2)

                elif reason == "opp":
                    clint.calcalate(cl_2[1])    

                elif reason == "id":
                    clint.id_cl(cl_2[1])    

                elif reason == "rate":
                    clint.rate_python(cl_2[1])

                elif reason == "all_data" or reason == "database":
                    data_base.database_all(cl_2)

                elif reason == "edit" or reason == "change":
                    data_base.adit_cl(cl_2[1])

                elif reason == 'anlysis salary':
                    print(data_base.anlysis_salary[cl_2[1]])

                elif reason == 'anlysis age':
                    print(data_base.anlysis_age[cl_2[1]])      

                elif reason == "add":
                    data_base.add_cl(cl_2[1])

                elif reason == "delet" or reason == "del":
                    data_base.delete_cl(cl_2[1])

                elif reason == "skill cl1":
                    print(cl_1[8])

                elif reason == "skill cl2":
                    print(cl_2[8])

                elif reason == "skill cl3":
                    print(cl_3[8])

                elif reason == "skill cl4":
                    print(cl_4[8])

                elif reason == "skill cl5":
                    print(cl_5[8])

                elif reason == "skill cl6":
                    print(cl_6[8])

                elif reason == "skill cl7":
                    print(cl_7[8])

                elif reason == "skill cl8":
                    print(cl_8[8])

                elif reason == "skill cl9":
                    print(cl_9[8])

                elif reason == "skill cl10":
                    print(cl_10[8])

                elif reason == "age cl1":
                    print(cl_1[2])

                elif reason == "age cl2":
                    print(cl_2[2])

                elif reason == "age cl3":
                    print(cl_3[2])

                elif reason == "age cl4":
                    print(cl_4[2])

                elif reason == "age cl5":
                    print(cl_5[2])

                elif reason == "age cl6":
                    print(cl_6[2])

                elif reason == "age cl7":
                    print(cl_7[2])

                elif reason == "age cl8":
                    print(cl_8[2])

                elif reason == "age cl9":
                    print(cl_9[2])

                elif reason == "age cl10":
                    print(cl_10[2])

                elif reason == "country cl1":
                    print(cl_1[5])

                elif reason == "country cl2":
                    print(cl_2[5])

                elif reason == "country cl3":
                    print(cl_3[5])

                elif reason == "country cl4":
                    print(cl_4[5])

                elif reason == "country cl5":
                    print(cl_5[5])

                elif reason == "country cl6":
                    print(cl_6[5])

                elif reason == "country cl7":
                    print(cl_7[5])

                elif reason == "country cl8":
                    print(cl_8[5])

                elif reason == "country cl9":
                    print(cl_9[5])

                elif reason == "country cl10":
                    print(cl_10[5])

                elif reason == "all_data cl1":
                    print(cl_1)

                elif reason == "all_data cl2":
                    print(cl_2)

                elif reason == "all_data cl3":
                    print(cl_3)

                elif reason == "all_data cl4":
                    print(cl_4)

                elif reason == "all_data cl5":
                    print(cl_5)

                elif reason == "all_data cl6":
                    print(cl_6)

                elif reason == "all_data cl7":
                    print(cl_7)

                elif reason == "all_data cl8":
                    print(cl_8)

                elif reason == "all_data cl9":
                    print(cl_9)

                elif reason == "all_data cl10":
                    print(cl_10)

                elif reason == "salary cl1":
                    print(cl_1[4])

                elif reason == "salary cl2":
                    print(cl_2[4])

                elif reason == "salary cl3":
                    print(cl_3[4])

                elif reason == "salary cl4":
                    print(cl_4[4])

                elif reason == "salary cl5":
                    print(cl_5[4])

                elif reason == "salary cl6":
                    print(cl_6[4])

                elif reason == "salary cl7":
                    print(cl_7[4])

                elif reason == "salary cl8":
                    print(cl_8[4])

                elif reason == "salary cl9":
                    print(cl_9[4])

                elif reason == "salary cl10":
                    print(cl_10[4])

                elif reason == "married cl1":
                    print(cl_1[3])

                elif reason == "married cl2":
                    print(cl_2[3])

                elif reason == "married cl3":
                    print(cl_3[3])

                elif reason == "married cl4":
                    print(cl_4[3])

                elif reason == "married cl5":
                    print(cl_5[3])

                elif reason == "married cl6":
                    print(cl_6[3])

                elif reason == "married cl7":
                    print(cl_7[3])

                elif reason == "married cl8":
                    print(cl_8[3])

                elif reason == "married cl9":
                    print(cl_9[3])

                elif reason == "married cl10":
                    print(cl_10[3])

                elif reason == "close" or reason == "exit":
                    sys.exit()

                else:
                    print("oh sorry try again if you need any more")
                    break
            else:
                break

        elif user_input == cl_3[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_3[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_3[1]}")
                print("*"*50)
                quision = input(f"what can i help you hacker {cl_3[1]} :".strip().title())
                if quision == "data":
                    cr = db.execute("select * from data_clint where user_id = 3")
                    all_data6 = cr.fetchall()
                    print(all_data6)

                elif quision == 'copy':
                    print(clint.copy_code(cl_3[1]))

                elif quision == 'opp':
                    print(clint.calcalate(cl_3[1]))        

                elif quision == 'edit':
                    print(data_base.add_cl(cl_3[1]))

                elif quision == 'add':
                    print(data_base.add_cl(cl_3[1]))

                elif quision == 'delet' or quision == 'del':
                    print(data_base.delete_cl(cl_3[1]))  
                
                elif quision == 'id':
                    print(id(cl_3[1]))

                elif quision == 'database':
                    print(data_base.database_all(cl_3[1]))  

                else:
                    print("sorry_cant show you this information only for manger_vip")
                    break

        elif user_input == cl_4[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_4[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hello {cl_4[1]}")
                print("*"*50)
                quision = input("you can only look your information : ".title().strip())
                if quision == "okey" or quision == "ok" or quision == "data me":
                    print(cl_4)
                    
                elif quision == 'anlysis salary':
                    print(data_base.anlysis_salary)

                elif quision == 'anlysis age':
                    print(data_base.anlysis_age(cl_4[1]))  

                elif quision == 'database':
                    print(data_base.database_all(cl_4[1]))

                elif quision == 'edit':
                    print(data_base.adit_cl(cl_4[1]))

                elif quision == 'add':
                    print(data_base.add_cl(cl_4[1]))             
                    
                else:
                    print("sorry_cant show you this information only for manger_vip")
                    break

        elif user_input == cl_5[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_5[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_5[1]}")
                print("*"*50)
            while True:
                reason = input("what are you want boss : ".strip().title())
                if reason == 'database':
                    print(data_base.database_all(cl_5[1]))

                elif reason == "opp":
                    clint.calcalate(cl_5[1])    

                elif reason == "id":
                    clint.id_cl(cl_5[1])    

                elif reason == "rate":
                    clint.rate_python(cl_5[1])

                elif reason == "skill cl1":
                    print(cl_1[8])

                elif reason == "skill cl2":
                    print(cl_2[8])

                elif reason == "skill cl3":
                    print(cl_3[8])

                elif reason == "skill cl4":
                    print(cl_4[8])

                elif reason == "skill cl5":
                    print(cl_5[8])

                elif reason == "skill cl6":
                    print(cl_6[8])

                elif reason == "skill cl7":
                    print(cl_7[8])

                elif reason == "skill cl8":
                    print(cl_8[8])

                elif reason == "skill cl9":
                    print(cl_9[8])

                elif reason == "skill cl10":
                    print(cl_10[8])

                elif reason == "skill cl11":
                    print(cl_11[8])

                elif reason == "skill cl12":
                    print(cl_12[8])

                elif reason == "skill cl13":
                    print(cl_13[8])            

                elif reason == "age cl1":
                    print(cl_1[2])

                elif reason == "age cl2":
                    print(cl_2[2])

                elif reason == "age cl3":
                    print(cl_3[2])

                elif reason == "age cl4":
                    print(cl_4[2])

                elif reason == "age cl5":
                    print(cl_5[2])

                elif reason == "age cl6":
                    print(cl_6[2])

                elif reason == "age cl7":
                    print(cl_7[2])

                elif reason == "age cl8":
                    print(cl_8[2])

                elif reason == "age cl9":
                    print(cl_9[2])

                elif reason == "age cl10":
                    print(cl_10[2])

                elif reason == "age cl11":
                    print(cl_11[2])

                elif reason == "age cl12":
                    print(cl_12[2])

                elif reason == "age cl13":
                    print(cl_13[2])            

                elif reason == "country cl1":
                    print(cl_1[5])

                elif reason == "country cl2":
                    print(cl_2[5])

                elif reason == "country cl3":
                    print(cl_3[5])

                elif reason == "country cl4":
                    print(cl_4[5])

                elif reason == "country cl5":
                    print(cl_5[5])

                elif reason == "country cl6":
                    print(cl_6[5])

                elif reason == "country cl7":
                    print(cl_7[5])

                elif reason == "country cl8":
                    print(cl_8[5])

                elif reason == "country cl9":
                    print(cl_9[5])

                elif reason == "country cl10":
                    print(cl_10[5])

                elif reason == "country cl11":
                    print(cl_11[5])

                elif reason == "country cl12":
                    print(cl_12[5])

                elif reason == "country cl13":
                    print(cl_13[5])            

                elif reason == "all_data cl1":
                    print(cl_1)

                elif reason == "all_data cl2":
                    print(cl_2)

                elif reason == "all_data cl3":
                    print(cl_3)

                elif reason == "all_data cl4":
                    print(cl_4)

                elif reason == "all_data cl5":
                    print(cl_5)

                elif reason == "all_data cl6":
                    print(cl_6)

                elif reason == "all_data cl7":
                    print(cl_7)

                elif reason == "all_data cl8":
                    print(cl_8)

                elif reason == "all_data cl9":
                    print(cl_9)

                elif reason == "all_data cl10":
                    print(cl_10)

                elif reason == "all_data cl11":
                    print(cl_11)

                elif reason == "all_data cl12":
                    print(cl_12)

                elif reason == "all_data cl13":
                    print(cl_13)

                elif reason == "salary cl1":
                    print(cl_1[4])

                elif reason == "salary cl2":
                    print(cl_2[4])

                elif reason == "salary cl3":
                    print(cl_3[4])

                elif reason == "salary cl4":
                    print(cl_4[4])

                elif reason == "salary cl5":
                    print(cl_5[4])

                elif reason == "salary cl6":
                    print(cl_6[4])

                elif reason == "salary cl7":
                    print(cl_7[4])

                elif reason == "salary cl8":
                    print(cl_8[4])

                elif reason == "salary cl9":
                    print(cl_9[4])

                elif reason == "salary cl10":
                    print(cl_10[4])

                elif reason == "salary cl11":
                    print(cl_11[4])

                elif reason == "salary cl12":
                    print(cl_12[4])  

                elif reason == "salary cl13":
                    print(cl_13[4])          

                elif reason == "married cl1":
                    print(cl_1[3])

                elif reason == "married cl2":
                    print(cl_2[3])

                elif reason == "married cl3":
                    print(cl_3[3])

                elif reason == "married cl4":
                    print(cl_4[3])

                elif reason == "married cl5":
                    print(cl_5[3])

                elif reason == "married cl6":
                    print(cl_6[3])

                elif reason == "married cl7":
                    print(cl_7[3])

                elif reason == "married cl8":
                    print(cl_8[3])

                elif reason == "married cl9":
                    print(cl_9[3])

                elif reason == "married cl10":
                    print(cl_10[3])

                elif reason == "married cl11":
                    print(cl_11[3])

                elif reason == "married cl12":
                    print(cl_12[3])

                elif reason == "married cl13":
                    print(cl_13[3])            

                elif reason == "close" or reason == "exit":
                    sys.exit()            
                else:
                    print("i cant understand you please try agian")  

            else:
                break             


        elif user_input == cl_7[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_7[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_7[1]}")
                print("*"*50)
                quision = input("you can only look your information : ".title().strip())
                if quision == "okey" or quision == "ok" or quision == "data me":
                    cr = db.execute("select * from data_clint where user_id = 7")
                    all_data1 = cr.fetchall()
                    print(all_data1)
                    sec = input("do you know secrat password to acess all_data company :".title().strip())
                    if sec == "yes":
                        sec_input = input("***put a password*** :".strip())
                        if sec_input in secart_password:
                            while True:
                                reason = input("what are you want : ".strip())

                                if reason == "copy":
                                    clint.copy_code(cl_7)

                                elif reason == "opp":
                                    clint.calcalate(cl_7[1])    

                                elif reason == "id":
                                    clint.id_cl(cl_7[1])    

                                elif reason == "rate":
                                    clint.rate_python(cl_7[1])

                                elif reason == "all_data" or reason == "database":
                                    data_base.database_all(cl_7)

                                elif reason == "skill cl1":
                                    print(cl_1[8])

                                elif reason == "skill cl2":
                                    print(cl_2[8])

                                elif reason == "skill cl3":
                                    print(cl_3[8])

                                elif reason == "skill cl4":
                                    print(cl_4[8])

                                elif reason == "skill cl5":
                                    print(cl_5[8])

                                elif reason == "skill cl6":
                                    print(cl_6[8])

                                elif reason == "skill cl7":
                                    print(cl_7[8])

                                elif reason == "skill cl8":
                                    print(cl_8[8])

                                elif reason == "skill cl9":
                                    print(cl_9[8])

                                elif reason == "skill cl10":
                                    print(cl_10[8])

                                elif reason == "skill cl11":
                                    print(cl_11[8])

                                elif reason == "skill cl12":
                                    print(cl_12[8])        

                                elif reason == "age cl1":
                                    print(cl_1[2])

                                elif reason == "age cl2":
                                    print(cl_2[2])

                                elif reason == "age cl3":
                                    print(cl_3[2])

                                elif reason == "age cl4":
                                    print(cl_4[2])

                                elif reason == "age cl5":
                                    print(cl_5[2])

                                elif reason == "age cl6":
                                    print(cl_6[2])

                                elif reason == "age cl7":
                                    print(cl_7[2])

                                elif reason == "age cl8":
                                    print(cl_8[2])

                                elif reason == "age cl9":
                                    print(cl_9[2])

                                elif reason == "age cl10":
                                    print(cl_10[2])

                                elif reason == "age cl11":
                                    print(cl_11[2])

                                elif reason == "age cl12":
                                    print(cl_12[2])        

                                elif reason == "country cl1":
                                    print(cl_1[5])

                                elif reason == "country cl2":
                                    print(cl_2[5])

                                elif reason == "country cl3":
                                    print(cl_3[5])

                                elif reason == "country cl4":
                                    print(cl_4[5])

                                elif reason == "country cl5":
                                    print(cl_5[5])

                                elif reason == "country cl6":
                                    print(cl_6[5])

                                elif reason == "country cl7":
                                    print(cl_7[5])

                                elif reason == "country cl8":
                                    print(cl_8[5])

                                elif reason == "country cl9":
                                    print(cl_9[5])

                                elif reason == "country cl10":
                                    print(cl_10[5])

                                elif reason == "country cl11":
                                    print(cl_11[5])

                                elif reason == "country cl12":
                                    print(cl_12[5])        

                                elif reason == "all_data cl1":
                                    print(cl_1)

                                elif reason == "all_data cl2":
                                    print(cl_2)

                                elif reason == "all_data cl3":
                                    print(cl_3)

                                elif reason == "all_data cl4":
                                    print(cl_4)

                                elif reason == "all_data cl5":
                                    print(cl_5)

                                elif reason == "all_data cl6":
                                    print(cl_6)

                                elif reason == "all_data cl7":
                                    print(cl_7)

                                elif reason == "all_data cl8":
                                    print(cl_8)

                                elif reason == "all_data cl9":
                                    print(cl_9)

                                elif reason == "all_data cl10":
                                    print(cl_10)

                                elif reason == "all_data cl11":
                                    print(cl_11)

                                elif reason == "all_data cl12":
                                    print(cl_12)        

                                elif reason == "salary cl1":
                                    print(cl_1[4])

                                elif reason == "salary cl2":
                                    print(cl_2[4])

                                elif reason == "salary cl3":
                                    print(cl_3[4])

                                elif reason == "salary cl4":
                                    print(cl_4[4])

                                elif reason == "salary cl5":
                                    print(cl_5[4])

                                elif reason == "salary cl6":
                                    print(cl_6[4])

                                elif reason == "salary cl7":
                                    print(cl_7[4])

                                elif reason == "salary cl8":
                                    print(cl_8[4])

                                elif reason == "salary cl9":
                                    print(cl_9[4])

                                elif reason == "salary cl10":
                                    print(cl_10[4])

                                elif reason == "salary cl11":
                                    print(cl_11[4])

                                elif reason == "salary cl12":
                                    print(cl_12[4])        

                                elif reason == "married cl1":
                                    print(cl_1[3])

                                elif reason == "married cl2":
                                    print(cl_2[3])

                                elif reason == "married cl3":
                                    print(cl_3[3])

                                elif reason == "married cl4":
                                    print(cl_4[3])

                                elif reason == "married cl5":
                                    print(cl_5[3])

                                elif reason == "married cl6":
                                    print(cl_6[3])

                                elif reason == "married cl7":
                                    print(cl_7[3])

                                elif reason == "married cl8":
                                    print(cl_8[3])

                                elif reason == "married cl9":
                                    print(cl_9[3])

                                elif reason == "married cl10":
                                    print(cl_10[3])

                                elif reason == "married cl11":
                                    print(cl_11[3])

                                elif reason == "married cl12":
                                    print(cl_12[3])        

                                elif reason == "close" or reason == "exit":
                                    sys.exit()

                                else:
                                    print("oh sorry try again if you need any more")
                                    break
                            else:
                                break
                        else:
                            print("you dont know password so bye")
                            break
                    else:
                        print("password secart is wrong bye >[-_-]<")
                        break

        elif user_input == cl_8[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_8[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_8[1]}")
                print("*"*50)
                quision = input("you can only look your information : ".title().strip())
                if quision == "okey" or quision == "ok" or quision == "data me":
                    cr = db.execute("select * from data_clint where user_id = 8")
                    all_data7 = cr.fetchall()
                    print(all_data7)
                    sec = input("do you know secrat password to acess all_data company :".title().strip())
                    if sec == "yes":
                        pass11 = input("***put a password*** :".strip())
                        if pass11 in secart_password:
                            while True:
                                reason = input("what are you want : ".strip())

                                if reason == "copy":
                                    clint.copy_code(cl_8)

                                elif reason == "opp":
                                    clint.calcalate(cl_8[1])    

                                elif reason == "id":
                                    clint.id_cl(cl_8[1])    

                                elif reason == "rate":
                                    clint.rate_python(cl_8[1])

                                elif reason == "all_data" or reason == "database":
                                    data_base.database_all(cl_8)

                                elif reason == "skill cl1":
                                    print(cl_1[8])

                                elif reason == "skill cl2":
                                    print(cl_2[8])

                                elif reason == "skill cl3":
                                    print(cl_3[8])

                                elif reason == "skill cl4":
                                    print(cl_4[8])

                                elif reason == "skill cl5":
                                    print(cl_5[8])

                                elif reason == "skill cl6":
                                    print(cl_6[8])

                                elif reason == "skill cl7":
                                    print(cl_7[8])

                                elif reason == "skill cl8":
                                    print(cl_8[8])

                                elif reason == "skill cl9":
                                    print(cl_9[8])

                                elif reason == "skill cl10":
                                    print(cl_10[8])

                                elif reason == "skill cl11":
                                    print(cl_11[8])

                                elif reason == "skill cl12":
                                    print(cl_12[8])        

                                elif reason == "age cl1":
                                    print(cl_1[2])

                                elif reason == "age cl2":
                                    print(cl_2[2])

                                elif reason == "age cl3":
                                    print(cl_3[2])

                                elif reason == "age cl4":
                                    print(cl_4[2])

                                elif reason == "age cl5":
                                    print(cl_5[2])

                                elif reason == "age cl6":
                                    print(cl_6[2])

                                elif reason == "age cl7":
                                    print(cl_7[2])

                                elif reason == "age cl8":
                                    print(cl_8[2])

                                elif reason == "age cl9":
                                    print(cl_9[2])

                                elif reason == "age cl10":
                                    print(cl_10[2])

                                elif reason == "age cl11":
                                    print(cl_11[2])

                                elif reason == "age cl12":
                                    print(cl_12[2])        

                                elif reason == "country cl1":
                                    print(cl_1[5])

                                elif reason == "country cl2":
                                    print(cl_2[5])

                                elif reason == "country cl3":
                                    print(cl_3[5])

                                elif reason == "country cl4":
                                    print(cl_4[5])

                                elif reason == "country cl5":
                                    print(cl_5[5])

                                elif reason == "country cl6":
                                    print(cl_6[5])

                                elif reason == "country cl7":
                                    print(cl_7[5])

                                elif reason == "country cl8":
                                    print(cl_8[5])

                                elif reason == "country cl9":
                                    print(cl_9[5])

                                elif reason == "country cl10":
                                    print(cl_10[5])

                                elif reason == "country cl11":
                                    print(cl_11[5])

                                elif reason == "country cl12":
                                    print(cl_12[5])        

                                elif reason == "all_data cl1":
                                    print(cl_1)

                                elif reason == "all_data cl2":
                                    print(cl_2)

                                elif reason == "all_data cl3":
                                    print(cl_3)

                                elif reason == "all_data cl4":
                                    print(cl_4)

                                elif reason == "all_data cl5":
                                    print(cl_5)

                                elif reason == "all_data cl6":
                                    print(cl_6)

                                elif reason == "all_data cl7":
                                    print(cl_7)

                                elif reason == "all_data cl8":
                                    print(cl_8)

                                elif reason == "all_data cl9":
                                    print(cl_9)

                                elif reason == "all_data cl10":
                                    print(cl_10)

                                elif reason == "all_data cl11":
                                    print(cl_11)

                                elif reason == "all_data cl12":
                                    print(cl_12)        

                                elif reason == "salary cl1":
                                    print(cl_1[4])

                                elif reason == "salary cl2":
                                    print(cl_2[4])

                                elif reason == "salary cl3":
                                    print(cl_3[4])

                                elif reason == "salary cl4":
                                    print(cl_4[4])

                                elif reason == "salary cl5":
                                    print(cl_5[4])

                                elif reason == "salary cl6":
                                    print(cl_6[4])

                                elif reason == "salary cl7":
                                    print(cl_7[4])

                                elif reason == "salary cl8":
                                    print(cl_8[4])

                                elif reason == "salary cl9":
                                    print(cl_9[4])

                                elif reason == "salary cl10":
                                    print(cl_10[4])

                                elif reason == "salary cl11":
                                    print(cl_11[4])

                                elif reason == "salary cl12":
                                    print(cl_12[4])        

                                elif reason == "married cl1":
                                    print(cl_1[3])

                                elif reason == "married cl2":
                                    print(cl_2[3])

                                elif reason == "married cl3":
                                    print(cl_3[3])

                                elif reason == "married cl4":
                                    print(cl_4[3])

                                elif reason == "married cl5":
                                    print(cl_5[3])

                                elif reason == "married cl6":
                                    print(cl_6[3])

                                elif reason == "married cl7":
                                    print(cl_7[3])

                                elif reason == "married cl8":
                                    print(cl_8[3])

                                elif reason == "married cl9":
                                    print(cl_9[3])

                                elif reason == "married cl10":
                                    print(cl_10[3])

                                elif reason == "married cl11":
                                    print(cl_11[3])

                                elif reason == "married cl12":
                                    print(cl_12[3])        

                                elif reason == "close" or reason == "exit":
                                    sys.exit()

                                else:
                                    print("oh sorry try again if you need any more")
                                    break
                            else:
                                break
                        else:
                            print("wrong password please try agian")
                            break
                    else:
                        break
                else:
                    print("i cant show you more if you know secart password")
                    break


        elif user_input == cl_9[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_9[6]:
                tried -= 1
                print(f"you have a {tried} to try agian")
                password = input('password: ').strip()
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_9[1]}")
                print("*"*50)
            while True:
                reason = input("can i help you manger : ".strip().title())                

                if reason == "copy":
                    clint.copy_code(cl_9)

                elif reason == "id":
                    clint.id_cl(cl_9[1]) 

                elif reason == "opp":
                    clint.calcalate(cl_9[1])       

                elif reason == "rate":
                    clint.rate_python(cl_9[1])

                elif reason == "all_data" or reason == "database":
                    data_base.database_all(cl_6)

                elif reason == "skill cl1":
                    print(cl_1[8])

                elif reason == "skill cl2":
                    print(cl_2[8])

                elif reason == "skill cl3":
                    print(cl_3[8])

                elif reason == "skill cl4":
                    print(cl_4[8])

                elif reason == "skill cl5":
                    print(cl_5[8])

                elif reason == "skill cl6":
                    print(cl_6[8])

                elif reason == "skill cl7":
                    print(cl_7[8])

                elif reason == "skill cl8":
                    print(cl_8[8])

                elif reason == "skill cl9":
                    print(cl_9[8])

                elif reason == "skill cl10":
                    print(cl_10[8])

                elif reason == "age cl1":
                    print(cl_1[2])

                elif reason == "age cl2":
                    print(cl_2[2])

                elif reason == "age cl3":
                    print(cl_3[2])

                elif reason == "age cl4":
                    print(cl_4[2])

                elif reason == "age cl5":
                    print(cl_5[2])

                elif reason == "age cl6":
                    print(cl_6[2])

                elif reason == "age cl7":
                    print(cl_7[2])

                elif reason == "age cl8":
                    print(cl_8[2])

                elif reason == "age cl9":
                    print(cl_9[2])

                elif reason == "age cl10":
                    print(cl_10[2])

                elif reason == "country cl1":
                    print(cl_1[5])

                elif reason == "country cl2":
                    print(cl_2[5])

                elif reason == "country cl3":
                    print(cl_3[5])

                elif reason == "country cl4":
                    print(cl_4[5])

                elif reason == "country cl5":
                    print(cl_5[5])

                elif reason == "country cl6":
                    print(cl_6[5])

                elif reason == "country cl7":
                    print(cl_7[5])

                elif reason == "country cl8":
                    print(cl_8[5])

                elif reason == "country cl9":
                    print(cl_9[5])

                elif reason == "country cl10":
                    print(cl_10[5])

                elif reason == "all_data cl1":
                    print(cl_1)

                elif reason == "all_data cl2":
                    print(cl_2)

                elif reason == "all_data cl3":
                    print(cl_3)

                elif reason == "all_data cl4":
                    print(cl_4)

                elif reason == "all_data cl5":
                    print(cl_5)

                elif reason == "all_data cl6":
                    print(cl_6)

                elif reason == "all_data cl7":
                    print(cl_7)

                elif reason == "all_data cl8":
                    print(cl_8)

                elif reason == "all_data cl9":
                    print(cl_9)

                elif reason == "all_data cl10":
                    print(cl_10)

                elif reason == "salary cl1":
                    print(cl_1[4])

                elif reason == "salary cl2":
                    print(cl_2[4])

                elif reason == "salary cl3":
                    print(cl_3[4])

                elif reason == "salary cl4":
                    print(cl_4[4])

                elif reason == "salary cl5":
                    print(cl_5[4])

                elif reason == "salary cl6":
                    print(cl_6[4])

                elif reason == "salary cl7":
                    print(cl_7[4])

                elif reason == "salary cl8":
                    print(cl_8[4])

                elif reason == "salary cl9":
                    print(cl_9[4])

                elif reason == "salary cl10":
                    print(cl_10[4])

                elif reason == "married cl1":
                    print(cl_1[3])

                elif reason == "married cl2":
                    print(cl_2[3])

                elif reason == "married cl3":
                    print(cl_3[3])

                elif reason == "married cl4":
                    print(cl_4[3])

                elif reason == "married cl5":
                    print(cl_5[3])

                elif reason == "married cl6":
                    print(cl_6[3])

                elif reason == "married cl7":
                    print(cl_7[3])

                elif reason == "married cl8":
                    print(cl_8[3])

                elif reason == "married cl9":
                    print(cl_9[3])

                elif reason == "married cl10":
                    print(cl_10[3])

                elif reason == "close" or reason == "exit":
                    sys.exit()

                else:
                    print("oh sorry try again if you need any more")
                    break
            else:
                break

        elif user_input == cl_10[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_10[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_10[1]}")
                print("*"*50)
                quision = input("you can only look your information : ".title().strip())
                if quision == "okey" or quision == "ok" or quision == "data me":
                    cr = db.execute("select * from data_clint where user_id = 10")
                    all_data10 = cr.fetchall()
                    print(all_data10)
                    sec = input("do you know secrat password to acess all_data company :".title().strip())
                    if sec == "yes":
                        pass11 = input("***put a password*** :".strip())
                        if pass11 in secart_password:
                            while True:
                                reason = input("what are you want : ".strip())

                                if reason == "copy":
                                    clint.copy_code(cl_10)

                                elif reason == "opp":
                                    clint.calcalate(cl_10[1])    

                                elif reason == "id":
                                    clint.id_cl(cl_10[1])    

                                elif reason == "rate":
                                    clint.rate_python(cl_10[1])

                                elif reason == "all_data" or reason == "database":
                                    data_base.database_all(cl_10)

                                elif reason == "skill cl1":
                                    print(cl_1[8])

                                elif reason == "skill cl2":
                                    print(cl_2[8])

                                elif reason == "skill cl3":
                                    print(cl_3[8])

                                elif reason == "skill cl4":
                                    print(cl_4[8])

                                elif reason == "skill cl5":
                                    print(cl_5[8])

                                elif reason == "skill cl6":
                                    print(cl_6[8])

                                elif reason == "skill cl7":
                                    print(cl_7[8])

                                elif reason == "skill cl8":
                                    print(cl_8[8])

                                elif reason == "skill cl9":
                                    print(cl_9[8])

                                elif reason == "skill cl10":
                                    print(cl_10[8])

                                elif reason == "skill cl11":
                                    print(cl_11[8])

                                elif reason == "skill cl12":
                                    print(cl_12[8])        

                                elif reason == "age cl1":
                                    print(cl_1[2])

                                elif reason == "age cl2":
                                    print(cl_2[2])

                                elif reason == "age cl3":
                                    print(cl_3[2])

                                elif reason == "age cl4":
                                    print(cl_4[2])

                                elif reason == "age cl5":
                                    print(cl_5[2])

                                elif reason == "age cl6":
                                    print(cl_6[2])

                                elif reason == "age cl7":
                                    print(cl_7[2])

                                elif reason == "age cl8":
                                    print(cl_8[2])

                                elif reason == "age cl9":
                                    print(cl_9[2])

                                elif reason == "age cl10":
                                    print(cl_10[2])

                                elif reason == "age cl11":
                                    print(cl_11[2])

                                elif reason == "age cl12":
                                    print(cl_12[2])        

                                elif reason == "country cl1":
                                    print(cl_1[5])

                                elif reason == "country cl2":
                                    print(cl_2[5])

                                elif reason == "country cl3":
                                    print(cl_3[5])

                                elif reason == "country cl4":
                                    print(cl_4[5])

                                elif reason == "country cl5":
                                    print(cl_5[5])

                                elif reason == "country cl6":
                                    print(cl_6[5])

                                elif reason == "country cl7":
                                    print(cl_7[5])

                                elif reason == "country cl8":
                                    print(cl_8[5])

                                elif reason == "country cl9":
                                    print(cl_9[5])

                                elif reason == "country cl10":
                                    print(cl_10[5])

                                elif reason == "country cl11":
                                    print(cl_11[5])

                                elif reason == "country cl12":
                                    print(cl_12[5])        

                                elif reason == "all_data cl1":
                                    print(cl_1)

                                elif reason == "all_data cl2":
                                    print(cl_2)

                                elif reason == "all_data cl3":
                                    print(cl_3)

                                elif reason == "all_data cl4":
                                    print(cl_4)

                                elif reason == "all_data cl5":
                                    print(cl_5)

                                elif reason == "all_data cl6":
                                    print(cl_6)

                                elif reason == "all_data cl7":
                                    print(cl_7)

                                elif reason == "all_data cl8":
                                    print(cl_8)

                                elif reason == "all_data cl9":
                                    print(cl_9)

                                elif reason == "all_data cl10":
                                    print(cl_10)

                                elif reason == "all_data cl11":
                                    print(cl_11)

                                elif reason == "all_data cl12":
                                    print(cl_12)        

                                elif reason == "salary cl1":
                                    print(cl_1[4])

                                elif reason == "salary cl2":
                                    print(cl_2[4])

                                elif reason == "salary cl3":
                                    print(cl_3[4])

                                elif reason == "salary cl4":
                                    print(cl_4[4])

                                elif reason == "salary cl5":
                                    print(cl_5[4])

                                elif reason == "salary cl6":
                                    print(cl_6[4])

                                elif reason == "salary cl7":
                                    print(cl_7[4])

                                elif reason == "salary cl8":
                                    print(cl_8[4])

                                elif reason == "salary cl9":
                                    print(cl_9[4])

                                elif reason == "salary cl10":
                                    print(cl_10[4])

                                elif reason == "salary cl11":
                                    print(cl_11[4])

                                elif reason == "salary cl12":
                                    print(cl_12[4])        

                                elif reason == "married cl1":
                                    print(cl_1[3])

                                elif reason == "married cl2":
                                    print(cl_2[3])

                                elif reason == "married cl3":
                                    print(cl_3[3])

                                elif reason == "married cl4":
                                    print(cl_4[3])

                                elif reason == "married cl5":
                                    print(cl_5[3])

                                elif reason == "married cl6":
                                    print(cl_6[3])

                                elif reason == "married cl7":
                                    print(cl_7[3])

                                elif reason == "married cl8":
                                    print(cl_8[3])

                                elif reason == "married cl9":
                                    print(cl_9[3])

                                elif reason == "married cl10":
                                    print(cl_10[3])

                                elif reason == "married cl11":
                                    print(cl_11[3])

                                elif reason == "married cl12":
                                    print(cl_12[3])        

                                elif reason == "close" or reason == "exit":
                                    sys.exit()

                                else:
                                    print("oh sorry try again if you need any more")
                                    print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                                    break
                            else:
                                print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                                break
                        else:
                            print("wrong passowrd bye [-_-]")
                            print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                            break
                    else:
                        print("okey thank you to use us [^_^]")
                        print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                        break
                else:
                    print("sorry_cant show you this information only for manger_vip")
                    print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                    break
        
        elif user_input == cl_11[1]:
            password = input('password: ').strip()
            tried = 4
            while password != cl_11[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"sucess password hi {cl_11[1]}")
                print("*"*50)
                quision = input("you can only look your information : ".title().strip())
                if quision == "okey" or quision == "ok" or quision == "data me":
                    cr = db.execute("select * from data_clint where user_id = 11")
                    all_data11 = cr.fetchall()
                    print(all_data11)
                    sec = input("do you know secrat password to acess all_data company :".title().strip())
                    if sec == "yes":
                        pass11 = input("***put a password*** :".strip())
                        if pass11 in secart_password:
                            while True:
                                reason = input("what are you want : ".strip())

                                if reason == "copy":
                                    clint.copy_code(cl_11)

                                elif reason == "opp":
                                    clint.calcalate(cl_11[1])    

                                elif reason == "id":
                                    clint.id_cl(cl_11[1])    

                                elif reason == "rate":
                                    clint.rate_python(cl_11[1])

                                elif reason == "all_data" or reason == "database":
                                    data_base.database_all(cl_11)

                                elif reason == "skill cl1":
                                    print(cl_1[8])

                                elif reason == "skill cl2":
                                    print(cl_2[8])

                                elif reason == "skill cl3":
                                    print(cl_3[8])

                                elif reason == "skill cl4":
                                    print(cl_4[8])

                                elif reason == "skill cl5":
                                    print(cl_5[8])

                                elif reason == "skill cl6":
                                    print(cl_6[8])

                                elif reason == "skill cl7":
                                    print(cl_7[8])

                                elif reason == "skill cl8":
                                    print(cl_8[8])

                                elif reason == "skill cl9":
                                    print(cl_9[8])

                                elif reason == "skill cl10":
                                    print(cl_10[8])

                                elif reason == "skill cl11":
                                    print(cl_11[8])

                                elif reason == "skill cl12":
                                    print(cl_12[8])        

                                elif reason == "age cl1":
                                    print(cl_1[2])

                                elif reason == "age cl2":
                                    print(cl_2[2])

                                elif reason == "age cl3":
                                    print(cl_3[2])

                                elif reason == "age cl4":
                                    print(cl_4[2])

                                elif reason == "age cl5":
                                    print(cl_5[2])

                                elif reason == "age cl6":
                                    print(cl_6[2])

                                elif reason == "age cl7":
                                    print(cl_7[2])

                                elif reason == "age cl8":
                                    print(cl_8[2])

                                elif reason == "age cl9":
                                    print(cl_9[2])

                                elif reason == "age cl10":
                                    print(cl_10[2])

                                elif reason == "age cl11":
                                    print(cl_11[2])

                                elif reason == "age cl12":
                                    print(cl_12[2])        

                                elif reason == "country cl1":
                                    print(cl_1[5])

                                elif reason == "country cl2":
                                    print(cl_2[5])

                                elif reason == "country cl3":
                                    print(cl_3[5])

                                elif reason == "country cl4":
                                    print(cl_4[5])

                                elif reason == "country cl5":
                                    print(cl_5[5])

                                elif reason == "country cl6":
                                    print(cl_6[5])

                                elif reason == "country cl7":
                                    print(cl_7[5])

                                elif reason == "country cl8":
                                    print(cl_8[5])

                                elif reason == "country cl9":
                                    print(cl_9[5])

                                elif reason == "country cl10":
                                    print(cl_10[5])

                                elif reason == "country cl11":
                                    print(cl_11[5])

                                elif reason == "country cl12":
                                    print(cl_12[5])        

                                elif reason == "all_data cl1":
                                    print(cl_1)

                                elif reason == "all_data cl2":
                                    print(cl_2)

                                elif reason == "all_data cl3":
                                    print(cl_3)

                                elif reason == "all_data cl4":
                                    print(cl_4)

                                elif reason == "all_data cl5":
                                    print(cl_5)

                                elif reason == "all_data cl6":
                                    print(cl_6)

                                elif reason == "all_data cl7":
                                    print(cl_7)

                                elif reason == "all_data cl8":
                                    print(cl_8)

                                elif reason == "all_data cl9":
                                    print(cl_9)

                                elif reason == "all_data cl10":
                                    print(cl_10)

                                elif reason == "all_data cl11":
                                    print(cl_11)

                                elif reason == "all_data cl12":
                                    print(cl_12)        

                                elif reason == "salary cl1":
                                    print(cl_1[4])

                                elif reason == "salary cl2":
                                    print(cl_2[4])

                                elif reason == "salary cl3":
                                    print(cl_3[4])

                                elif reason == "salary cl4":
                                    print(cl_4[4])

                                elif reason == "salary cl5":
                                    print(cl_5[4])

                                elif reason == "salary cl6":
                                    print(cl_6[4])

                                elif reason == "salary cl7":
                                    print(cl_7[4])

                                elif reason == "salary cl8":
                                    print(cl_8[4])

                                elif reason == "salary cl9":
                                    print(cl_9[4])

                                elif reason == "salary cl10":
                                    print(cl_10[4])

                                elif reason == "salary cl11":
                                    print(cl_11[4])

                                elif reason == "salary cl12":
                                    print(cl_12[4])        

                                elif reason == "married cl1":
                                    print(cl_1[3])

                                elif reason == "married cl2":
                                    print(cl_2[3])

                                elif reason == "married cl3":
                                    print(cl_3[3])

                                elif reason == "married cl4":
                                    print(cl_4[3])

                                elif reason == "married cl5":
                                    print(cl_5[3])

                                elif reason == "married cl6":
                                    print(cl_6[3])

                                elif reason == "married cl7":
                                    print(cl_7[3])

                                elif reason == "married cl8":
                                    print(cl_8[3])

                                elif reason == "married cl9":
                                    print(cl_9[3])

                                elif reason == "married cl10":
                                    print(cl_10[3])

                                elif reason == "married cl11":
                                    print(cl_11[3])

                                elif reason == "married cl12":
                                    print(cl_12[3])        

                                elif reason == "close" or reason == "exit":
                                    sys.exit()

                                else:
                                    print("oh sorry try again if you need any more")
                                    print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                                    break
                            else:
                                print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                                break
                        else:
                            print("wrong passowrd bye [-_-]")
                            print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                            break
                    else:
                        print("okey thank you to use us [^_^]")
                        print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                        break
                else:
                    print("sorry_cant show you this information only for manger_vip")
                    print(ascii_train.train("abdo_Dolh_99 => [<*_*>]"))
                    break

        elif user_input == cl_12[1]:
            password = input("password :".strip())
            tried = 4
            while password != cl_12[6]:
                tried -= 1
                print(f"you have {tried} to try agian")
                password = input("password :".strip())
                if tried == 0:
                    sys.exit()
            else:
                print(f"correct password hello {cl_12[1]}".capitalize())
                print("*"*50)
            while True:
                reason = input("what can i help you boss :".strip().title())
                if reason == "all_password" or reason == "all_pass":
                    clint.show_password(cl_12)

                elif reason == "copy":
                    clint.copy_code(cl_12)   

                elif reason == "opp":
                    clint.calcalate(cl_12[1])    

                elif reason == "id":
                    clint.id_cl(cl_12[1])    

                elif reason == "rate":
                    clint.rate_python(cl_12)

                elif reason == "all_data" or reason == "database":
                    data_base.database_all(cl_12)

                elif reason == "edit" or reason == "change":
                    data_base.adit_cl(cl_12[1])

                elif reason == "add":
                    data_base.add_cl(cl_12[1])

                elif reason == "delet" or reason == "del":
                    data_base.delete_cl(cl_12[1])

                elif reason == "skill cl1":
                    print(cl_1[8])

                elif reason == "skill cl2":
                    print(cl_2[8])

                elif reason == "skill cl3":
                    print(cl_3[8])

                elif reason == "skill cl4":
                    print(cl_4[8])

                elif reason == "skill cl5":
                    print(cl_5[8])

                elif reason == "skill cl6":
                    print(cl_6[8])

                elif reason == "skill cl7":
                    print(cl_7[8])

                elif reason == "skill cl8":
                    print(cl_8[8])

                elif reason == "skill cl9":
                    print(cl_9[8])

                elif reason == "skill cl10":
                    print(cl_10[8])

                elif reason == "skill cl11":
                    print(cl_11[8])

                elif reason == "skill cl12":
                    print(cl_12[8])

                elif reason == "skill cl13":
                    print(cl_13[8])            

                elif reason == "age cl1":
                    print(cl_1[2])

                elif reason == "age cl2":
                    print(cl_2[2])

                elif reason == "age cl3":
                    print(cl_3[2])

                elif reason == "age cl4":
                    print(cl_4[2])

                elif reason == "age cl5":
                    print(cl_5[2])

                elif reason == "age cl6":
                    print(cl_6[2])

                elif reason == "age cl7":
                    print(cl_7[2])

                elif reason == "age cl8":
                    print(cl_8[2])

                elif reason == "age cl9":
                    print(cl_9[2])

                elif reason == "age cl10":
                    print(cl_10[2])

                elif reason == "age cl11":
                    print(cl_11[2])

                elif reason == "age cl12":
                    print(cl_12[2])

                elif reason == "age cl13":
                    print(cl_13[2])            

                elif reason == "country cl1":
                    print(cl_1[5])

                elif reason == "country cl2":
                    print(cl_2[5])

                elif reason == "country cl3":
                    print(cl_3[5])

                elif reason == "country cl4":
                    print(cl_4[5])

                elif reason == "country cl5":
                    print(cl_5[5])

                elif reason == "country cl6":
                    print(cl_6[5])

                elif reason == "country cl7":
                    print(cl_7[5])

                elif reason == "country cl8":
                    print(cl_8[5])

                elif reason == "country cl9":
                    print(cl_9[5])

                elif reason == "country cl10":
                    print(cl_10[5])

                elif reason == "country cl11":
                    print(cl_11[5])

                elif reason == "country cl12":
                    print(cl_12[5])

                elif reason == "country cl13":
                    print(cl_13[5])            

                elif reason == "all_data cl1":
                    print(cl_1)

                elif reason == "all_data cl2":
                    print(cl_2)

                elif reason == "all_data cl3":
                    print(cl_3)

                elif reason == "all_data cl4":
                    print(cl_4)

                elif reason == "all_data cl5":
                    print(cl_5)

                elif reason == "all_data cl6":
                    print(cl_6)

                elif reason == "all_data cl7":
                    print(cl_7)

                elif reason == "all_data cl8":
                    print(cl_8)

                elif reason == "all_data cl9":
                    print(cl_9)

                elif reason == "all_data cl10":
                    print(cl_10)

                elif reason == "all_data cl11":
                    print(cl_11)

                elif reason == "all_data cl12":
                    print(cl_12)

                elif reason == "all_data cl13":
                    print(cl_13)

                elif reason == "salary cl1":
                    print(cl_1[4])

                elif reason == "salary cl2":
                    print(cl_2[4])

                elif reason == "salary cl3":
                    print(cl_3[4])

                elif reason == "salary cl4":
                    print(cl_4[4])

                elif reason == "salary cl5":
                    print(cl_5[4])

                elif reason == "salary cl6":
                    print(cl_6[4])

                elif reason == "salary cl7":
                    print(cl_7[4])

                elif reason == "salary cl8":
                    print(cl_8[4])

                elif reason == "salary cl9":
                    print(cl_9[4])

                elif reason == "salary cl10":
                    print(cl_10[4])

                elif reason == "salary cl11":
                    print(cl_11[4])

                elif reason == "salary cl12":
                    print(cl_12[4])  

                elif reason == "salary cl13":
                    print(cl_13[4])          

                elif reason == "married cl1":
                    print(cl_1[3])

                elif reason == "married cl2":
                    print(cl_2[3])

                elif reason == "married cl3":
                    print(cl_3[3])

                elif reason == "married cl4":
                    print(cl_4[3])

                elif reason == "married cl5":
                    print(cl_5[3])

                elif reason == "married cl6":
                    print(cl_6[3])

                elif reason == "married cl7":
                    print(cl_7[3])

                elif reason == "married cl8":
                    print(cl_8[3])

                elif reason == "married cl9":
                    print(cl_9[3])

                elif reason == "married cl10":
                    print(cl_10[3])

                elif reason == "married cl11":
                    print(cl_11[3])

                elif reason == "married cl12":
                    print(cl_12[3])

                elif reason == "married cl13":
                    print(cl_13[3])            

                elif reason == "close" or reason == "exit":
                    sys.exit()

                else:
                    print("oh sorry try again if you need any more")
                    break
            else:
                break
        else:
            print("this user name not agsist her ,try agin".title())
            break
else:
    print("i cant understand you please try agian")
    sys.exit()