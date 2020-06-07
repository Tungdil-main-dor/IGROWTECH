"""To-do list where you can chronologically add your tasks, modify them and mark if they have been completed.
  A cleanup feature enables you to delete completed tasks which are more than a week old - unless
  you have flagged them as 'protected'."""
from collections import OrderedDict
from datetime import date, datetime, timedelta
import os
from peewee import *

db = SqliteDatabase('garden.db')

class Plant(Model):
    """Model for creating plant items.
"""
    name = CharField(max_length=255)
    description = CharField(max_length=255)
    water_span_autumn = IntegerField()
    water_span_winter = IntegerField()
    water_span_spring = IntegerField()
    water_span_summer = IntegerField()
    water_info = TextField()
    last_watered = DateTimeField(default=datetime.now)
    fertilizer_info = TextField()


    class Meta:
        database = db


def clear():
    """Clear the display"""
    os.system('cls' if os.name == 'nt' else 'clear')


def initialize():
    """Connect to database, build tables if they don't exist"""
    db.connect()
    db.create_tables([Plant], safe=True)


def view_entries(index, entries, single_entry):
    """"View to-do list"""
    clear()
    season = get_season(date.today())
    # determines which entry is selected for modification
    index = index % len(entries)
    if single_entry:  # to see only 1 entry
        entries = [entries[index]]
        index = 0
    else:
        print(f'\nMY GARDEN - {date.today().strftime("%d-%m-%Y")} - {season.title()}')
        print('=' * 60)
    prev_timestamp = None

    for ind, entry in enumerate(entries):
        #timestamp = entry.timestamp.strftime('%d %B %Y')

        print('\n')
        #print('=' * len(timestamp))
        #prev_timestamp = timestamp

        if ind == index:  # placing the selection tick
            tick = '> '
        else:
            tick = '  '

        print('{}{}'.format(tick, entry.name), end='')
        now = datetime.now()
        elapsed = now - entry.last_watered
        if season == 'autumn':
            if elapsed < (timedelta(days = entry.water_span_autumn)):
                print(f'\n    Water OK - next time in {((timedelta(days = entry.water_span_autumn))-elapsed).days} days', end='')
            else:
                print(f'\n    Needs Water!! - should have been done {(elapsed-(timedelta(days = entry.water_span_autumn))).days} days ago', end='')
        elif season == 'winter':
            if elapsed < (timedelta(days = entry.water_span_winter)):
                print(f'\n    Water OK - next time in {((timedelta(days = entry.water_span_winter))-elapsed).days} days', end='')
            else:
                print(f'\n    Needs Water!! - should have been done {(elapsed-(timedelta(days = entry.water_span_winter))).days} days ago', end='')
        elif season == 'winter':
            if elapsed < (timedelta(days = entry.water_span_spring)):
                print(f'\n    Water OK - next time in {((timedelta(days = entry.water_span_spring))-elapsed).days} days', end='')
            else:
                print(f'\n    Needs Water!! - should have been done {(elapsed-(timedelta(days = entry.water_span_spring))).days} days ago', end='')
        elif season == 'summer':
            if elapsed < (timedelta(days = entry.water_span_summer)):
                print(f'\n    Water OK - next time in {((timedelta(days = entry.water_span_summer))-elapsed).days} days', end='')
            else:
                print(f'\n    Needs Water!! - should have been done {(elapsed-(timedelta(days = entry.water_span_summer))).days} days ago', end='')
        print('')

    return entries  # so that we can modify the given entry if needed


def add_entry(index, entries):
    """Add a new plant"""

    nami = input('\n>>>>> New Plant Creation <<<<<\nWhat is it\'s name: ')
    descriptioni = input('Can you shortly describe the plant? ')
    water_span_autumn_i = int(input('\nHow often does it need to be watered in autumn (days): '))
    water_span_winter_i = int(input('\nHow often does it need to be watered in winter (days): '))
    water_span_spring_i = int(input('\nHow often does it need to be watered in spring (days): '))
    water_span_summer_i = int(input('\nHow often does it need to be watered in summer (days): '))
    water_infoi = input('Can you detail the water needs of this plant with a sentence? ')
    fertilizer_infoi = input('Can you detail the fertilizer needs of this plant with a sentence? ')

    Plant.create(name=nami, water_span_autumn=water_span_autumn_i, water_span_winter=water_span_winter_i, water_span_spring=water_span_spring_i, water_span_summer=water_span_summer_i, water_info=water_infoi,
                 description=descriptioni, fertilizer_info=fertilizer_infoi)


def modify_entry(index, entries):
    """Modify selected plant"""
    entry = view_entries(index, entries, True)[0]

    for key, value in sub_menu.items():
        print('{}) {}'.format(key, sub_menu[key].__doc__))
    print('q) Back to Main')
    next_action = input('Action: ')

    if next_action.lower().strip() in sub_menu:
        sub_menu[next_action](entry)
    else:
        return

