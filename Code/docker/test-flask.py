from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)
#app.secret_key = 'secretkey'

@app.route('/')
def index():
    print('Hello')
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    user = request.form['user']
    session['user']=user
    return render_template('login.html', user=user)

@app.route('/slides')
def slides():
    return render_template('slides.html')

@app.route('/logout')
def logout():
    del session['user']
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True, port=8000)