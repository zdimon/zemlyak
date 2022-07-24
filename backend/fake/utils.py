from fake.models import Prof, Name
from account.models import UserProfile, City
import random
import uuid



def get_random_name():
    return Name.objects.order_by('?').first()

def get_random_prof():
    return Prof.objects.order_by('?').first()

def get_random_gender():
    g = ['m','w']
    rnd = random.randint(0,1)
    return g[random.randrange]

def make_user(source_city, target_city):
    myuuid = str(uuid.uuid4())
    print(myuuid)
    name = get_random_name()
    prof = get_random_prof()
    print(name.name_ru)
    print(prof.name_ru)
    user = UserProfile()
    user.username = myuuid
    user.set_password(myuuid)
    user.publicname_ru = name.name_ru
    user.publicname_uk = name.name_uk
    user.publicname_en = name.name_en
    user.source_city = source_city
    user.target_city = target_city
    user.prof_ru = prof.name_ru
    user.prof_uk = prof.name_uk
    user.prof_en = prof.name_en
    user.save()
