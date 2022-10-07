import functions
from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    return functions.get_all()


@app.route('/candidates/<pk>')
def profile(pk):
    return functions.get_by_pk(int(pk))


@app.route("/skills/<skill_name>")
def page_feed(skill_name):
    return functions.get_by_skill(skill_name)


app.run()
