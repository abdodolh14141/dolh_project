from pymongo import mongo_client
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import pprint
import numpy as np
import re
from bson.objectid import ObjectId

load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()
clint = mongo_client.MongoClient('mongodb+srv://abdodolh14141:abdodolh14141@data.2n75kkb.mongodb.net/test')


sqlite_db = clint.data_clint
data_mongo = sqlite_db.sqlite3
help_frame = data_mongo.find().sort('user_id')
df_user = pd.DataFrame(help_frame)


phones = sqlite_db.new_phone
all_data = phones.find()
df_phone = pd.DataFrame(all_data)


laptop = sqlite_db.labtob
all_data_lab = laptop.find().sort('laptop_ID')
df_lap = pd.DataFrame(all_data_lab)

class market():

    def find_id():
        try:
            ID_phone = int(input('user_id => '))
            answer1 = phones.find_one({'user_id':ID_phone})

        except EOFError as er:
            print(f'error => {er}')

        except ValueError as ev:
            print(f'error => {ev}')

        finally:
            printer.pprint(answer1)

    def frame_all():
        print(df_all_phone.to_string())
        market.find_id()

    def search_phone():
        print(df_phone.to_string(index=False, columns=['user_id', 'Brand', 'Model', 'Storage ', 'RAM ']))
        find1 = input('marka => ')
        answer = df_phone.loc[df_phone['Brand'].str.contains(find1, regex=True, flags=re.I)]
        print(answer.to_string(index=False, columns=['user_id', 'Brand', 'Model', 'Storage ', 'RAM ']))
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
            print('sucess')

class labtob_1(market):
    def find_lab():
        try:
            ID_lap_find = int(input('laptop_ID => '))
            a = df_lap.iloc[ID_lap_find]

        except EOFError as er:
            print(f'error => {er}')

        except ValueError as ev:
            print(f'error => {ev}')

        finally:
            printer.pprint(a)

    def search_laptop():
        print(df_lap.to_string(index=False, columns=['laptop_ID', 'Company', 'Product', 'Cpu', 'Ram', 'Gpu']))
        find_l = str(input('marka => '.title()))
        answer = df_lap.loc[df_lap['Company'].str.contains(find_l, regex=True, flags=re.I)]
        print(answer.to_string(index=False, columns=['laptop_ID', 'Company', 'Product', 'Cpu', 'Ram', 'Gpu']))
        labtob_1.find_lab()
    

    def all_lab():
        print(df_all_lap.to_string())
        labtob_1.find_lab()
       

