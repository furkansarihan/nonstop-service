from pymongo import MongoClient

class NSMongo:
    def __init__(self, database_string):
        self.client = MongoClient(database_string)
        self.db = None
        self.collection = None
        
    def isAlive(self):
        return self.client.server_info()

    def areParamsSet(self):
        if self.db == None or self.collection == None:
            return False
        return True

    def set_db(self, db_name):
        self.db = self.client[db_name]
    
    def set_collection(self, collection, db_name = None):
        if db_name:
            self.collection = self.client[db_name][collection]
        else:
            self.checkIfDatabaseIsSet()
            self.collection = self.db[collection]
    
    def get(self, query = None):
        self.checkIfCollectionIsSet()
        result = None
        if query:
            result = self.collection.find_one(query)
        else:
            result = self.collection.find_one()
            print(result)
        return result
    
    def insert(self, document, bulk = False):
        self.checkIfCollectionIsSet()
        result = None
        if bulk:
            result = self.collection.insert_many(document)
        else:
            result = self.collection.insert_one(document)            
        return result
    
    def checkIfDatabaseIsSet(self):
        if not self.db:
            raise Exception('Database is not set yet!\nSet a database !')
    
    def checkIfCollectionIsSet(self):
        if not self.collection:
            raise Exception('Collection is not set yet!\nSet a collection before crud operations.')