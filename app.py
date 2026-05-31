from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Note: Database-la 'attempts' column illana, idhu error kaatum. 
# So simple-ah irukka, namma old logic-eye use pannuvom.

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/verify', methods=['POST'])
def verify():
    u1, u2, u3, u4 = request.form.get('a1'), request.form.get('a2'), request.form.get('a3'), request.form.get('a4')
    
    conn = sqlite3.connect('atm_fraud.db')
    cursor = conn.cursor()
    cursor.execute("SELECT ans1, ans2, ans3, ans4 FROM user_details WHERE id = 1")
    db_data = cursor.fetchone()
    
    if db_data and (u1, u2, u3, u4) == db_data:
        msg = "SUCCESS: Access Granted!"
    else:
        msg = "ALERT: Access Denied. Security Blocked!"
    
    conn.close()
    return render_template('index.html', alert_msg=msg)

if __name__ == '__main__':
    app.run(debug=True)