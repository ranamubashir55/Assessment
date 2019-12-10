
import json, requests
from flask import Flask
import paramiko
import sqlite3
from flask_cors import CORS
from flask import request

app = Flask(__name__)

cors = CORS(app)


def insert_data(data):
    conn = sqlite3.connect('assessment.db')
    conn.execute('''CREATE TABLE if not exists file_usage 
            (ID INTEGER PRIMARY KEY    AUTOINCREMENT,
            file_system           CHAR(50),
            size            CHAR(50),
            used        CHAR(50),
            avail         CHAR(50),
            use            CHAR(50),
            mounted_on     CHAR(50) );''')
    print("table created successfully")
    for x in data:
        conn.execute("INSERT INTO file_usage (file_system, size, used, avail, use, mounted_on) VALUES ( '"+x['file_system']+"', '"+x['size']+"', '"+x['used']+"', '"+x['avail']+"', '"+x['use']+"', '"+x['mounted']+"')")
        conn.commit()
    print("data inserted successfully...")
    conn.close()


@app.route('/get_file_usage', methods=['POST','GET'])
def create_ssh():
    data =request.get_json()
    host = data['ip']
    username= data['username']
    password = data['password']
    print(data)
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    result =[] 
    try:
        print("creating connection")
        ssh.connect(host,22,username,password)
        print("connected")
        stdin, stdout, stderr = ssh.exec_command('df -h')
        for line in stdout:
            print(line.strip('\n'))
            values = line.strip('\n').split(" ")
            values = [x for x in values if x]
            if "filesystem" in values[0].lower():
                continue
            else:
                    result.append({"file_system":values[0],"size":values[1],"used":values[2],"avail":values[3],"use":values[4],"mounted":values[5]})
        #insert data in db 
        insert_data(result)
    finally:
       print ("closing connection")
       ssh.close()
       print ("closed")
    return json.dumps(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, threaded=True, debug=True)
