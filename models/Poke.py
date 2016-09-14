""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
class Poke(Model):
    def __init__(self):
        super(Poke, self).__init__()
    
    def pokeuser(self,id,poker_id):
        poke_user_query = 'INSERT INTO pokes(user_id, pokers_id,created_at, updated_at) VALUES (:user_id, :pokers_id, NOW(), NOW())'
        poke_user_data = {
            'user_id':id,
            'pokers_id':poker_id
        }
        
        self.db.query_db(poke_user_query, poke_user_data)
        return True