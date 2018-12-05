import pymongo 
from pymongo import MongoClient

class db_interaction_class:
    def __init__(self, python_dictionary, db_item, replacement_item):
        Mongodb_URI = "mongodb://test:test123@ds151292.mlab.com:51292/mydatabase"
        client = MongoClient(Mongodb_URI, connectTimeoutMS=30000)
        db = client.get_database('mydatabase')
        user_records = db.user_baskets
        self.user_records = user_records
        self.python_dictionary = python_dictionary
        self.db_item = db_item
        self.replacement_item = replacement_item
        
    def view_document(self):
        cursor = self.user_records.find({})
        for document in cursor:
            print(document['user_name'],document['item'],document['added_to_basket'],document['quantity'],document['_id'], document['date'], document['time'])

    def create_document(self):
        self.user_records.insert_one(self.python_dictionary)
    
    def delete_document(self):
        try:
            self.user_records.delete_one({'item':self.db_item})
        except:
            print('unable to remove item')
            
    def modify_document_item(self):
        finding_item = self.user_records.find_one({'item':self.db_item})
        myquery = {'item':finding_item['item']}
        new_query = {'$set':{'item':self.replacement_item}}
        self.user_records.update_one(myquery, new_query)
