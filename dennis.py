import pandas as pd
import requests
from json import loads, dumps


def mijnmethode():
    df = pd.read_csv("Pokemon.csv")
    print(df.tail(1))

    # API call from catfact
    paginaresult = requests.get("https://catfact.ninja/fact")
    facts = paginaresult.json()
    return '<h1>Random cat fact: </h1>' + facts['fact']


def get_data(columns, jaar):
    df = pd.read_csv('IT_Salary_Survey_EU_' + str(jaar) + '.csv')
    mydata = df[columns]

    return mydata


def calculate_average(calc_list):
    total = 0
    for x in calc_list:
        total += x
    try:
        average = total / len(calc_list)
    except ZeroDivisionError:
        average = 0

    return round(average, 2)


def job_salary_average(beroep="devops", jaar="2020"):
    df = pd.read_csv('IT_Salary_Survey_EU_' + str(jaar) + '.csv')

    YearlyBrutoSalaryColumn = 'Yearly bruto salary (without bonus and stocks) in EUR'
    extra_small_company = 'up to 10'

    small_company = '11-50'
    small_company_salary = []

    medium_company = '51-100'
    medium_company_salary = []

    large_company = '101-1000'
    large_company_salary = []

    extra_large_company = '1000+'
    extra_large_company_salary = []

    for i, line in df.iterrows():
        if str(line['Position']).lower().strip() == beroep:
            if line['Company size'] == extra_small_company or line['Company size'] == small_company:
                small_company_salary.append(line[YearlyBrutoSalaryColumn])

            elif line['Company size'] == medium_company:
                medium_company_salary.append(line[YearlyBrutoSalaryColumn])

            elif line['Company size'] == large_company:
                large_company_salary.append(line[YearlyBrutoSalaryColumn])

            elif line['Company size'] == extra_large_company:
                extra_large_company_salary.append(line[YearlyBrutoSalaryColumn])

    return {'position': beroep,
            'small': calculate_average(small_company_salary),
            'medium': calculate_average(medium_company_salary),
            'large': calculate_average(large_company_salary),
            'xlarge': calculate_average(extra_large_company_salary)}


# print(company_salary_average())


def all_positions(jaar="2020"):
    df = pd.read_csv('IT_Salary_Survey_EU_' + str(jaar) + '.csv')
    total_jobs = []
    for i, line in df.iterrows():
        total_jobs.append(str(line['Position']).lower().strip())
    return set(total_jobs)

#print(all_positions())


def jobs_salary(jaar="2020"):
    mylist = all_positions(jaar)
    returnlist = []

    for job in mylist:
        returnlist.append(job_salary_average(job, jaar))

    return returnlist

#print(jobs_salary())



def data_to_json(data):
    result = data.to_json(orient="records")
    parsed = loads(result)
    return dumps(parsed, indent=4)


def dict_to_json(data):
    if type(data) is dict:
        array = [{i: data[i] for i in data}]
        return dumps(array, indent=4)
    else:
        return dumps(data, indent=4)


print(dict_to_json(jobs_salary()))
#print(dict_to_json(company_salary_average()))
# print(set(get_data(['Yearly brutto salary (without bonus and stocks) in EUR', 'Company size'], 2020)))
# print(salary_vs_company_size(2020))
# print(data_to_json(company_salary_average()))
