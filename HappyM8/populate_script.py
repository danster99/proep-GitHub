import os, django, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "happyM8.settings")
django.setup()


from faker import Faker
from api.users.models import User
from api.houses.models import House, Room
from api.utilities.models import Utility
from datetime import timedelta
from api.chores.models import Chore
from api.bookings.models import Booking

fake = Faker()


# def create_user(n):
#     for _ in range(n):
#         first_name = fake.first_name()
#         last_name = fake.last_name()
#         email = fake.ascii_free_email()
#         password = fake.password(length=10)
#         phone_nr = fake.phone_number()
#         is_admin = fake.boolean(chance_of_getting_true=20)
#         user = User.objects.get_or_create(first_name=first_name, last_name=last_name,
#                                           email=email, password=password,
#                                           phone_nr=phone_nr, is_admin=is_admin)
#
#
# create_user(50)
#
#
# def create_house():
#     for user_var in User.objects.filter(is_admin=True):
#         address = fake.street_address()
#         max_nr_tenants = random.randint(1, 7)
#         rules = "dcsdouvhwoduvhsriugvhrujvhwrufsrrr" \
#                 "enrjkgvrujvrbugvebrivurbviu" \
#                 "jvkvbrfvbrdvbdivbfvd" \
#                 "vkvduvbfivuerivriuvb" \
#                 "efiohrwiorhfworfhwe" \
#                 "dwdjnvrdvgbrugv"
#         owner = user_var
#         house = House.objects.get_or_create(address=address, max_nr_tenants=max_nr_tenants,
#                                             rules=rules, owner=owner)
#
#
# create_house()
#
#
# def update_house():
#     for user in User.objects.all():
#         for house in House.objects.prefetch_related('tenant').all():
#             print('\033[34m{}\033[0m'.format('before if'))
#             if house.max_nr_tenants > house.tenant.count():
#                 print('\033[34m{}\033[0m'.format('here'))
#                 user.house_tenant = house
#                 user.save()
#
#
# update_house()


# def create_room():
#     room_types = ["living room", "bathroom", "kitchen"]
#     for house in House.objects.all():
#         for _ in range(3):
#             is_bookable = fake.boolean(chance_of_getting_true=40)
#             houses = House.objects.all()
#             house= random.choice(houses)
#             room = Room.objects.get_or_create(room_type=room_types[_],
#                                           is_bookable=is_bookable, house=house)
#
#
# create_room()
#
#
# def create_utility():
#
#     utility_types = ['dryer', 'washing machine', 'vacuum cleaner', 'dish washer']
#     for house_var in House.objects.all():
#         for _ in range(4):
#             utility = Utility.objects.get_or_create(house=house_var, name=utility_types[_])
#
#
# create_utility()


def create_booking(n):
    for _ in range(n):
        users = User.objects.filter(is_admin=False)
        user = random.choice(users)
        rooms = Room.objects.filter(house_id=user.house_tenant_id)
        room = random.choice(rooms)
        utilities = Utility.objects.filter(house=user.house_tenant)
        utility = random.choice(utilities)
        description = fake.sentence()
        begin_time = fake.future_datetime()
        end_time = begin_time + timedelta(hours=2)
        booking = Booking.objects.get_or_create(user=user, room=room,
                                                utility=utility, description=description,
                                                begin_time=begin_time, end_time=end_time)


create_booking(30)


def create_chore():
    for house_var in House.objects.all():
        for _ in range(3):
            chore_names = ['take out trash', 'clean kitchen', 'clean bathroom']
            house = house_var
            description = fake.sentence()
            begin_time = fake.future_datetime()
            end_time = begin_time + timedelta(hours=2)
            chore = Chore.objects.get_or_create(name=chore_names[_], house=house,
                                                description=description, begin_time=begin_time,
                                                end_time=end_time)


create_chore()

