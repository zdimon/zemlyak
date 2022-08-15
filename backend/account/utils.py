from account.models import CityGroup

def add_city_group(source, target):
    try:
        cg = CityGroup.objects.get(target=target, source=source)
    except Exception as e:
        print(e)
        CityGroup.objects.create(target=target, source=source)
