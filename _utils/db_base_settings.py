import dotenv
import pymysql
import os
from datetime import datetime

def db_initialize():
    connection = pymysql.connect(
        user = os.environ.get("MYSQL_USER"),
        password = os.environ.get("MYSQL_PASSWORD"),
        host = os.environ.get("MYSQL_HOST"),
        db = os.environ.get("MYSQL_DB_NAME"),
        charset = 'utf8',
    )
    cursor = connection.cursor()

    try:
        # Add ACCOUNT_BOOK_TYPE
        strSql = """
            INSERT INTO ACCOUNT_BOOK_TYPE (id, name)
            VALUES 
            (1, 'Expenditure'),
            (2, 'Income');
        """
        cursor.execute(strSql)
        connection.commit()

        # Add USER
        strSql = f"""
            INSERT INTO USER (id, password, last_login, email, nickname, is_active, is_admin)
            VALUES 
            (1, '{os.environ.get("ADMIN_USER_PASSWORD")}', '{datetime.today()}', '{(os.environ.get('ADMIN_USER_EMAIL'))}', '{os.environ.get('ADMIN_USER_NICKNAME')}',
            True, True);
        """
        cursor.execute(strSql)
        connection.commit()
    
        # Add Category
        strSql = f"""
            INSERT INTO CATEGORY (id, account_book_type_id, writer_id, name, is_custom)
            VALUES 
            (1, 1, 1, '교육비', False),
            (2, 1, 1, '교통비', False),
            (3, 1, 1, '문화비', False),
            (4, 1, 1, '미용비', False),
            (5, 1, 1, '생필품', False),
            (6, 1, 1, '식비', False),
            (7, 1, 1, '의료비', False),
            (8, 1, 1, '의류비', False),
            (9, 1, 1, '주거비', False),
            (10, 1, 1, '차량유지비', False),
            (11, 1, 1, '통신비', False),
            (12, 2, 1, '급여', False),
            (13, 2, 1, '상여금', False),
            (14, 2, 1, '금융수익', False),
            (15, 2, 1, '용돈', False),
            (16, 2, 1, '임대수익', False);
        """
        cursor.execute(strSql)
        connection.commit()
    except:
        connection.rollback()
        print("Insertion Failed")
    connection.close()

if __name__ == "__main__":
    dotenv.read_dotenv(
        dotenv = '.env.local',
    )
    db_initialize()    
