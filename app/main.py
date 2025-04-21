from flask import Flask, render_template, url_for

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


if __name__ == "__main__":
    app.run(debug=True)
    
    