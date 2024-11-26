from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """
    def __init__(self, username='aacuser', password='SNHU1234'):
        # Initializing the MongoClient
        self.client = MongoClient(f'mongodb://{username}:{password}@nv-desktop-services.apporto.com:33945/AAC?authSource=AAC&directConnection=true')
        self.database = self.client['AAC']
    #Create method
    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            
    #Read method
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
        else:
            data = self.database.animals.find({}, {"_id": False})
        return data

    #Update method
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set": updateData })
        else:
            return "{}"
        # Return the dataset else let the error flow up
        return result.raw_result

    #Delete method
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        # Return the dataset else let the error flow up
        return result