import json
import pprint


def get_candidates():
    """
    Получает из файла список кандидатов
    return
    """
    with open("data/candidates.json", "r") as fp:
        candidats = json.load(fp)
    return candidats


def get_candidate_by_id(can_id):
    """
    возвращает кандидата по его id з файла
    """
    candidates = get_candidates()

    for can in candidates:
        if can_id == can["id"]:
            return can


def get_settings():
    """
       Получает словарь с настройками
       return
       """
    with open("data/setting.json", "r") as fp:
        candidats = json.load(fp)
    return candidats


def get_candidate_by_name(name):
    candidates = get_candidates()
    settings = get_settings()

    candidats_found = []

    for can in candidates:

        if _make_search(name, can["name"], settings["case-sensitive"]):
            candidats_found.append(can)

    return candidats_found


def candidates_by_skill(skill_name):
    candidates = get_candidates()
    settings = get_settings()

    candidats_found = []

    for can in candidates:

        if _make_search(skill_name, can["skills"], settings["case-sensitive"]):
            candidats_found.append(can)

    limit = settings["limit"]

    candidats_found = candidats_found[:limit]

    return candidats_found


def _make_search(search_for, user_name, case_sensitive):

    if case_sensitive:
        if search_for in user_name:
            return True
    else:
        if search_for.lower() in user_name.lower():
            return True
    return False
