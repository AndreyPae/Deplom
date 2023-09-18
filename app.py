from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'secret_key' # Заменить на секретный ключ

# пример
users = {
'user1': 'password1',
'user2': 'password2'
}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
username = request.form['username']
password = request.form['password']

if username in users and users[username] == password:
    session['username'] = username

    return redirect('/secret')

else:

    return render_template('login.html', message='Неверные имя пользователя или пароль')

    return render_template('login.html')

@app.route('/secret')
def secret():
    if 'username' in session:
        return f'Привет, {session["username"]}! Добро пожаловать на секретную страницу!'
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
