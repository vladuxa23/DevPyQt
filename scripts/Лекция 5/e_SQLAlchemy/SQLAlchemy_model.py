import json
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from mimesis import Person

engine = create_engine("sqlite:///example.db", echo=True, future=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Model = declarative_base(name='Model')
Model.query = db_session.query_property()


def init_db():
    Model.metadata.create_all(bind=engine)


def create_user():
    person = Person('ru')

    return {'name': person.first_name(),
            'surename': person.surname(),
            'login': '@' + person.username(mask='l_l'),
            'password': person.password(),
            'email': person.email(),
            'phone': person.telephone(),
            'register_time': datetime.now()}


def addUser():
    user = User(**create_user())
    db_session.add(user)
    db_session.commit()
    return user.to_dict()


def getAllUsers():
    return [x.to_dict() for x in User.query.all()]


Model = declarative_base(name='Model')
Model.query = db_session.query_property()


class User(Model):
    __tablename__ = 'users'
    id = Column('user_id', Integer, primary_key=True)
    name = Column('name', String(200))
    surname = Column('surename', String(200))
    login = Column('login', String(200))
    password = Column('password', String(200))
    email = Column('email', String(200))
    phone = Column('phone', String(200))
    register_time = Column('register_time', DateTime())

    def __init__(self, **params):
        self.name = params.get("name")
        self.surname = params.get("surename")
        self.login = params.get("login")
        self.password = params.get("password")
        self.email = params.get("email")
        self.phone = params.get("phone")
        self.register_time = params.get("register_time")

    def to_dict(self):
        return dict(name=self.name, surname=self.surname, login=self.login,
                    password=self.password, email=self.email, phone=self.phone,
                    register_time=self.register_time)

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4, sort_keys=True, default=str)


init_db()
