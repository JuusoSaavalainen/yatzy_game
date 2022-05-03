class Loginrepo:
    def __init__(self, connection):
        self._connection = connection

    def create_acc(self, name):
        cursor = self._connection.cursor()
        cursor.execute('INSERT INTO users (username) VALUES 0', [name])
        self._connection.commit()
        return 'User was created'

    def update_score(self, score, name):
        cursor = self._connection.cursor()
        cursor.execute('Update users set score = ? where username = ?', [score, name])
        self._connection.commit()

    def get_highscores(self):
        high_score = []
        print('asdjfnboaisefnoi')
        cursor = self._connection.cursor()
        helping_hand = cursor.execute('SELECT * FROM users')
        rows = helping_hand.fetchall()
        for row in rows:
            high_score.append(row)
        self._connection.commit()
        return high_score
