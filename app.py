from Flask import Flask , render_template
app=Flask(__name__)
@app.route('/')
def home():
    return "welcome"
if __name__ =="main":
    app.run(debug=True)