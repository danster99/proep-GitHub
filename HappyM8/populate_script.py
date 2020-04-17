import os, django, random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "happyM8.settings")
django.setup()


from faker import Faker
from api.users.models import User
from api.houses.models import House, Room

fake = Faker()


def create_user(n):
    for _ in range(n):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.ascii_free_email()
        password = fake.password(length=10)
        phone_nr = fake.phone_number()
        user = User.objects.get_or_create(first_name=first_name, last_name=last_name, email=email, password=password, phone_nr=phone_nr)


create_user(50);


def create_house(n):
    for _ in range(n):
        address = fake.street_address()
        max_nr_tenants = random.randint(1, 7);
        rules = "dcsdouvhwoduvhsriugvhrujvhwrufsrrr" \
                "enrjkgvrujvrbugvebrivurbviu" \
                "jvkvbrfvbrdvbdivbfvd" \
                "vkvduvbfivuerivriuvb" \
                "efiohrwiorhfworfhwe" \
                "dwdjnvrdvgbrugv"
        house = House.objects.get_or_create(address=address, max_nr_tenants=max_nr_tenants,rules=rules)


create_house(15);


def create_room(n):
    room_types = ["living room", "bathroom", "kitchen"]
    for _ in range(n):
        room_type = random.choice(room_types)
        is_bookable = fake.boolean(chance_of_getting_true=40)
        rand_int = random.randint(1, 14)
        house_id = House.objects.get(pk=rand_int)
        room = Room.objects.get_or_create(room_type=room_type, is_bookable=is_bookable, house_id=house_id)


create_room(40);

