from flask import g
import traceback

def addList(email):
    cursor = g.db.cursor()

    query = """
        INSERT INTO project_ml.mailing_list (email, input_time) VALUES (%s, CURRENT_TIMESTAMP)
    """
    try:
        cursor.execute(query, (email, ))
    except:
        g.db.rollback()
        traceback.print_exc()
        return False

    g.db.commit()
    return True
