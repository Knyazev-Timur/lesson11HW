import json


def load_candidates():
    with open('candidates.json', 'r', encoding='UTF-8') as load_files:
        return json.load(load_files)


def get_by_pk(pk):
    data_candidates = load_candidates()
    for items in data_candidates:
        if pk == items.get('pk'):
            data_pk = f"<img src='({items.get('picture')})'>\n" \
                      f"<pre>\nИмя кандидата - {items.get('name')}\n" \
                      f"Позиция кандидата - {items.get('position')}\n" \
                      f"Навыки: {items.get('skills')}\n</pre>\n"
            return data_pk
    return f'Данные не найдены'


def get_by_skill(skill_name):
    data_candidates = load_candidates()
    data_skill = ''
    for items in data_candidates:
        if skill_name.lower() in items.get('skills').lower():
            data_skill += f"\n<pre>\nИмя кандидата - {items.get('name')}\n" \
                         f"Позиция кандидата - {items.get('position')}\n" \
                         f"Навыки: {items.get('skills')}\n</pre>\n"

    if data_skill == '':
        return f'Данные не найдены'
    else:
        return data_skill


def get_all():
    data_candidates = load_candidates()
    data_all = ''
    for items in data_candidates:
        data_all += f'\n<pre>\nИмя кандидата - {items.get("name")}\n' \
                    f'Позиция кандидата - {items.get("position")}\n' \
                    f'Навыки: {items.get("skills")}\n</pre>\n'

    return data_all
