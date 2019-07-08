import sqlalchemy as db

def teste1():
    """
    Teste acessando diretamente ao banco
    """
    engine = db.create_engine('sqlite:///test.sqlite') 
    connection = engine.connect()
    metadata = db.MetaData()
    Emp = db.Table('emp', metadata,
          db.Column('Id',db.Integer()),
          db.Column('name', db.String(255),nullable=False),
          db.Column('salary', db.Float(), default=100.0),
          db.Column('active', db.Boolean(), default=True)
          )
    #metadata.create_all(engine)
    #Inserting record one by one
    #query = db.insert(Emp).values(Id=1, name='naveen', salary=60000.00, active=True)
    #ResultProxy = connection.execute(query)

    #Equivalent to 'SELECT * FROM census'
    query = db.select([Emp])
    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    for elem in ResultSet:
        print("{name} {salary}".format(name=elem.name, salary=elem.salary))


def teste2():
    """
    Teste declarativa
    """
    from database import db_session
    from models import User
    #u = User('admin', 'admin@localhost')
    #db_session.add(u)
    #db_session.commit()
    for x in User.query.all():
        print("Nome: {} [ {} ]".format(x.name, x.email))
    user1 = User.query.filter(User.name == 'admin').first()
    print("Nome: {:30}: [ {} ]".format(user1.name, user1.email))

    # Atualiza
    #user1.email = "admin@teste" 
    #db_session.flush()
    #db_session.commit()

    #apagando
    #db_session.delete(user1)
    #db_session.commit()


    #query.filter(User.name.like('%ed%'))
    #query.filter(User.name.in_(['ed', 'wendy', 'jack']))
    #from sqlalchemy import and_
    #query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))
    #from sqlalchemy import or_
    #query.filter(or_(User.name == 'ed', User.name == 'wendy'))
    #query.filter(User.name.like('%ed')).count()



def teste2a():
    """
    Iniciando o banco
    """
    from database import init_db
    init_db()


if __name__ == "__main__":
        teste2()
