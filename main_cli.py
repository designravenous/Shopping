import db_app
import datetime
import random

record = {
    "user_name": "Peter",
    "item": "Stadium",
    "quantity": 1,
    "date": "2018-01-01",
    "time": "10:43",
    "_id": "1212",
    "added_to_basket":False
}

item = "godis"
new_item = "GODIS"

def setting_time():
    date = datetime.datetime.now()
    m = date.month
    d = date.day
    h = date.hour
    min_ = date.minute
    sec = date.second

    if m <= 9:
        month = "0" + str(m)
    else:
        month = str(m)
    if d <= 9:
        day = "0" + str(d)
    else:
        day = str(d)
    if h <= 9:
        hour = "0" + str(h)
    else:
        hour = str(h)
    if min_ <= 9:
        minute = "0" + str(min_)
    else:
        minute = str(min_)
    if sec <= 9:
        second = "0" + str(sec)
    else:
        second = str(sec)
    todays_date = str(date.year) + "-" + month + "-" + day
    current_time = hour + ":" + minute + ":" + second
    time = [todays_date, current_time]
    return time

loop_Value = True

while loop_Value:
    db_options = input('VIEW, ADD, REMOVE, MODIFY, INBASKET or EXIT:  ')

    if db_options.lower() == 'view':
        db_call = db_app.db_interaction_class(record,item,new_item)
        response = db_call.view_document()
        for document in response:
            print(document['user_name'],document['item'],document['added_to_basket'],document['quantity'],document['_id'], document['date'], document['time'])
    elif db_options.lower() == 'exit':
        print('Exit Program')
        loop_Value = False
    elif db_options.lower() == 'add':
        try:
            item = str(input('Enter Item to add: ')).upper()
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
        item = str(input('What item would you like to remove? ')).upper()
        db_call = db_app.db_interaction_class(record, item, new_item)
        db_call.delete_document()

    elif db_options.lower() == 'modify':
        item = str(input('What Item would you like to modify? ')).upper()
        new_item = str(input('Enter Replacement Item: ')).upper()
        db_call = db_app.db_interaction_class(record, item, new_item)
        db_call.modify_document_item()
        #KOLLA VARFÖR DENNA INTE FUNGERAR!!!! INBASKET
    elif db_options.lower() == 'inbasket':
        item = str(input('Change basket status, for item: ')).upper()
        db_call = db_app.db_interaction_class(record,item,new_item)
        db_call.change_inbasket_status()
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
    
