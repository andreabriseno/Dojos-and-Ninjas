from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:                                       #data from dojo_and_ninjas schema table 
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name,age, dojo_id) VALUES (%(first_name)s,%(last_name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
#getting the information from db to make a create query 

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM ninjas WHERE id = %(id)s;"
        result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE ninjas SET first_name = %(first_name)s, last_name=%(last_name)s, age= %(age)s WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        return results

    @classmethod
    def destroy(cls,data):
        query = "DELETE FROM ninjas WHERE id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print(results)
        return results

