import unittest
from src.data.database_connection import get_database_connection
from src.data.intialize_database import initialize_database1
from src.repot.yatzyrepo import Loginrepo

class Testrepo(unittest.TestCase):
    def setUp(self):
        initialize_database1()
        self.connection = get_database_connection()
        self.test_repo = Loginrepo(self.connection)
        self.name = 'ripa'
        self.password = 'sika'
        self.score = 69
        self.active = 1
        self.turha = 0

    def test_create_acc(self):
        self.test_repo.create_acc(self.name, self.password)
        score_list = self.test_repo.print_all()
        self.assertEqual(len(score_list), 1)
        self.assertEqual(score_list[0][0],'ripa')

    def test_update_score_and_activity(self):
        self.test_repo.create_acc(self.name, self.password)

        bool_value = self.test_repo.check_activity()
        self.assertEqual(bool_value,False)

        score_list = self.test_repo.print_all()
        self.assertEqual(score_list[0][1],0)
        

        self.test_repo.set_active(self.name)
        self.test_repo.update_score(500)
        score_list = self.test_repo.print_all()
        self.assertEqual(score_list[0][1],500)

        bool_value = self.test_repo.check_activity()
        self.assertEqual(bool_value,True)

        self.test_repo.set_nonactive()
        bool_value = self.test_repo.check_activity()
        self.assertEqual(bool_value,False)

    def test_register(self):
        self.test_repo.create_acc(self.name, self.password)
        bool_value = self.test_repo.find_user('matti')
        bool_value2 = self.test_repo.find_user(self.name)
        self.assertEqual(bool_value,True)
        self.assertEqual(bool_value2,False)

    def test_login(self):
        self.test_repo.create_acc(self.name, self.password)
        bool_value = self.test_repo.check_login(self.name, self.password)
        bool_value2 = self.test_repo.check_login(self.name, 'vaarasalis')
        self.assertEqual(bool_value,True)
        self.assertEqual(bool_value2,False)

