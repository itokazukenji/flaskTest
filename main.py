from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello():
    html = render_template('index.html')
    return html

@app.route('/test')
def test():
    html = render_template('test.html')
    return html


if __name__ == '__main__':
    app.run()


