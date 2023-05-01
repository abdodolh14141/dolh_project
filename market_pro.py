from pymongo import mongo_client
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import pprint
import numpy as np
import re
import time
import pylint.lint

if __name__ == '__main__':
    load_dotenv(find_dotenv())
    printer = pprint.PrettyPrinter()
    clint = mongo_client.MongoClient('mongodb+srv://abdodolh14141:abdodolh14141@data.2n75kkb.mongodb.net/test')


sqlite_db = clint.data_clint
data_mongo = sqlite_db.sqlite3
help_frame = data_mongo.find().sort('user_id')
df_user = pd.DataFrame(help_frame)


phones = sqlite_db.mobile_sqlite3
all_data = phones.find().sort('_id')
df_phone = pd.DataFrame(all_data)
sign = sqlite_db.data_market

laptop = sqlite_db.labtob
all_data_lab = laptop.find().sort('laptop_ID')
df_lap = pd.DataFrame(all_data_lab)

class market():
    def find_id():
        try:
            ID_phone = int(input('user_id => ').title())
            answer1 = phones.find_one({'_id':ID_phone})

        except EOFError as er:
            print(f'error => {er}')

        except ValueError as ev:
            print(f'error => {ev}')

        finally:
            printer.pprint(answer1)

    def save_data_clint():
        user_name = input('user_name :'.title())
        email_user = input('email :'.title())
        time_bot = time.ctime(time.time())
        sign.insert_one({'name':user_name,'email':email_user,'time':time_bot})

    def delete_sign():
        quz_del = input('so you want delete sign :'.title())
        if quz_del == 'yes':
            name_del = input('user_name to delete :'.title())
            sign.delete_one({'name':name_del})
            print('sucess delete'.title())
        else:
            print('okey bye'.title())

    def frame_all():
        print(df_phone.to_string(index=False, columns=['_id', 'name', 'rate']))
        market.find_id()

    def search_phone():
        print(df_phone.to_string(index=False, columns=['_id', 'name', 'rate']))
        find1 = input('marka => ')
        answer = df_phone.loc[df_phone['name'].str.contains(find1, regex=True, flags=re.I)]
        print(answer.to_string(index=False, columns=['_id', 'name', 'rate']))
        market.find_id()
     
    def rebot_clint():
        try:
            commint = sqlite_db.rebot
            name22 = input('your name => '.title())
            massage = input('put your massage => '.title())
            data =  {
                'name':name22,
                'report':massage
            }
            commint.insert_one(data)

        except ValueError as ev:
            print(f'error => {ev}')

        except EOFError as er:
            print(f'error => {er}')

        finally:
            print('sucess report'.title())

class labtob_1(market):
    def find_lab():
        try:
            ID_lap_find = int(input('laptop_ID => '))
            answer2 = laptop.find_one({'laptop_ID':ID_lap_find})

        except EOFError as er:
            print(f'error => {er}')

        except ValueError as ev:
            print(f'error => {ev}')

        finally:
            printer.pprint(answer2)

    def search_laptop():
        print(df_lap.to_string(index=False, columns=['laptop_ID', 'Company',
                                            'Product', 'Cpu', 'Ram', 'Gpu']))

        find_l = str(input('marka => '.title()))
        answer = df_lap.loc[df_lap['Company'].str.contains(find_l, regex=True, flags=re.I)]
        print(answer.to_string(index=False, columns=['laptop_ID', 'Company',
                                            'Product', 'Cpu', 'Ram', 'Gpu']))
        labtob_1.find_lab()

    def all_lab():
        print(df_lap.to_string(index=False, columns=['laptop_ID', 'Company',
                                            'Product', 'Cpu', 'Ram', 'Gpu']))
        labtob_1.find_lab()
       

