from flask import Flask,request,render_template


app = Flask(__name__)

@app.route('/')
def home():
    return ('Hello,Welcome to flask!')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello, {name}!'
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1><p>Sorry, the page you are looking for does not exist.</p>", 404


if __name__ == '__main__':
    app.run(debug=True)