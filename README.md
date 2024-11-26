Animal Shelter Database CRUD Module

About the Project 
This Python CRUD (Create, Read, Update, Delete) module provides an  interface for managing animal shelter data in MongoDB. Designed specifically for Grazioso Salvare's animal shelter database system, it enables efficient data management through a maintainable and secure API.

Motivation
Animal shelters need reliable, efficient systems to manage data and track animals in their care. This module aims to:
Provide an intuitive and standardized Python interface for database operations.
Enables secure authentication for database access
Ensure data consistency and reliability through proper error handling.
Facilitates efficient animal record management
Supports complex queries for data analysis

Technical Implementation
MongoDB Driver
This project uses the PyMongo driver (pymongo) for the following reasons:
Native Python integration with MongoDB
Comprehensive support for all CRUD operations
Robust authentication and security features
Excellent documentation and community support
Built-in connection pooling and error handling

Installation
mongodb://{username}:{password}@nv-desktop-services.apporto.com:33945      

CRUD Operations Functionality
Create: 
Validates input data before insertion
Returns boolean success indicator
Includes error handling for empty data

Code Example
#Create method
```python
    def create(self, data):
        if data is not None:
            insertSuccess = self.database.animals.insert_one(data)
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
```
            

Tests
#Create test data
```python
animal_data = {
    "rec_num": 22,
    "age_upon_outcome": "3 years",
    "animal_id": "A123457",
    "animal_type": "Dog",
    "breed": "Golden Retriever",
    "color": "Gold",
    "date_of_birth": "2020-05-01",
    "datetime": "2023-05-01 12:00:00",
    "monthyear": "2023-05",
    "name": "Max",
    "outcome_subtype": "",
    "outcome_type": "Adoption",
    "sex_upon_outcome": "Neutered Male",
    "location_lat": 30.2672,
    "location_long": -97.7431,
    "age_upon_outcome_in_weeks": 156
}
```

#Test create method
```python
print("\nTesting Create Functionality:")
create_result = shelter.create(animal_data)
print("Create result:", create_result)
```


Read: 
Supports flexible querying with MongoDB's find() operation
Returns cursor for efficient data iteration
Handles both specific queries and full collection retrieval

                  Code Example
```python
                   #Read method
    def read(self, searchData):
        if searchData:
            data = self.database.animals.find(searchData, {"_id": False})
        else:
            data = self.database.animals.find({}, {"_id": False})
        return data

            #Test read
#Test read method with queries
print("\nTesting Read Functionality:")

#Find all dogs
print("\nQuery 1: Find all dogs")
query1 = {"animal_type": "Dog"}
read_result = shelter.read(query1)
for doc in read_result:
    print(doc)

#Find specific animal by ID
print("\nQuery 2: Find specific animal")
query2 = {"animal_id": "A691584"}
read_result = shelter.read(query2)
for doc in read_result:
    print(doc)

#Find animals by breed type
print("\nQuery 3: Find animals by breed")
query3 = {"breed": "Labrador Retriever Mix"}
read_result = shelter.read(query3)
for doc in read_result:
    print(doc)
```

Update:
Supports bulk updates with update_many()
Returns detailed operation results
Includes validation of search criteria

       Code Example
#Update method
```python
    def update(self, searchData, updateData):
        if searchData is not None:
            result = self.database.animals.update_many(searchData, { "$set": updateData })
        else:
            return "{}"
        # Return the dataset else let the error flow up
        return result.raw_result
```

#Test Update method
```python
print("\nTesting Update Functionality:")
#Update the animal we created earlier
update_query = {"animal_id": "A123457"}
update_data = {"color": "Light Gold"}
update_result = shelter.update(update_query, update_data)
print("Update result:", update_result)
```

Delete:
Supports bulk deletions
Includes validation checks
Returns deletion operation results
          
       Code example
#Delete method
```python
    def delete(self, deleteData):
        if deleteData is not None:
            result = self.database.animals.delete_many(deleteData)
        else:
            return "{}"
        # Return the dataset else let the error flow up
        return result
```

      Test Delete

#Test delete method
```python
print("\nTesting Delete Functionality:")
#Delete the animal we created
delete_query = {"animal_id": "A123457"}
delete_result = shelter.delete(delete_query)
print("Delete result:", delete_result)
```

Screenshots
 
 



 
 


 
. Contact
Contact: Michael Spaniolo
