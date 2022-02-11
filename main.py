from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
import sqlite3

conn = sqlite3.connect('BDD.db')


class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

users = []
users.append(User(id=1, username='RebeuDeter', password='DonutSucréAuSucre'))
users.append(User(id=2, username='Miguel', password='secret'))
users.append(User(id=3, username='Maxence', password='Réveille_toi'))


app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        """verifier si l'utilisateur n'est pas deja utilise par un client"""

        req_user_existant = "SELECT * FROM Donnees WHERE Identifiant = '%s' "
        cursor.execute(req_user_existant % Identifiant)
        resultat_req_user_existant = cursor.fetchall()
        print(resultat_req_user_existant)

        '''Si on a déjà un utilisateur avec ce numéro, on dit qu'il est déjà utilisé'''

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        return redirect(url_for('login'))

        return render_template('login.html')



        #"""Sinon on enregistre les informations de l'identifiant dans la BD"""

    else:
        req_login = "INSERT INTO Donnees (User, Identifiant, Mot de passe)VALUES(%s,%s,%s)"
        cursor.execute (req_login, (User, Identifiant, password))
        connection.commit()
    
@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')

