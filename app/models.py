from flask_mysqldb import MySQL

class College:
    def __init__(self, *args, **kwargs):
        code = kwargs["code"]
        name = kwargs["name"]

    def create(self, *args, **kwargs):
        pass 

    def delete(self, *args, **kwargs):
        pass 

class Program:
    def __init__(self, *args, **kwargs):
        code = kwargs["code"]
        name = kwargs["name"]
        description = kwargs["description"]

    def create(self, *args, **kwargs):
        pass 

    def delete(self, *args, **kwargs):
        pass 

class Student:
    def __init__(self, *args, **kwargs):
        id_number = kwargs["id_number"]
        
        last_name = kwargs["last_name"]
        first_name = kwargs["first_name"] 
        middle_name = kwargs["middle_name"] or None
        
        program = kwargs["program"] or None
        
        gender = kwargs["gender"]
        year_level = kwargs["year_level"] or None

    def create(self, *args, **kwargs):
        pass 

    def delete(self, *args, **kwargs):
        pass 
