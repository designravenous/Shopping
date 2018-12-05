import pymongo 
from pymongo import MongoClient

class db_interaction_class:
    def __init__(self, python_dictionary, db_item, replacement_item):
        Mongodb_URI = "mongodb://xxx:xxx@ds151292.mlab.com:51292/database"
        client = MongoClient(Mongodb_URI, connectTimeoutMS=30000)
        db = client.get_database('database')
        user_records = db.user_baskets
        self.user_records = user_records
        self.python_dictionary = python_dictionary
        self.db_item = db_item
        self.replacement_item = replacement_item
        
    def view_document(self):
        cursor = self.user_records.find({})
        dic_list =[]
        for document in cursor:
            dic_list.append({'user_name':document['user_name'],'item':document['item'],'quantity':document['quantity'],'date':document['date'],'time':document['time'],'_id':document['_id'], 'added_to_basket':document['added_to_basket']})
        return dic_list

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

    def change_inbasket_status(self):
        finding_item = self.user_records.find_one({'item':self.db_item})
        myquery = {'added_to_basket':finding_item['added_to_basket']}
        if finding_item['added_to_basket'] == False:
            new_query = {'$set':{'added_to_basket':True}}
        else:
            new_query = {'$set':{'added_to_basket':False}}
        self.user_records.update_one(myquery,new_query)
