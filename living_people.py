from argparse import ArgumentParser
import csv
from collections import namedtuple, defaultdict
import datetime

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

    def valid_date_check(self, persons):
        for person in persons:
            if person.birth.year > person.death.year:
                return 'Invalid birth date: {} {} {}'.format(
                    person.first_name, person.last_name, person.birth.date().strftime(FORMAT))
            if person.birth.year < 1900 or person.birth.year > 2000:
                return 'Birthdate is out of range: {} {} {}'.format(
                    person.first_name, person.last_name, person.birth.date().strftime(FORMAT))
            if person.death.year < 1900 or person.death.year > 2000:
                return 'Death date is out of range: {} {} {}'.format(
                    person.first_name, person.last_name, person.death.date().strftime(FORMAT))

    def read_file(self, file_name):
        if file_name:
            with open(file_name, 'r') as f:
                reader = csv.reader(f)
                return list(reader)

    def get_lives_per_year(self, people_list):
        for person in people_list:
            for year in range(person.birth.year, person.death.year + 1):
                self.years_alive[year] += 1
        return self.years_alive

    def get_all_max_years(self):
        return [k for k, v in self.years_alive.items() if v == max(self.years_alive.values())]


def chart_data(years_alive):
    for year, count in sorted(years_alive.items()):
        print('{}|'.format(year) + count * '#')

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--file_name", help="Name of file to read", required=True)
    parser.add_argument("--chart", type=bool, help="Boolean True or False", required=False)
    args = parser.parse_args()
    g = LivingPeople()
    list_of_people = g.get_people(args.file_name)
    date_check = g.valid_date_check(list_of_people)
    if date_check:
        print("Error")
        print(date_check)
    else:
        g.get_lives_per_year(list_of_people)
        print('Year(s) with the most people alive:', g.get_all_max_years())
        if args.chart:
            chart_data(g.years_alive)
