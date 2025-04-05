from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SECURE=False,
    SESSION_COOKIE_SAMESITE='Lax'
)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about-us")
def aboutus():
    return render_template('about-us.html')

@app.route("/courses")
def courses():
    return render_template('courses.html')

@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/catalog")
def catalog():
    return render_template('catalog.html')

@app.route("/reclamaciones")
def ldr():
    return render_template('ldr.html')

@app.route("/politicas")
def politicas():
    return render_template('politicas.html')

@app.route("/condiciones")
def condiciones():
    return render_template('condiciones.html')

@app.errorhandler(404)
def error_handler(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)