import db_app
import datetime
import random

record = {
    "user_name": "Peter",
    "item": "Stadium",
    "quantity": 10,
    "date": "2018-01-01",
    "time": "10:43",
    "_id": "1212"
}

item = "godis"
new_item = "GODIS"

def setting_time():
    date = datetime.datetime.now()
    todays_date = str(date.year) + "-" + str(date.month) + "-" + str(date.day)
    current_time = str(date.hour) + ":" + str(date.minute) + ":" + str(date.second)
    time = [todays_date, current_time]
    return time

loop_Value = True

while loop_Value:
    db_options = input('VIEW, ADD, REMOVE, MODIFY or EXIT:  ')

    if db_options.lower() == 'view':
        db_call = db_app.db_interaction_class(record,item,new_item)
        db_call.view_document()
        print('\n')
    elif db_options.lower() == 'exit':
        print('Exit Program')
        loop_Value = False
    elif db_options.lower() == 'add':
        try:
            item = str(input('Enter Item to add: '))
            updated_time = setting_time()
            record['item'] = item
            record['date'] = updated_time[0]
            record['time'] = updated_time[1]
            random_num = random.randint(1,1000000000)
            record['_id'] = str(random_num)
            db_call = db_app.db_interaction_class(record, item, new_item)
            db_call.create_document()
        except:
            print('Unable to add item')
    elif db_options.lower() == 'remove':
        item = str(input('What item would you like to remove? '))
        db_call = db_app.db_interaction_class(record, item, new_item)
        db_call.delete_document()

    elif db_options.lower() == 'modify':
        item = str(input('What Item would you like to modify? '))
        new_item = str(input('Enter Replacement Item: '))
        db_call = db_app.db_interaction_class(record, item, new_item)
        db_call.modify_document_item()
    else:
        print('Unknown input\n')


# ---- MODIFY ITEM QUANTITY FUNCTION ------
"""
    def modify_document_quantity(enter_collection, some_record):
    user_quantity = int(input('Change to quantity: '))
    quantity_update ={
        'quantity':user_quantity
    }
    enter_collection.update_one({'_id':some_record['_id']}, {'$set':quantity_update}, upsert=False)
"""
# ---- MODIFY ITEM QUANTITY FUNCTION CALL ------
"""
    elif db_options.lower() == 'modifyquantity':
        change_to = str(input('What item do you want to change? '))
        record = user_records.find_one({'item':change_to})
        print(record)
        modify_document_quantity(user_records,record)
"""
    
