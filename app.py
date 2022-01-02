from flask import Flask, request, render_template

from utils import get_candidates, get_settings, get_candidate_by_id

app = Flask(__name__)


@app.route("/")
def page_index():
    settings = get_settings()
    online = settings.get("online")
    if online:
        return "Приложение работает"
    return "Приложение не работает"


@app.route("/list")
def page_list_of_candidates():
    cans = get_candidates()
    return render_template("list.html", can=cans)


@app.route("/candidate/<int:can_id>")
def page_singl_candidat(can_id):
    can = get_candidate_by_id(can_id)

    return render_template("candidate.html", can=can)


@app.route("/search")
def page_search_by_name():
    name = request.args['name']

    cans = get_candidate_by_name(name)
    cans_count = len(cans)
    return render_template("search.html", cans=cans)

app.run()


@app.route("/skill/<skill_name>")
def page_search_by_scill():
    name = request.args['scillname']

    cans = candidates_by_skill(skill_name)
    cans_count = len(cans)
    return render_template("skill.html", skill_name=skkill_name, cans=cans)

app.run()
