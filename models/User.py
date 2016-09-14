""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
class User(Model):
    def __init__(self):
        super(User, self).__init__()
    def register(self, info):
        emailRegrex = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

        PW_REGEX = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

        dictionary_errors = {
            'emailError':'',
            'name':'',
            'passwordError':''
        }
        errorCount=0
        
        if len(info['email']) < 1:
            dictionary_errors['emailError']+='Email cannot be blank\n'
            errorCount+=1
        if not emailRegrex.match(info['email']):
            dictionary_errors['emailError']+='Email format must be valid!\n'
            errorCount+=1
        if len(info['name']) < 1:
            dictionary_errors['name']+='First name cannot be blank\n'
            errorCount+=1
        if len(info['password']) < 1:
            dictionary_errors['passwordError']+='Password cannot be blank\n'
            errorCount+=1
        if len(info['confirm_password']) < 1:
            dictionary_errors['passwordError']+='Confirm cannot be blank\n'
            errorCount+=1
        if str(info['confirm_password']) != str(info['password']):
            dictionary_errors['passwordError']+='Password does not match\n'
            errorCount+=1
        if str(info['name']).isalpha() == False:
            dictionary_errors['name']+='First name must only contain letters\n'
            errorCount+=1
        if len(info['password']) <= 8:
            dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
            errorCount+=1
        if PW_REGEX.match(info['password']) == None:
            dictionary_errors['passwordError']+='Password must have atleast 1 upper case, 1 lower case and 1 number!\n'
            errorCount+=1
        
        query = "SELECT * FROM users where email = :email"
        data = {
            'email': info['email']
        }
        emails = self.db.query_db(query,data)

        if len(emails)>0:
            dictionary_errors['emailError']+='Email already taken\n'
            errorCount+=1


        print 'errorrrrrrrrrr'
        print errorCount
        print dictionary_errors
        if errorCount>0:
            return {"status": False, "errors": dictionary_errors}
        else:
            password = info['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)


            register_query = 'INSERT INTO users(name, alias, email, password, dateofbirth, created_at, updated_at) VALUES (:name, :alias, :email, :pw_hash,:dateofbirth, NOW(), NOW())'
            register_data = {
                'name': info['name'],
                'alias': info['alias'],
                'email': info['email'],
                'pw_hash': hashed_pw,
                'dateofbirth': info['dateofbirth']
            }
            registered_user_id = self.db.query_db(register_query, register_data)

            
            
            return { "status": True, 'registered_user_id': registered_user_id}
    def login(self,info):
        # We write our validations in model functions.
        # They will look similar to those we wrote in Flask
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        
        dictionary_errors = {
            'emailError':'',
            'passwordError':'',
            'invalidCredentialError':''
        }
        errorCount = 0
        if len(info['email']) < 1:
            dictionary_errors['emailError']+='Email cannot be blank\n'
            errorCount+=1
        if not EMAIL_REGEX.match(info['email']):
            dictionary_errors['emailError']+='Email format must be valid!\n'
            errorCount+=1
        if len(info['password']) < 1:
            dictionary_errors['passwordError']+='Password cannot be blank\n'
            errorCount+=1
        if len(info['password']) <= 8:
            dictionary_errors['passwordError']+='Password must be more than 8 characters long\n'
            errorCount+=1
        
        if errorCount>0:
            return {"status": False, "errors": dictionary_errors}
        else:
            password = info['password']
            get_login_user_query = "SELECT * FROM users where email = :email"
            get_login_user_data = {
                'email':info['email']
            }
            
            user = self.db.query_db(get_login_user_query, get_login_user_data)

            if len(user) >0:
                if self.bcrypt.check_password_hash(user[0]['password'], password):
                    print user, '<--- this is the logged in user'
                    return { "status": True, 'loggedin_user':user[0]['id']}
                else:
                    dictionary_errors['invalidCredentialError']+='Invalid credentials!\n'
                    return {"status": False, "errors": dictionary_errors}
            else:
                dictionary_errors['invalidCredentialError']+='Invalid credentials!\n'
                return {"status": False, "errors": dictionary_errors}
    def pokeuser(self,id,poker_id):
        poke_user_query = 'INSERT INTO pokes(user_id, pokers_id,created_at, updated_at) VALUES (:user_id, :pokers_id, NOW(), NOW())'
        poke_user_data = {
            'user_id':id,
            'pokers_id':poker_id
        }
        
        self.db.query_db(poke_user_query, poke_user_data)
        return True
    def pokesdashboard(self,loggedin_user_id):
        print loggedin_user_id, 'hahaha'
        print loggedin_user_id, 'hahaha'
        print loggedin_user_id, 'hahaha'
        print loggedin_user_id, 'hahaha'
        print loggedin_user_id, 'hahaha'
        get_login_user_query = "SELECT name FROM users where id = :id"
        get_login_user_data = {
            'id':loggedin_user_id
        }

        name = self.db.query_db(get_login_user_query, get_login_user_data)
        print name
        
        #select users.name, count(pokes.pokers_id) as pokecount from users join pokes on users.id = pokes.user_id where pokes.user_id = 1
        # get_poke_user_query = "select users.name, count(pokes.pokers_id) as pokecount from users join pokes on users.id = pokes.user_id where pokes.user_id = :id"
        # get_poke_user_data = {
        #     'id':loggedin_user_id
        # }
        
        # name = self.db.query_db(get_login_user_query, get_login_user_data)


        #select users.name, count(pokes.pokers_id) as pokedme from pokes join users on users.id = pokes.pokers_id where pokes.user_id = 1 group by pokes.pokers_id
        
        #select count(user_id) as numpokes from pokes where user_id = 1 group by user_id

        get_num_pokes_query = "SELECT count(user_id) as numpokes from pokes where user_id = :id group by user_id"
        get_num_pokes_data = {
            'id':loggedin_user_id
        }
        
        numpokes = self.db.query_db(get_num_pokes_query, get_num_pokes_data)
        
        get_poker_query = "SELECT users.name, count(pokes.pokers_id) as pokedme from pokes join users on users.id = pokes.pokers_id where pokes.user_id = :id group by pokes.pokers_id order by pokedme desc"
        get_poker_data = {
            'id':loggedin_user_id
        }
        mypokers = self.db.query_db(get_poker_query, get_poker_data)
        
        print len(mypokers)
        print 'hooooooo'
        print 'hooooooo'
        print 'hooooooo'
        print 'hooooooo'
        print 'hooooooo'
        print 'hooooooo'
        print 'hooooooo'

        get_users_query = "select users.id, users.name, users.alias, users.email, count(pokes.user_id) as history from users left join pokes on users.id = pokes.user_id where users.id != :id group by pokes.user_id order by users.name"
        # get_users_query = "select users.name, users.alias, users.email, pokes.user_id, pokes.pokers_id from pokes join users on users.id = pokes.pokers_id"
        get_users_data = {
            'id':loggedin_user_id
        }
        
        users = self.db.query_db(get_users_query, get_users_data)
        
        return {'name':name[0]['name'], 'numpokes':len(mypokers), 'users':users, 'mypokers':mypokers}