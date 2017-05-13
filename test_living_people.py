#!python

import unittest
import datetime
import living_people

Person = living_people.Person
FORMAT = '%m-%d-%Y'
TODAY = datetime.datetime.today().date()

TEST_PEOPLE = [
    Person(last_name='paxton', first_name='bill', birth=datetime.datetime(1981, 1, 1, 0, 0), death=datetime.datetime(1982, 2, 2, 0, 0)),
    Person(last_name='goldburg', first_name='jeff', birth=datetime.datetime(1981, 1, 2, 0, 0), death=datetime.datetime(2000, 1, 4, 0, 0)),
    Person(last_name='cruise', first_name='tom', birth=datetime.datetime(1983, 1, 3, 0, 0), death=datetime.datetime(1999, 1, 4, 0, 0)),
    Person(last_name='bale', first_name='christian', birth=datetime.datetime(1991, 1, 5, 0, 0), death=datetime.datetime(1991, 1, 6, 0, 0))
    ]

TEST_PEOPLE_2 = [
    Person(last_name='paxton', first_name='bill', birth=datetime.datetime(1981, 1, 1, 0, 0), death=datetime.datetime(1982, 2, 2, 0, 0)),
    Person(last_name='goldburg', first_name='jeff', birth=datetime.datetime(1981, 1, 2, 0, 0), death=datetime.datetime(2018, 1, 4, 0, 0)),
    Person(last_name='cruise', first_name='tom', birth=datetime.datetime(1981, 1, 3, 0, 0), death=datetime.datetime(2010, 1, 4, 0, 0)),
    Person(last_name='bale', first_name='christian', birth=datetime.datetime(1981, 1, 5, 0, 0), death=datetime.datetime(1991, 1, 6, 0, 0))
    ]


class TestLivingPeople(unittest.TestCase):

    def setUp(self):
        self.people = living_people.LivingPeople()

    def test_get_people(self):
        self.assertCountEqual(TEST_PEOPLE, self.people.get_people('file.csv'))

    def test_get_lives_per_year(self):
        people_list = self.people.get_people('file.csv')
        self.people.get_lives_per_year(people_list)
        result = self.people.get_all_max_years()
        self.assertCountEqual([1991], result)

    def test_get_lives_per_year_if_multiple_years_have_max_value(self):
        people_list = TEST_PEOPLE_2
        self.people.get_lives_per_year(people_list)
        result = self.people.get_all_max_years()
        self.assertCountEqual([1981, 1982], result)
