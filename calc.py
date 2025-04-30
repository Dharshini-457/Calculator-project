from flask import  Flask,render_template
app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/ncalc')
def Ncalc():
    return render_template('nor_calc.html')
@app.route('/calc')
def calc():
    return render_template("file.html")

if __name__ == '__main__':
    app.run(debug=True)