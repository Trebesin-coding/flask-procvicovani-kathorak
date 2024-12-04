from flask import Flask, render_template, request #importování potřebných knihoven

app = Flask(__name__) #zajistí spuštění aplikace


@app.route("/") #UMĚT "/" !!! dekorátor (zlepšuje/upravuje funkci)
def home():
    return render_template("index.html")

@app.route("/form")
def form():
    py_var = request.args.get("html_name")
    return render_template("form.html", jinja_var=py_var)
    
# name = request.args.get("name")   #Proměnná "name" který přijme jméno uživatele napsané do formuláře
# input_class = request.args.get("class") #Proměnná "input_class" který přijímá třídu uživatele napsanou do formuláře
# message = request.args.get("message") #Proměnná "message" přijme zprávu od uživatele napsanou do formuláře

#     return redirect(url_for("result", name=name, form_class=input_class, message=message)) #
    


# name = request.form.get("name")
# input_class = request.form.get("class")
# message = request.form.get("message")

#     return redirect(url_for("result", name=name)
    





if __name__ == "__main__": #zkontroluje zda je to spuštěné přímo nebo klonované
    app.run(debug=True) #spouštění flaskové aplikace