class admin(market):

    def insert_test_doc():

        try:

            userID_input = input('user_id =+> '.title())
            name1 = input('name =+> '.title())
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

    def add_phone():

        try:

            model_new = input('model new phone => ')
            brand_new = input('brand new phone => ')
            storage_new = input('storage new phone => ')
            ram_new = input('ram new phone => ')
            batter_new = int(input('battery new phone => '))
            screen_new = input('screen size (inches) => ')   
            camera_new = input('camerea (MP) => ')
            price_new = int(input('price => '))
            user_new = int(input('user_id => '))

            data = {
                'user_id':user_new,
                'Brand':brand_new,
                'Model':model_new,
                'Storage ':storage_new,
                'RAM ':ram_new,
                'Screen Size (inches)':screen_new,
                'Camera (MP)':screen_new,
                'Battery Capacity (mAh)':batter_new,
                'Price':price_new
            }
            
            phones.insert_one(data).inserted_id()

        except Exception as ex:
            print(f'error => {ex}')

        finally:
            print('success add phone'.title())


    def find_hack():
        hack = data_mongo.find({'skill' : 'cyber secuirty'})
        for row in hack:
            printer.pprint(row)

    def get_age_arange():
        min_age = int(input('put min age => '.strip()))
        max_age = int(input('put max age => '.strip()))
        query = {'$and':[
            {'age':{'$gte':min_age}},
            {'age':{'$lte':max_age}}
        ]}
        a = data_mongo.find(query).sort('age')
        for people in a:
            printer.pprint(people)


    def replace():
        print(df_user.head(50))
        quision = input('changed what => ')
        try:
            if quision == 'name':
                user_id = input('old name => ')
                new_name = input('new name => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"name": f"{new_name}"}}
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
                newvalues = { "$set": {"skill": f"{new_skill}"}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'married':
                user_id = int(input('user_id => '))
                new_married = input('new married => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"married": new_married}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'password':
                user_id = int(input('user_id => '))
                new_pass = input('new password => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"password": f"{new_pass}"}}
                data_mongo.update_one(myquery, newvalues)

            elif quision == 'country':
                user_id = int(input('user_id => '))
                new_sity = input('new country => ')
                myquery = { "user_id": user_id}
                newvalues = { "$set": {"country": f"{new_sity}"}}
                data_mongo.update_one(myquery, newvalues)
                
        except ValueError as ev:
            print(f'error => {ev}')
        except EOFError as er:
            print(f'error => {er}')
        finally:
            print('sucess change')



            print('success change'.title())
        
    def drop_admin():
        try:
            user_id = input('put here user_id or name => '.strip())
            if user_id == int:
                data_mongo.delete_one({'user_id':user_id})
            elif user_id == str:
                data_mongo.delete_one({'name':f"{user_id}"})
            else:
                exit()
        except ValueError as ev:
            print(f'error ==> {ev}')
        except EOFError as er:
            print(f'error ==> {er}')
        finally:
            print('succes delet')

    def drop_ID():
        try:
            object_1 = input('object_id => '.title())
            aa = ObjectId(object_1)
            phones.delete_one({'_id':aa})
        except EOFError as er:
            print(f'error => {er}')
        finally:
            print('success delet')

    def drop_phone():
        try:
            user_id = int(input('put here user_id => '.strip()))
            phones.delete_one({'user_id':user_id})
        except EOFError as er:
            print('error => er')
        finally:
            print('sucess delet'.title())

    def drop_laptop():
        user_id = input('put here laptop_ID => '.strip())
        if user_id == int:
            laptop.delete_one({'laptop_ID':user_id})
        else:
            exit()
            
    def comment_help():
        commint = sqlite_db.rebot
        use = ['(write , input) or (read , show)'.title()]
        print(use)
        comment_help_1 = input("how can i help you problem ==> ".title())
        if comment_help_1 == 'show' or comment_help_1 == 'read':
            add_data = commint.find({})
            for row in add_data:
                printer.pprint(row)
            delet = input('do you want delet report => ')
            if delet == 'yes':
                name = input('name => ')
                commint.delete_one({'name':f'{name}'})
            else:
                print('okey thanks you')

        elif comment_help_1 == 'input' or comment_help_1 == 'write':
            name_user22 = input('your name => ')
            rebot = input('put your massage => '.title())
            data =  {
                'report':rebot,
                'name':name_user22
            }
            commint.insert_one(data)

        else:
            exit()

    def update_phones():
        try:
            print(df_all_phone.to_string())
            id_find = input('user_id => ')
            new_pp = input('put any you want change => ')
            new_value = input('new value => ')
            old = {'user_id':id_find}
            new_reslt = {'$set':{f"{new_pp}":f"{new_value}"}}
            phones.update_one(old, new_reslt)

        except EOFError as er:
            print(f'error => {er}')

        finally:
            print('sucess change')

    def update_lab():
        try:
            print(df_all_lap.to_string())
            id_find = input('laptop_ID => ')
            new_pp = input('put any you want change => ')
            new_value = input('new value => ')
            old = {'laptop_ID':id_find}
            new_reslt = {'$set':{f"{new_pp}":f"{new_value}"}}
            phones.update_one(old, new_reslt)

        except EOFError as er:
            print(f'error => {er}')

        finally:
            print('sucess change')

    def show_phones():
        print(df_all_phone.to_string())
        market.find_id()

    def show_lab():
        print(df_all_lap.to_string())
        labtob_1.find_lab()

class tool(market):
    def tool_admin():
        while True:
                list_user_admin = np.array(['(age)','(find hack)', '(delet or del (admin or phone or laptop)',
                                            '(report or comment)', '(all_data (admin or phone or laptop))',
                                            '(update or change(admin or phone)',
                                            '(add (admin or phone))', '(update laptop)',
                                            '(delet (phone object))'])
                print(list_user_admin)
                help_1 = input('what can i help you => ')

                if help_1 == 'all_data admin' or help_1 == 'database':
                    print(df_user)

                elif help_1 == 'change admin' or help_1 == 'update admin':
                    admin.replace()

                elif help_1 == 'update laptop':
                    admin.update_lab()

                elif help_1 == 'all_data laptop':
                    admin.show_lab()

                elif help_1 == 'find hack':
                    admin.find_hack()

                elif help_1 == 'add phone':
                    admin.add_phone()

                elif help_1 == 'delet admin' or help_1 == 'del admin':
                    admin.drop_admin()

                elif help_1 == 'delet phone' or help_1 == 'del phone':
                    admin.drop_phone()

                elif help_1 == 'delet laptop' or help_1 == 'del laptop':
                    admin.drop_laptop()

                elif help_1 == 'report' or help_1 == 'comment':
                    admin.comment_help()

                elif help_1 == 'age' or help_1 == 'find age':
                    admin.get_age_arange()

                elif help_1 == 'rebot' or help_1 == 'comment':
                    admin.comment_help()

                elif help_1 == 'update phone' or help_1 == 'change phone':
                    admin.update_phones()

                elif help_1 == 'all_data phone' or help_1 == 'phone':
                    admin.show_phones()

                elif help_1 == 'find phone' or help_1 == 'search':
                    market.search_phone()

                elif help_1 == 'add admin':
                    admin.insert_test_doc()

                elif help_1 == 'delet phone object':
                        admin.drop_ID()

                elif help_1 == 'close' or help_1 == 'cls':
                    exit()

                else:
                    print('error please try agian')
                    break

    def tool_clint():
            elc = input('phones or laptop => '.title())
            while True:
                if elc == 'phone':
                    list_use_clint = np.array(['(all phone or phones)','(find marka & search)','(report or comment)'])
                    print(list_use_clint)

                    qusison = input('what can halp you => ')

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

                elif elc == 'laptop':
                    list_use_clint = np.array([['(all laptop or laptops)','(find lap)'],
                                               ['(find marka & search lap)','(report)']])
                    print(list_use_clint)
                    qusison = input('what can halp you => ')

                    if qusison == 'all laptop' or qusison == 'laptops':
                        labtob_1.all_lab()

                    elif qusison == 'find lap':
                        labtob_1.find_lab()

                    elif qusison == 'find marka' or qusison == 'search lap':
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
        knowlage = input('admin or clint => '.title())
        if knowlage == 'admin':
            user = input('user_name => ')

            if user == df_user.iloc[0][2] or user == df_user.iloc[1][2]\
                or user == df_user.iloc[2][2] or user == df_user.iloc[3][2]\
                or user == df_user.iloc[4][2] or user == df_user.iloc[5][2] or user == df_user.iloc[6][2]\
                or user == df_user.iloc[7][2] or user == df_user.iloc[8][2] or user == df_user.iloc[9][2]\
                or user == df_user.iloc[10][2] or user == df_user.iloc[11][2] or user == df_user.iloc[12][2]\
                or user == df_user.iloc[13][2] or user == df_user.iloc[14][2]: 

                if user == df_user.iloc[0][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[0][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[1][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[1][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[2][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[2][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[3][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[3][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[4][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[4][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[5][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[5][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[6][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[6][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[7][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[7][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[8][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[8][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[9][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[9][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[10][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[10][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[11][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[11][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[12][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[12][7]:
                        tool.tool_admin()

                elif user == df_user.iloc[13][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[13][7]:
                        tool.tool_admin()
                        
                elif user == df_user.iloc[14][2]:
                    pass_input = input('password => ')
                    if pass_input == df_user.iloc[14][7]:
                        tool.tool_admin()
                else:
                    print('wrong password please try agian')
            
            else:
                exit()
            
        elif knowlage == 'clint':
            tool.tool_clint()

        else:
            print('not found answer please try agian'.title())
            break
    else:
        exit()


