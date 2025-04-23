from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about_company():
    return render_template("about.html")

@app.route("/our_services")
def company_service():
    return render_template("company_services.html")


@app.route("/partner")
def company_partner():
    return render_template("partner.html")


dict_of_employees = {0:"tony",  1: "anna", 2: "bob", 3: "nik", 4: "dima" }



@app.route("/employees")
def user():
    id = request.args.get("id")
    id = int(id)
    employee_name = dict_of_employees.get(id, "anna")  
    return render_template(f"employees/{dict_of_employees[id]}.html", id = id)

if __name__ == "__main__":
    app.run(debug=True)
    
    