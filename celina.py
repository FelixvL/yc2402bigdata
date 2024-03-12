import pandas
import math
teller = 0

def mijnmethode():
    pokemons = pandas.read_csv("Pokemon.csv")
    global teller
    teller += 1
    print(teller)
    print(pokemons)
    return "dit komt uit het bestand celina"

print (mijnmethode() + str(4+5))

programming_languages = []
salary_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
for i,regel in salary_survey.iterrows():
    new_entry= str(regel["Your main technology / programming language"])
    if new_entry.lower() in programming_languages:
        continue
    programming_languages.append(new_entry.lower())
print(programming_languages)
for x in programming_languages:
    print(x)

def language_salary():
    salary_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
    print(salary_survey)
    python_totaal_salaris = 0
    python_aantal = 0
    js_totaal_salaris = 0
    js_aantal = 0
    java_totaal_salaris = 0
    java_aantal = 0
    sql_totaal_salaris = 0
    sql_aantal = 0
    for i,regel in salary_survey.iterrows():
        print("---",str(regel["Your main technology / programming language"]).lower())
        if "python" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            #for regel["Yearly brutto salary (without bonus and stocks) in EUR"]
            python_aantal += 1
            python_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "javascript" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            js_aantal += 1
            js_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "java" == str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            java_aantal += 1
            java_totaal_salaris+=regel["Yearly brutto salary (without bonus and stocks) in EUR"]
        elif "sql" ==  str(regel["Your main technology / programming language"]).lower():
            print("Ja", regel["Your main technology / programming language"], regel["Yearly brutto salary (without bonus and stocks) in EUR"])
            sql_aantal += 1
            sql_totaal_salaris += regel["Yearly brutto salary (without bonus and stocks) in EUR"]
    print(python_aantal)
    print(python_totaal_salaris)
    print(python_totaal_salaris/python_aantal)
    print(js_aantal)
    print(js_totaal_salaris)
    print(js_totaal_salaris/js_aantal)
    print(java_totaal_salaris)
    print(java_totaal_salaris/js_aantal)
    print(sql_totaal_salaris)
    print(sql_totaal_salaris/js_aantal)
    return "Average salary Python programmer in 2020: " + str(math.ceil(python_totaal_salaris/python_aantal)) + " EUR, average salary JavaScript programmer in 2020: " + str(math.ceil(js_totaal_salaris/js_aantal)) + " EUR, average salary Java programmer in 2020: " + str(math.ceil(java_totaal_salaris/java_aantal)) + " EUR, average salary SQL programmer in 2020: " + str(math.ceil(sql_totaal_salaris/sql_aantal)) + "EUR "


#def language_name():
    language_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
    for i,language in language_survey.iterrows():
        language["Your main technology / programming language"] = language["Your main technology / programming language"].str.lower()
        print(language)

#def language_choice(de_taal):
    salary_survey = pandas.read_csv("IT_Salary_Survey_EU_2020.csv")
    for i,regel in salary_survey.iterrows():
        print("---",str(regel["Your main technology / programming language"]).lower())
        de_tekst_in_kleine_letters = str(regel["Your main technology / programming language"]).lower()
        if de_tekst_in_kleine_letters == de_taal :
            print("Yes, een match.")
        elif de_tekst_in_kleine_letters.find(de_taal) >= 0:
            print("Komt in de titel voor.")
    return "ABC" + de_taal