class Loginrepo:
    '''Loginrepo is big repository that main job is to push pull and update the db
    takes in the connection to the db'''
    def __init__(self, connection):
        self._connection = connection

    def create_acc(self, name, passw):
        '''method to create account with specisific name and password'''
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO users (username,password,score,active) VALUES (?,?,?,?)', [name, passw, 0, 0])
        self._connection.commit()

    def update_score(self, score):
        '''Method used to update the score after game'''
        cursor = self._connection.cursor()
        cursor.execute('SELECT score from users where active = 1')
        unit = cursor.fetchone()
        if unit[0] < score:
            cursor.execute('Update users set score = ? where active = 1', [score])
            self._connection.commit()

    def check_activity(self):
        '''Method for checking if there is any activity rightnow
        when people log in the activity for the logging player is set to 1'''
        cursor = self._connection.cursor()
        cursor.execute('SELECT * FROM users WHERE active = 1')
        unit = cursor.fetchone()
        if unit == None:
            return False
        else:
            return True
        
    def print_all(self):
        '''Method to return the best scores in descending order for the highscore
        list'''
        hg_list = []
        cursor = self._connection.cursor()
        cursor.execute('SELECT username,score from users order by score DESC')
        unit = cursor.fetchall()
        for i in unit:
            hg_list.append((i[0], i[1]))
        return hg_list

    def find_user(self, name):
        '''Method used to check if the username allready exist ,
        used in registering process'''
        cursor = self._connection.cursor()
        cursor.execute('SELECT username,password from users where username = ?', [name])
        unit = cursor.fetchone()
        if unit == None:
            return True
        else:
            return False

    def check_login(self, name, passw):
        '''Method checking if the given login credentials match the
        database'''
        cursor = self._connection.cursor()
        cursor.execute('SELECT username from users where username = ? and password = ?', [name, passw])
        unit = cursor.fetchone()
        if unit == None:
            return False
        else:
            return True

    def set_active(self, name):
        '''Method to set player status active'''
        cursor = self._connection.cursor()
        cursor.execute('UPDATE users SET active = 1 where username = ?', [name])
        self._connection.commit()

    def set_nonactive(self):
        '''Method to set allplayers nonactive used to make sure game is not opening
        when it should not be'''
        cursor = self._connection.cursor()
        cursor.execute('UPDATE users SET active = 0 where active = 1')
        self._connection.commit()
