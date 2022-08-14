
from account.models import UserProfile, City, Country
import logging
import random
logger = logging.getLogger(__name__)
from backend.settings import FIXTURES_PATH
import os
import glob
import json
from django.core.files import File  # you need this somewhere
import urllib
from usermedia.models import UserMedia
import random

def user_gen(city_source,city_target):
    try:
        citys = City.objects.get(alias=city_source)
        cityt = City.objects.get(alias=city_target)
        logger.info(f'loading {citys}')
        gender = get_random_gender()
        logger.info(f'gender {gender}')
        name = get_random_name(gender)
        logger.info(f'name {name}')
        image = get_random_image_path()
        logger.info(f'image {image}')
        scity = get_random_uk_city()
        logger.info(f'from {citys}')
        prof = get_random_prof()
        logger.info(f'prof {prof["name_ru"]}')
        password = '123456t'
        profile = UserProfile()
        profile.username = name['name_en']+str(random.randint(1,9999))
        profile.publicname_ru = name['name_ru']
        profile.publicname_en = name['name_en']
        profile.publicname_uk = name['name_uk']
        profile.prof_ru = prof['name_ru']
        profile.prof_en = prof['name_en']
        profile.prof_uk = prof['name_uk']
        profile.set_password(password)
        profile.target_city = cityt
        profile.source_city = citys           
        profile.gender = gender
        profile.is_staff = True
        profile.is_superuser = True
        profile.is_superuser = True
        profile.is_fake = True
        profile.save()
        save_image(profile,image)
    except Exception as e:
        print(e)
        return 'City not found!'


def get_random_gender():
    gender = ['male','female']
    idx = random.randint(0,1)
    return gender[idx]

def get_random_name(gender):
    path = os.path.join(FIXTURES_PATH,'fake', 'names.json')
    with open(path, 'r') as f:
        names = json.loads(f.read())
    if gender == 'male':
        rnd = random.randint(0,len(names['man'])-1)
        return names['man'][rnd]
    else:
        rnd = random.randint(0,len(names['woman'])-1)
        path = os.path.join(FIXTURES_PATH, 'wnames.txt')
        return names['man'][rnd]


def get_random_image_path():
    path = os.path.join(FIXTURES_PATH, 'avatar/*')
    imgs = glob.glob(path)
    idx = random.randint(0,len(imgs)-1)
    return imgs[idx]


def get_random_uk_city():
    country = Country.objects.get(alias='ukraine')
    return City.objects.filter(country=country).order_by('?')[0]

def get_random_prof():
    path = os.path.join(FIXTURES_PATH,'fake', 'prof.json')
    with open(path, 'r') as f:
        profs = json.loads(f.read())
    idx = random.randint(0,len(profs)-1)
    return profs[idx]

def save_image(user,img_path):
    i = UserMedia()
    i.user = user
    i.is_approved = True
    i.is_main = True
    i.save()
    i.image.save(user.username,File(open(img_path, 'rb')))