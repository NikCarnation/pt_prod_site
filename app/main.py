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

@app.route("/user/<username>")
def user(username):
    return render_template("user.html", user=username) #для уязвимости типа idor. Сделаем тестовую страницу админа/разраба и на нее засунем что нибудь


if __name__ == "__main__":
    app.run(debug=True)
    
    