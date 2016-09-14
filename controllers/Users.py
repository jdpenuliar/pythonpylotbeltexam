from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Poke')
        self.db = self._app.db
    def index(self):
        if session.get('userid')!= None:
            return redirect ('/pokes')
        else:
            if session.get('errors') != None:
                flash(session['errors']['emailError'], 'Email Error')
                flash(session['errors']['passwordError'], 'Password Error')
                flash(session['errors']['name'], 'Name Error')
                session.pop('errors')
            return self.load_view('/users/index.html')
    def pokesdashboard(self):
        print session['userid']
        info = self.models['User'].pokesdashboard(session['userid'])
        print 'controller'
        print 'controller'
        print 'controller'
        print 'controller'
        print 'controller'
        print 'controller'
        print 'controller'
        print 'controller'
        print info
        return self.load_view('/users/pokes.html', name=info['name'], users = info['users'], mypokers = info['mypokers'], numpokes = info['numpokes'])



    def login(self):
        info = {
            'email':request.form['email'],
            'password':request.form['password']
        }
        login_status = self.models['User'].login(info)
        if login_status['status']==False or login_status == None:
            if login_status['errors']['emailError'] != None:
                flash(login_status['errors']['emailError'],'emailError')
            if login_status['errors']['passwordError'] != None:
                flash(login_status['errors']['passwordError'],'passwordError')
            if login_status['errors']['invalidCredentialError'] != None:
                flash(login_status['errors']['invalidCredentialError'],'invalidCredentialError')
            return redirect('/')
        else:
            print login_status['loggedin_user']
            #I chose only to put the user id so there would be minimal info stored in the session for security, instead of putting all of the info there tho I could just select only the id. Which I now did
            session['userid'] = login_status['loggedin_user']
            return redirect('/pokes')
        return redirect('/')
    def register(self):
        #if i dont put request.forms in dictionary it will return imutablle multiple dictionaries or something like that
        # print request.form
        info = {
            'name':request.form['name'],
            'alias':request.form['alias'],
            'email':request.form['email'],
            'password':request.form['password'],
            'confirm_password':request.form['confirm_password'],
            'dateofbirth':request.form['dateofbirth']
        }

        result = self.models['User'].register(info)
        print result
        if result['status'] == True:
            session['userid'] = result['registered_user_id']
            return redirect('/pokes')
        else:
            session['errors'] = result['errors']
            return redirect('/')
        return redirect('/')

    def logout(self):
        if session.get('userid') != None:
            session.pop('userid')
        return redirect('/')

    def pokeuser(self,id):
        self.models['Poke'].pokeuser(id,session['userid'])
        return redirect('/')