class admin(market):
    def insert_test_doc():
        try:
            userID_input = int(input('user_id =+>'))
            name1 = input('name =+> ')
            age1 = int(input('age =+> '))
            married1 = input('married =+> ')
            salary1 = int(input('salary =+> '))
            country1 = input('country =+> ')
            password1 = input('password =+> ')
            genter1 = input('genter =+> ')
            skill1 = input('skill =+> ')

            data = {
                'user_id':userID_input,
                'name':name1,
                'age':age1,
                'married':married1,
                'salary':salary1,
                'country':country1,
                'password':password1,
                'genter':genter1,
                'skill':skill1
                }
            data_mongo.insert_one(data)

        except ValueError as ev:
            print(f'error => {ev}')

        except EOFError as er:
            print(f' error => {er}')

        finally:
            print('success add')

    def show_sign():
        for i in sign.find({}):
            printer.pprint(i)

        market.delete_sign()

    def add_phone():
        try:
            ID_ = int(input('ID user :'))
            name_mobile = input('name mobile :')
            rate_new = input('rate :')
            review_new = input('review phone :')
            memory_new = input('storage and ram new phone :')
            battey_new = int(input('battery new phone :'))
            screen_new = input('screen size (inches) :')   
            camera_new = input('camerea (MP) :')
            gpu = input('processor :')

            data = {
                '_id':ID_,
                'name':name_mobile,
                'reviews':review_new,
                'rate':rate_new,
                'memory ':memory_new,
                'screen':screen_new,
                'camera':screen_new,
                'battery':battey_new,
                'processor':gpu
            }
            phones.insert_one(data).inserted_id()

        except Exception as ex:
            print(f'error => {ex}')

        finally:
            print('success add phone'.title())

    def replace():
        print(df_user.head(50))
        quision = input('changed what => ')
        try:
            if quision == 'name':
                user_id = input('old name => ')
                new_name = input('new name => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"name": new_name}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'age':
                user_id = int(input('user_id => '))
                new_age = input('new age => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"age": new_age}}

                data_mongo.update_one(myquery, newvalues)
            elif quision == 'salary':
                user_id = int(input('user_id => '))
                new_salary = input('new name => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"salary": new_salary}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'skill':
                user_id = int(input('user_id => '))
                new_skill = input('new skill => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"skill": new_skill}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'married':
                user_id = int(input('user_id => '))
                new_married = input('new married => ')
                myquery = {"user_id": user_id}
                newvalues = { "$set": {"married": new_married}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'password':
                user_id = int(input('user_id => '))
                new_pass = input('new password => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"password": new_pass}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'country':
                user_id = int(input('user_id => '))
                new_sity = input('new country => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"country": new_sity}}
                data_mongo.update_one(myquery, newvalues)
                
        except ValueError as ev:
            print(f'error => {ev}')

        except EOFError as er:
            print(f'error => {er}')

        finally:
            print('success change'.title())
        
    def drop_admin():
        try:
            user_id = int(input('put here user_id => '.strip()))
            data_mongo.delete_one({'user_id':user_id})

        except ValueError as ev:
            print(f'error ==> {ev}')

        except EOFError as er:
            print(f'error ==> {er}')

        finally:
            print('succes delet'.title())

    def drop_phone():
        try:
            user_id = int(input('put here user_id => '.strip()))
            phones.delete_one({'user_id':user_id})
        except EOFError as er:
            print(f'error => {er}')
        finally:
            print('sucess delet'.title())

    def drop_laptop():
        try:
            user_id = input('put here laptop_ID => '.strip())
            laptop.delete_one({'user_id':user_id})
        except EOFError as er:
            print(f'error => {er}')
        finally:
            print('sucess delet laptop'.title())
            
    def comment_help():
        commint = sqlite_db.rebot
        use = np.array([['(write , input)'],['(read , show)']])
        print(use)
        comment_help_1 = input("how can i help you problem ==> ".title())
        if comment_help_1 == 'show' or 'read':
            add_data = commint.find({})
            for row in add_data:
                printer.pprint(row)

            quz_delet = input('do you want delet report => '.title())

            if quz_delet == 'yes':
                try:
                    name = str(input('name => '))
                    commint.delete_one({'name': name})

                except EOFError as er:
                    print(f'error => {er}'.title())

                except ValueError as ev:
                    print(f'error => {ev}'.title())

                finally:
                    print('sucess delet'.title())

            else:
                print('okey thanks you'.title())

        elif comment_help_1 == 'input' or 'write':
            name_user22 = input('your name => ')
            rebot = input('put your massage => '.title())
            data =  {
                'report':rebot,
                'name':name_user22
            }
            commint.insert_one(data)

        else:
            print('sorry please try agian'.title())
            exit()

    def update_phones():
        try:
            print(df_phone.to_string(index=False, columns=['_id', 'name', 'rate']))
            id_find = input('user_id => ')
            new_pp = input('put any you want change => ')
            new_value = input('new value => ')
            old = {'user_id':id_find}
            new_reslt = {'$set':{new_pp:new_value}}
            phones.update_one(old, new_reslt)

        except EOFError as er:
            print(f'error => {er}')

        finally:
            print('sucess change'.title())

    def rate_python():
        try:
            rate1 = ['market_pro.py']
            pylint.lint.Run(rate1)
        except SyntaxError as er:
            print(f"error => {er}")
        finally:
            print('success rate'.title())

    def update_lab():
        try:
            print(df_lap.to_string(index=False, columns=['laptop_ID', 'Company',
                                            'Product', 'Cpu', 'Ram', 'Gpu']))
            id_find = input('laptop_ID => ')
            new_pp = input('put any you want change => ')
            new_value = input('new value => ')
            old = {'laptop_ID':id_find}
            new_reslt = {'$set':{new_pp:new_value}}
            phones.update_one(old, new_reslt)

        except EOFError as er:
            print(f'error => {er}')

        finally:
            print('sucess change')

    def show_phones():
        print(df_phone.to_string(index=False, columns=['_id', 'name', 'rate']))
        market.find_id()

    def show_lab():
        print(df_lap.to_string(index=False, columns=['laptop_ID', 'Company',
                                            'Product', 'Cpu', 'Ram', 'Gpu']))
        labtob_1.find_lab()




class tool(market):
    def tool_admin():
        while True:
                list_user_admin = np.array(['(delete or del (admin or phone or laptop)',
                                            '(report or comment)', '(all_data (admin or phones or laptop))',
                                            '(update or change(admin or phone)',
                                            '(add (admin or phone))', '(update laptop)', '(show sign)', 'rate code'])
                print(list_user_admin)
                help_1 = input('what can i help you => '.title())
                if help_1 == 'all_data admin' or help_1 == 'database':
                    print(df_user)

                elif help_1 == 'change admin' or help_1 == 'update admin':
                    admin.replace()

                elif help_1 == 'update laptop':
                    admin.update_lab()

                elif help_1 == 'rate code':
                    admin.rate_python()

                elif help_1 == 'show sign':
                    admin.show_sign()

                elif help_1 == 'all_data laptop':
                    admin.show_lab()

                elif help_1 == 'add phone':
                    admin.add_phone()

                elif help_1 == 'delete admin' or help_1 == 'del admin':
                    admin.drop_admin()

                elif help_1 == 'delete phone' or help_1 == 'del phone':
                    admin.drop_phone()

                elif help_1 == 'delete laptop' or help_1 == 'del laptop':
                    admin.drop_laptop()

                elif help_1 == 'report' or help_1 == 'comment':
                    admin.comment_help()

                elif help_1 == 'update phone' or help_1 == 'change phone':
                    admin.update_phones()

                elif help_1 == 'all_data phone' or help_1 == 'phones':
                    admin.show_phones()

                elif help_1 == 'find phone' or help_1 == 'search':
                    market.search_phone()

                elif help_1 == 'add admin':
                    admin.insert_test_doc()

                elif help_1 == 'close' or help_1 == 'cls':
                    exit()

                else:
                    print('error please try agian'.title())
                    exit()

    def tool_clint():
            market.save_data_clint()
            elc = input('phones or laptop => '.title())
            while True:
                if elc == 'phone' or elc == 'phones':
                    list_use_clint = np.array(['(all phone or phones)','(find marka & search)','(report or comment)'])
                    print(list_use_clint)

                    qusison = input('what can halp you => '.title())

                    if qusison == 'all phone' or qusison == 'phones':
                        market.frame_all()

                    elif qusison == 'find marka' or qusison == 'search':
                        market.search_phone()

                    elif qusison == 'report' or qusison == 'comment':
                        market.rebot_clint()

                    elif qusison == 'close' or qusison == 'cls':
                        exit()

                    else:
                        print("i can't understand you please try agian".title())
                        break

                elif elc == 'laptop' or 'laptops':
                    list_use_clint = np.array([['(all laptop or laptops)','(find lap)'],
                                               ['(find marka & search lap)','(report)']])
                    print(list_use_clint)
                    qusison = input('what can halp you => '.title())

                    if qusison == 'all laptop' or qusison == 'laptops':
                        labtob_1.all_lab()

                    elif qusison == 'find lap':
                        labtob_1.find_lab()

                    elif qusison == 'find marka' or qusison ==  'search lap':
                        labtob_1.search_laptop()

                    elif qusison == 'report':
                        market.rebot_clint()

                    elif qusison == 'close' or qusison == 'cls':
                        exit()

                    else:
                        print("i can't understand you please try agian".title())
                        break
                else:
                    exit()

while True:
    if __name__ == '__main__':
        choise_user = input('admin or clint => '.title())
        if choise_user == 'admin':
            user = input('user_name => '.title())
            if user == df_user.iloc[0][2] or user ==df_user.iloc[1][2]\
                or user ==df_user.iloc[2][2] or user ==df_user.iloc[3][2]\
                or user ==df_user.iloc[4][2] or user ==df_user.iloc[5][2] or user ==df_user.iloc[6][2]\
                or user ==df_user.iloc[7][2] or user ==df_user.iloc[8][2] or user ==df_user.iloc[9][2]\
                or user ==df_user.iloc[10][2] or user ==df_user.iloc[11][2] or user ==df_user.iloc[12][2]\
                or user ==df_user.iloc[13][2] or user ==df_user.iloc[14][2]: 

                if user == df_user.iloc[0][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[0][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[1][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[1][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[2][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[2][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[3][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[3][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[4][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[4][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[5][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[5][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[6][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[6][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[7][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[7][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[8][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[8][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[9][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[9][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[10][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[10][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[11][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[11][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[12][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[12][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                elif user == df_user.iloc[13][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[13][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    
                        
                elif user == df_user.iloc[14][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[14][7]:
                        bot_time = time.ctime(time.time())
                        sign.insert_one({'name':user,'password':pass_input,'time':bot_time})
                        tool.tool_admin()
                    else:
                        print('wrong password please try agian'.title())
            
            else:
                exit()
            
        elif choise_user == 'clint':
            tool.tool_clint()

        else:
            print('error please try agian'.title())
            exit()

    else:
        exit()