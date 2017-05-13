import datetime
import csv
from collections import namedtuple, defaultdict
import operator

TODAY = datetime.datetime.today().date()
FORMAT = '%m-%d-%Y'
Person = namedtuple('Person', ['last_name', 'first_name', 'birth', 'death'])


class LivingPeople():

    def __init__(self):
        self.years_alive = defaultdict(int)

    def get_people(self, file_name):
        people = self.read_file(file_name=file_name)
        return [
            Person(
                person[0],
                person[1],
                datetime.datetime.strptime(person[2], FORMAT),
                datetime.datetime.strptime(person[3], FORMAT),
                ) for person in people if person
            ]

    def read_file(self, file_name):
        if file_name:
            with open(file_name, 'r') as f:
                reader = csv.reader(f)
                return list(reader)

    def count_living(self, people_list):
        for person in people_list:
            for year in range(person.birth.year, person.death.year + 1):
                self.years_alive[year] += 1
        return self.get_all_max_years()

    def get_all_max_years(self):
        return [k for k, v in self.years_alive.items() if v == max(self.years_alive.values())]
