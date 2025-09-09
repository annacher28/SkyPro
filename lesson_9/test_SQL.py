from sqlalchemy import create_engine, select, text, MetaData, Table
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import sessionmaker

db_connection_string = "postgresql://postgres:Aa123456@localhost:5432/postgres"
db = create_engine(db_connection_string)
Session = sessionmaker(bind=db)
session = Session()

def test_insert():
    
    connection = db.connect()
    transaction = connection.begin()
    sql_insert = text("""
        INSERT INTO users(user_id, user_email, subject_id) 
        VALUES (:user_id, :user_email, :subject_id)
    """)
    
    connection.execute(sql_insert, {
        "user_id": "666", 
        "user_email": "Skypro@Skypro.ru",
        "subject_id": 2
    })

    transaction.commit()
    connection.close()


def test_update():
    """Обновление существующей записи в таблице users"""
    connection = db.connect()
    transaction = connection.begin()
    sql_update = text("""
        UPDATE users 
        SET user_email = :new_email, subject_id = :new_subject_id
        WHERE user_id = :user_id
    """)
    
    connection.execute(sql_update, {
        "new_email": "updated@Skypro.ru",
        "new_subject_id": 3,
        "user_id": "666"
    })

    transaction.commit()
    connection.close()

def test_delete():
    
    connection = db.connect()
    transaction = connection.begin()
    sql_delete = text("""
        DELETE FROM users 
        WHERE user_id = :user_id
    """)
    connection.execute(sql_delete, {
        "user_id": "666"
    })
    transaction.commit()
    connection.close()