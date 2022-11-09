from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja

class Dojo:                                         #data is given from the data base 
    def __init__(self, data):
        self.id = data ['id']
        self.name = data ['name']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']
        self.ninjas=[]                              #empty list to connect to nin dict

    @classmethod 
    def get_all(cls):
        query = "SELECT * FROM dojos;"                                      #Getting at the data from dojo table
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query) #Database info
        dojos=[]
        for places in results:              #places is the data in which is going to get transferred 
            dojos.append(cls(places))
        return dojos

    @classmethod
    def create(cls,data):                                                       #getting access to db
        query = "INSERT INTO dojos (name) VALUES (%(name)s)"                    #adding new data in database under dojos tabe name
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data) #db info
        return result

    @classmethod
    def get_one_all_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;" #Joining data table together chose left due to tables not having the same names
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        dojo = cls(results[0])
        for people in results:
            nin ={
                'id': people['ninjas.id'],
                'first_name': people['first_name'],
                'last_name': people['last_name'],
                'age': people['age'],
                'created_at': people['ninjas.created_at'],
                'updated_at': people['ninjas.updated_at'],
            }
            dojo.ninjas.append(Ninja(nin))
        return dojo #putting all the data information to store data

    @classmethod
    def get_one(cls,data):
        query ="SELECT * FROM dojos LEFT JOIN ninjas on dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(results[0])
