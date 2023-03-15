from pymongo import mongo_client
from dotenv import load_dotenv, find_dotenv
import pandas as pd
import pprint
import numpy as np
load_dotenv(find_dotenv())
printer = pprint.PrettyPrinter()
clint = mongo_client.MongoClient('mongodb+srv://abdodolh14141:abdodolh14141@data.2n75kkb.mongodb.net/test')
sqlite_db = clint.data_clint
data_mongo = sqlite_db.sqlite3
help_frame = data_mongo.find()
frame = pd.DataFrame(help_frame)
phones = sqlite_db.phones
all_data = phones.find()
frame_phone_all = pd.DataFrame(all_data, columns=['user_id', 'names', 'memory', 'stars'])
class market():
    def find_id():
        user_id = input('user_id => ')
        a = phones.find_one({'user_id':user_id})
        printer.pprint(a)

    def frame_all():
        print(frame_phone_all.to_string())
        market.find_id()

    def find():
        print(frame_phone_all.head(50))
        market.find_id()

    def serach():
        print(frame_phone_all.to_string())
        marka_find = input('name marka =>'.strip().title())
        list_find = frame_phone_all.loc[frame_phone_all['names'].str.contains(f'{marka_find}')]
        print(list_find.to_string())
        market.find_id()

class admin(market):
    def insert_test_doc():
        try:
            userID_input = input('user_id =+>')
            name1 = input('name =+>')
            age1 = input('age =+>')
            married1 = input('married =+>')
            salary1 = input('salary =+>')
            country1 = input('country =+>')
            password1 = input('password =+>')
            genter1 = input('genter =+>')
            skill1 = input('skill =+>')
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


    def find_hack():
        hack = data_mongo.find({'skill' : 'cyber secuirty'})
        for row in hack:
            printer.pprint(row)

    def count_of_people():
        a = data_mongo.count_documents(filter={})
        print('number of people count',a)

    def find():
        print(frame)
        user_id = input('user_id => ')
        answer = phones.find_one({'user_id':user_id})
        printer.pprint(answer)
        

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
        print(frame.head(50))
        quision = input('changed what => ')
        if quision == 'name':
            old_name = input('old name => ')
            new_name = input('new name => ')
            myquery = { "name": old_name}
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
            myquery = { "user_id": f"{user_id}"}
            newvalues = { "$set": {"password": f"{new_pass}"}}
            data_mongo.update_one(myquery, newvalues)
        elif quision == 'country':
            user_id = int(input('user_id => '))
            new_sity = input('new country => ')
            myquery = { "user_id": f"{user_id}"}
            newvalues = { "$set": {"country": f"{new_sity}"}}
            data_mongo.update_one(myquery, newvalues)
        else:
            print('not found please try agian')    

    def drop():
        user_id = input('put here user_id or name => '.strip())
        if user_id == int:
            data_mongo.delete_one({'user_id':f"{user_id}"})
        else:
            data_mongo.delete_one({'name':f"{user_id}"})

    def comment_help():
        comment_help_1 = input("how can i help you problem ==>")
        if comment_help_1 == 'show' or comment_help_1 == 'read':
            aa = data_mongo.find_one({'user_id':'11'})
            printer.pprint(aa)
        elif comment_help_1 == 'input' or comment_help_1 == 'write':
            rebot_masg = input('massage to rebot ==>')
            data_mongo.update_one({"user_id":"11"}, {"$addToSet":{"comment": f"{rebot_masg}"}})
        else:
            exit()

    def update_phones():
        try:
            print(frame_phone_all.to_string())
            id_find = input('user_id => ')
            new_pp = input('put any you want change => ')
            new_value = input('new value => ')
            old = {'user_id':f"{id_find}"}
            new_reslt = {'$set':{f"{new_pp}":f"{new_value}"}}
            phones.update_one(old, new_reslt)
        except EOFError as er:
            print(f'error => {er}')
        finally:
            print('sucess change')

    def show_phones():
        print(frame_phone_all())
        market.find_id()


while True:
    list_user_admin = np.array(['change','find hack','delet or del', 'rebot', 'all_data phones', 'update phone'])
    knowlage = input('admin or clint => ')
    if knowlage == 'admin':
        user = input('user_name => ')
        if user == frame.iloc[0][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[0][7]:
                print(list_user_admin)
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'update phone' or help_1 == 'change phone':
                    admin.update_phones()
                elif help_1 == 'all_data phones':
                    admin.show_phones()
                else:
                    print('error please try agian')
                    break

        elif user == frame.iloc[1][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[1][7]:
                print(list_user_admin)
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break

        elif user == frame.iloc[1][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[1][7]:
                print(list_user_admin)
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break

        elif user == frame.iloc[2][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[2][7]:
                print(list_user_admin)
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break

        elif user == frame.iloc[3][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[3][7]:
                print(list_user_admin)
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break

        elif user == frame.iloc[4][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[4][7]:
                print(f'success sign hello {frame.iloc[4][2]}')
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break

        elif user == frame.iloc[5][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[5][7]:
                print(f'success sign hello {frame.iloc[5][2]}')
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break
        elif user == frame.iloc[6][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[6][7]:
                print(f'success sign hello {frame.iloc[5][2]}')
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break
        elif user == frame.iloc[7][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[7][7]:
                print(f'success sign hello {frame.iloc[5][2]}')
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break
        elif user == frame.iloc[8][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[8][7]:
                print(f'success sign hello {frame.iloc[5][2]}')
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break
        elif user == frame.iloc[9][2]:
            pass_input = input('password => ')
            if pass_input == frame.iloc[5][7]:
                print(f'success sign hello {frame.iloc[9][2]}')
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data' or help_1 == 'database':
                    print(frame)
                elif help_1 == 'change':
                    print(frame)
                    admin.replace()
                elif help_1 == 'find hack':
                    admin.find_hack()
                elif help_1 == 'delet' or help_1 == 'del':
                    admin.drop()
                elif help_1 == 'rebot':
                    admin.comment_help()
                elif help_1 == 'age':
                    admin.get_age_arange()
                else:
                    print('error please try agian')
                    break
        else:
            exit()
    elif knowlage == 'clint':
        qusison = input('what can halp you => ')
        if qusison == 'all_data':
            market.frame_all()
        elif qusison == 'find':
            market.find()
        elif qusison == 'find marka' or qusison == 'search':
            market.serach()
    else:
        break


