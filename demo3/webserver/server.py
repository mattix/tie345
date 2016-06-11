from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', latest_image='/static/latest.jpg')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')