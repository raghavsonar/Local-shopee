from flask import Flask, render_template
#https://local-shopee.raghavs2812.repl.co/static  img path
app = Flask(__name__)

@app.route("/")
def home_page():
  return render_template('index.html')

@app.route("/buy_now")
def buy_now_page():
  return render_template('buy_now.html')

@app.route("/company")
def company():
  return render_template('company.html')

@app.route("/login")
def company():
  return render_template('login.html')

@app.route("/signup")
def signup():
  return render_template('sign_up.html')


if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=1)