from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user

app = Flask(__name__)

app.config.update(
    SECRET_KEY='WOW SUCH SECRET'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(login):
    return User(login)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['login'] and request.form['pwd']:
            user = User(login)  # Создаем пользователя
            login_user(user)  # Логинем пользователя
            print(url_for('index'))
            return redirect(url_for('index'))
        else:
            return render_template('login.html', error='Неправильный логин или пароль')
    return render_template('login.html')


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@app.route("/")
@login_required
def index():
    return render_template("index.html")


@app.route("/about")
@login_required
def about():
    return render_template("about.html")


@app.route("/posts")
@login_required
def posts():
    return render_template("posts.html")


@app.route("/rate")
@login_required
def rate():
    return render_template("rate.html")


@app.route("/shop")
@login_required
def shop():
    return render_template("shop.html")


@app.route("/wallet")
@login_required
def wallet():
    return render_template("wallet.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
