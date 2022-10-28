from flask import Flask
from flask import url_for, render_template, request, redirect, session, jsonify
from datetime import datetime
import logging 

from random import sample
import mysql.connector

server = Flask(__name__)
logger = logging.getLogger()


cnx = None 
cursor = None 


def run_sql_query(*queries):
    cnx = mysql.connector.connect(user='root', password='Trace.Social-2021',
                              host='database',
                              database='trace_db')
    cursor = cnx.cursor()
    for query in queries: 
        cursor.execute(query) 
    result = cursor.fetchall() 
    cnx.commit() 
    cursor.close() 
    cnx.close()
    logger.warning(f"Database query of size {len(queries)} performed.")
    return result 

@server.route('/')
def index():
    uid = request.args.get("rec_id", default=-1, type=int)
    try:
        if 0 <= int(uid) < 20:
            logger.warning(f"Valid uid {uid}")
            # 数据库对应成员数量+1 
            query_count_update = f"UPDATE trace_member_data SET count = count + 1 WHERE uid={uid}"

            # datetime object containing current date and time
            now = datetime.now()
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S") # dd/mm/YY H:M:S

            logger.warning(f"Remote ip={request.remote_addr}, rec={uid}, time={dt_string}")
            query_ip_update = f"INSERT INTO visit_data (ip, rec, time) VALUES ('{request.remote_addr}', '{str(uid)}', '{dt_string}'); "
            queries = [query_ip_update, query_count_update] 
            run_sql_query(*queries) 
        return render_template("index.html")
    except Exception:
        return render_template("index.html")

@server.route('/about')
def about():
    return render_template("about.html")

@server.route('/submit', methods=['POST'])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        wxid = request.form.get("wxid")
        logger.warning(f"User form received: {name} : {wxid}") 
        
        query = f"insert into user_profile_data (name, wxid) values ('{name}', '{wxid}')"
        run_sql_query(query) 

        return render_template("thank.html")

@server.route('/show_data', methods=['GET'])
def show_users():
    pswd = request.args.get("p", default="", type=str)
    if pswd == "sdawwwjsczxc7spios":
        query_user = "select * from user_profile_data"
        query_visit = "select * from visit_data"
        u_list = run_sql_query(query_user) 
        v_list = run_sql_query(query_visit)
        return {
            "msg" : "Returning current data",
            "users" : list(u_list), 
            "visits" : list(v_list) 
        }
    else: 
        return {
            "msg" : "Wrong Access Pswd, request rejected."
        }

@server.route('/show_employees', methods=['GET'])
def show_employees(): 
    query = "select * from trace_member_data" 
    result = run_sql_query(query) 
    context = {
        "employee_points" : list(result) 
    }
    return render_template("demonstration.html", **context)
