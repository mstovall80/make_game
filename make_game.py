from flask import Flask, render_template               
app=Flask(__name__)


app = Flask(__name__)  
@app.route('/')                             
def hello_world():
    return render_template("index.html")

@app.route('/hawaii')
def Hawaii():
    return render_template("hawaii.html")

@app.route('/germany')
def germany():
    return render_template("germany.html")

@app.route('/beer')
def you_win():
    return render_template("beer.html")

@app.route('/wine')
def wine():
    return render_template("wine.html")

@app.route('/snorkling')
def snorkling():
    return render_template("snorkling.html")

@app.route('/out_to_eat')
def eat():
    return render_template("out_to_eat.html")

@app.route('/steak')
def steak():
    return render_template("steak.html")

@app.route('/salad')
def salad():
    return render_template("salad.html")

@app.route('/corral')
def corral():
    return render_template("corral.html")

@app.route('/reaf')
def reaf():
    return render_template("reaf.html")










if __name__=="__main__":                      
    app.run(debug=True)   