from flask import Flask , render_template
app=Flask(__name__)
@app.route('/')
def home():
    return render_template("index.html")




@app.route('/login')
def login():
    return "login"



@app.route('/signup')
def signup():
    return "signup"




if __name__ =="__main__":
    app.run(debug=True)