from flask import Flask, render_template, request, jsonify
from responses import responses
import sqlite3

chatbot = Flask(__name__)

# default reply if dictionary loop fails
normal_ans = "I don't have these information try contacting with our staff."

# making the db table
def build_db_stuff():
    conn = sqlite3.connect("chat_history.db")
    c = conn.cursor()
    
    # sql query to make table
    q = '''
        CREATE TABLE IF NOT EXISTS chat_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT,
            user_phone TEXT,
            message TEXT,
            reply TEXT,
            time DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    '''
    c.execute(q)
    conn.commit()
    conn.close()

# call it on startup
build_db_stuff()

def find_match(txt):
    txt = txt.lower().strip()
    
    for k, v in responses.items():
        if k in txt:
            return v
    return normal_ans

@chatbot.route("/")
def homepage():
    return render_template("chatbot.html")

@chatbot.route("/chat", methods=['POST'])
def process_chat():
    in_data = request.get_json()
    
    user_msg = in_data.get('message', '')
    n = in_data.get('name', '')
    p = in_data.get('phone', '')

    # check empty values for db
    if n == "":
        n = "Anonymous"
    if p == "":
        p = "No phone"

    # get the bot output
    bot_reply = find_match(user_msg)

    # database insert part
    try:
        con = sqlite3.connect("chat_history.db")
        cursor = con.cursor()
        cursor.execute(
            "INSERT INTO chat_records (user_name, user_phone, message, reply) VALUES (?, ?, ?, ?)", 
            (n, p, user_msg, bot_reply)
        )
        con.commit()
        con.close()
    except:
        pass 

    return jsonify({'reply': bot_reply})

# This the route from where we can i see the users name and number
@chatbot.route("/see_chats")
def check_db():
    # Used to set an password so no one get user's information other than admin
    passkey = request.args.get("key")
    if passkey != "admin123":
        return "<h1>Access Denied!</h1>" 
        
    con = sqlite3.connect('chat_history.db')
    c = con.cursor()
    c.execute('select * from chat_records order by id desc')
    records = c.fetchall()
    con.close()
    # Use "http://127.0.0.1:5000/see_chats?key=passkey" to see these page where the user's information is there.
    page = "<h1>All Chats</h1><br><table border='1'>"
    page = page + "<tr> <th>Num</th> <th>User</th> <th>Phone</th> <th>Msg</th> <th>Bot</th> <th>Time</th> </tr>"
    
    for item in records:
        page = page + "<tr>"
        page = page + "<td>" + str(item[0]) + "</td>"
        page = page + "<td>" + str(item[1]) + "</td>"
        page = page + "<td>" + str(item[2]) + "</td>"
        page = page + "<td>" + str(item[3]) + "</td>"
        page = page + "<td>" + str(item[4]) + "</td>"
        page = page + "<td>" + str(item[5]) + "</td>"
        page = page + "</tr>"
        
    page = page + "</table>"
    return page

# start the local server
if __name__ == '__main__':
    print("running the chatbot server now...")
    chatbot.run(host='127.0.0.1', port=5000, debug=True)