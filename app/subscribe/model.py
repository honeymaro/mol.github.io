from flask import g
import traceback
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

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

    msg = MIMEMultipart()

    msg['From'] = 'contact@langchain.io'
    msg['Subject'] = "Thank you for subscribing LangChain! (former, Mother of Language)"
    msg['To'] = email
    with open('app/subscribe/templates/letter.txt', 'r') as f:
        text = f.read()
    content = MIMEText(text, 'plain', _charset='utf-8')
    msg.attach(content)

    a = smtplib.SMTP('smtp.gmail.com:587')
    a.ehlo()  
    a.starttls()
    a.login('contact@langchain.io', 'ciceron3388!')
    a.sendmail(msg['From'], msg['To'], msg.as_string())

    return True
