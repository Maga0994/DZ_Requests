# Задание 1
import requests
from pprint import pprint

def all_hero_list():
    url = 'https://akabab.github.io/superhero-api/api/all.json'
    response = requests.get(url)
    hero_name = {}
    pprint(response.json())                # выводим все данные
    for hero in response.json():             # проходим циклом
        if hero['name'] in ['Hulk', 'Captain America', 'Thanos']:
            hero['powerstats'] = hero['powerstats']['intelligence']
            hero_name.setdefault(hero['name'], hero['powerstats'])               # заносим данные в пустой словать
    sorted_tuple = sorted(hero_name.items(), key=lambda x: x[1], reverse=True)          # переводим в кортеж и сортируем
    intellect_hero = {k: v for k, v in sorted_tuple}                   # переводим обратно в словарь
    print()
    print(intellect_hero)                # выводим значения сортированного словаря
    print(f'Самый умный супергерой, а точнее суперзлодей "Thanos" со значением интелекта {intellect_hero["Thanos"]}.')

if __name__ == '__main__':
    all_hero_list()
