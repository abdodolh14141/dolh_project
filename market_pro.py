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

    def rebot_clint():
        try:
            commint = sqlite_db.rebot
            name_user22 = input('your name => '.title())
            rebot = input('put your massage => '.title())
            data =  {
                'report':rebot,
                'name':name_user22
            }
            commint.insert_one(data)
        except ValueError as ev:
            print(f'error => {ev}')
        except EOFError as er:
            print(f'error => {er}')
        finally:
            print('sucess')
       

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

        else:
            print('not found please try agian')    

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

    def drop_phone():
        user_id = input('put here user_id or name => '.strip())
        if user_id == int:
            phones.delete_one({'user_id':user_id})

        else:
            phones.delete_one({'name':f"{user_id}"})
            
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
            print(frame_phone_all.to_string())
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

    def show_phones():
        print(frame_phone_all.to_string())

class tool(market):
    def tool_admin():
        while True:
                list_user_admin = np.array(['age','find hack','(delet or del) (admin or phone)','rebot',
                                             'all_data (admin or phone)', '(update or change) (admin or phone)', 'add admin'])
                print(list_user_admin)
                help_1 = input('what can i help you => ')
                if help_1 == 'all_data admin' or help_1 == 'database':
                    print(frame)

                elif help_1 == 'change admin' or help_1 == 'update admin':
                    admin.replace()

                elif help_1 == 'find hack':
                    admin.find_hack()

                elif help_1 == 'delet admin' or help_1 == 'del admin':
                    admin.drop_admin()

                elif help_1 == 'delet phone' or help_1 == 'del phone':
                    admin.drop_phone()

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
                    market.serach()

                elif help_1 == 'add admin':
                    admin.insert_test_doc()

                elif help_1 == 'close' or help_1 == 'cls':
                    exit()

                else:
                    print('error please try agian')
                    break

    def tool_clint():
        while True:
            list_use_clint = np.array(['all phone','find', 'rebot','find marka & search','report'])
            print(list_use_clint)
            qusison = input('what can halp you => ')
            if qusison == 'all_data':
                market.frame_all()
            elif qusison == 'find':
                market.find()
            elif qusison == 'find marka' or qusison == 'search':
                market.serach()
            elif qusison == 'report':
                market.rebot_clint()
            else:
                print("i can't understand you please try agian".title())
                break

while True:
    if __name__ == '__main__':
        knowlage = input('admin or clint => ')
        if knowlage == 'admin':
            user = input('user_name => ')

            if user == frame.iloc[0][2] or user == frame.iloc[1][2]\
                or user == frame.iloc[2][2] or user == frame.iloc[3][2]\
                or user == frame.iloc[4][2] or user == frame.iloc[5][2] or user == frame.iloc[6][2]\
                or user == frame.iloc[7][2] or user == frame.iloc[8][2] or user == frame.iloc[9][2]\
                or user == frame.iloc[10][2] or user == frame.iloc[11][2] or user == frame.iloc[12][2]\
                or user == frame.iloc[13][2] or user == frame.iloc[14][2]: 

                if user == frame.iloc[0][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[0][7]:
                        tool.tool_admin()

                elif user == frame.iloc[1][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[1][7]:
                        tool.tool_admin()

                elif user == frame.iloc[2][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[2][7]:
                        tool.tool_admin()

                elif user == frame.iloc[3][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[3][7]:
                        tool.tool_admin()

                elif user == frame.iloc[4][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[4][7]:
                        tool.tool_admin()

                elif user == frame.iloc[5][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[5][7]:
                        tool.tool_admin()

                elif user == frame.iloc[6][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[6][7]:
                        tool.tool_admin()

                elif user == frame.iloc[7][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[7][7]:
                        tool.tool_admin()

                elif user == frame.iloc[8][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[8][7]:
                        tool.tool_admin()

                elif user == frame.iloc[9][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[9][7]:
                        tool.tool_admin()

                elif user == frame.iloc[10][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[10][7]:
                        tool.tool_admin()

                elif user == frame.iloc[11][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[11][7]:
                        tool.tool_admin()

                elif user == frame.iloc[12][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[12][7]:
                        tool.tool_admin()

                elif user == frame.iloc[13][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[13][7]:
                        tool.tool_admin()
                        
                elif user == frame.iloc[14][2]:
                    pass_input = input('password => ')
                    if pass_input == frame.iloc[14][7]:
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


