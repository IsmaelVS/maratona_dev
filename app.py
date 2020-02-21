from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Doner(db.Model):
    """Classe para criação da tabela de doadores."""

    __tablename__ = 'doner'

    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    blood = db.Column(db.String(4), nullable=False)

    def __init__(self, name, email, blood):
        db.create_all()
        self.name = name
        self.email = email
        self.blood = blood

    def __repr__(self):
        return f'Doner(name={name}, email={email}, blood={blood})'


@app.route('/', methods=['POST', 'GET'])
def home():
    """Rota para exibir página e cadastrar novo doador."""

    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        blood = request.form.get('blood')

        doner = Doner(name=name, email=email, blood=blood)

        db.session.add(doner)
        db.session.commit()

    doners = db.session.query(Doner).all()

    return render_template('index.html', doners=doners)


if __name__ == '__main__':
    app.run()