def water_plant(index, entries):
    """Water the selected plant"""
    entry = view_entries(index, entries, True)[0]
    print(f"\n\n{entry.name}")
    if (input('Ok to water now [yN]? ').lower().strip() == 'y'):
        entry.last_watered = datetime.now()
        entry.save()
    print('\nBack to Main')
    next_action = input('Press Enter')


def display_plant_info(index, entries):
    """Display info for selected plant"""
    entry = view_entries(index, entries, True)[0]
    print(f"\n{entry.description}")
    print(f"\n\nWater needs:\n\tevery {entry.water_span_autumn} days in autumn, \n\tevery {entry.water_span_winter} days in winter, \n\tevery {entry.water_span_spring} days in spring, \n\tevery {entry.water_span_summer} days in summer.")
    if entry.water_info:
        print(f'\n\nMore details about it\'s water needs:\n\t{entry.water_info}')
    print(f'\n\nMore details about it\'s fetilizer needs:\n\t{entry.fertilizer_info}\n')
    print('\n\n\nBack to Main')
    next_action = input('Press Enter')


def modify_plant_name(entry):
    """Modify Plant Name"""
    new_name = input('> ')
    entry.name = new_name
    entry.save()


def modify_plant_water_spans(entry):
    """Modify Plant Water Spans"""
    print('\n')
    new_water_span_autumn = input(f'The current water span for {entry.name} in autumn is: {entry.water_span_autumn}, what do you want it to be ? ')
    new_water_span_winter = input(f'The current water span for {entry.name} in  winter is: {entry.water_span_winter}, what do you want it to be ? ')
    new_water_span_spring = input(f'The current water span for {entry.name} in  spring is: {entry.water_span_spring}, what do you want it to be ? ')
    new_water_span_summer = input(f'The current water span for {entry.name} in  summer is: {entry.water_span_summer}, what do you want it to be ? ')
    entry.water_span_autumn = new_water_span_autumn
    entry.water_span_winter = new_water_span_winter
    entry.water_span_spring = new_water_span_spring
    entry.water_span_summer = new_water_span_summer
    entry.save()


def modify_plant_description(entry):
    """Modify Plant Descriptions"""
    print('\n')
    new_description = input(f'The current the current description for {entry.name} is: {entry.description}, what do you want it to be ? ')
    new_water_info = input(f'The current the water needs info for {entry.name} is: {entry.water_info}, what do you want it to be ? ')
    new_fertilizer_info = input(f'The current the fertilizer needs info for {entry.name} is: {entry.fertilizer_info}, what do you want it to be ? ')

    entry.description = new_description
    entry.water_info = new_water_info
    entry.fertilizer_info = new_fertilizer_info
    entry.save()


def delete_entry(entry):
    """Erase entry"""
    print('\n')
    if (input('Are you sure [yN]? ').lower().strip() == 'y'):
        entry.delete_instance()


def menu_loop():
    choice = None
    index = 0  # shows which entry is selected
    entries = Plant.select().order_by(Plant.name.asc())
    while choice != 'q':
        if len(entries) != 0:
            view_entries(index, entries, False)

            print('\n' + '=' * 60 + '\n')
            print('Previous/Next: p/n \n')
        for key, value in main_menu.items():
            print('{}) {}'.format(key, value.__doc__))
        print('q) Quit')

        choice = input('\nAction: ')
        if choice in main_menu:
            try:
                main_menu[choice](index, entries)
            except ZeroDivisionError:
                continue
            # update entries after operations
            entries = Plant.select().order_by(Plant.name.asc())

        elif choice == 'n':
            index += 1
        elif choice == 'p':
            index -= 1


main_menu = OrderedDict([
    ('a', add_entry),
    ('w', water_plant),
    ('d', display_plant_info),
    ('m', modify_entry)
])

sub_menu = OrderedDict([
    ('mn', modify_plant_name),
    ('md', modify_plant_description),
    ('mws', modify_plant_water_spans),
    ('delete', delete_entry)
])

#handling the season aspect
Y = 2000 # dummy leap year to allow input X-02-29 (leap day)
seasons = [('winter', (date(Y,  1,  1),  date(Y,  3, 20))),
           ('spring', (date(Y,  3, 21),  date(Y,  6, 20))),
           ('summer', (date(Y,  6, 21),  date(Y,  9, 22))),
           ('autumn', (date(Y,  9, 23),  date(Y, 12, 20))),
           ('winter', (date(Y, 12, 21),  date(Y, 12, 31)))]

def get_season(now):
    if isinstance(now, datetime):
        now = now.date()
    now = now.replace(year=Y)
    return next(season for season, (start, end) in seasons
                if start <= now <= end)

if __name__ == '__main__':
    initialize()
    menu_loop()
    db.close()
water_plant()
