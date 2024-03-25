from flask import Flask 
import felix
import asef
import celina
import dennis

from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tweedetest")
def tweedetest():
    return "<p>Dit is mijn tweede test</p>"

@app.route("/derdetest/<pokemonnaam>")
def derdetest(pokemonnaam):
    return felix.mijnmethode(pokemonnaam)

@app.route("/testcelina")
def testcelina():
    return celina.mijnmethode()

@app.route("/testasef")
def testasef():
    return asef.mijnmethode()

@app.route("/testdennis")
def testdennis():
    return dennis.mijnmethode()

@app.route("/salaryCompanySize/<jaar>")
def salary_vs_company_size(jaar):
    return dennis.dict_to_json(dennis.jobs_salary(jaar=jaar))

@app.route("/getjobs/<jaar>")
def get_jobs(jaar):
    return dennis.dict_to_json(dennis.count_jobs(dennis.all_positions(jaar)))

@app.route("/<jaar>/<job>")
def job_salary_average(jaar, job):
    return dennis.dict_to_json(dennis.job_salary_average(job, jaar))


@app.route("/taalprijs")
def salary_vs_language():
    return celina.language_salary()

@app.route("/taalkeuze/<de_taal>")
def choice_language(de_taal):
    return celina.language_choice(de_taal)