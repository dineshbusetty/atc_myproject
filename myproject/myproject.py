# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 12:22:53 2020

@author: NI6303
"""
import requests
from flask import Flask, render_template, request, flash, redirect, url_for, jsonify, Response, send_from_directory,session, app
import os
from werkzeug.utils import secure_filename
import subprocess
import re
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
import pandas as pd
from os import listdir
from os.path import isfile, join
import sqlite3
import glob
import datetime
import zipfile
import json
from random import randint
from datetime import date ,datetime, timedelta
import pathlib
from pathlib import Path
from logging import FileHandler, WARNING
from collections import OrderedDict
#from flask.ext.cors import CORS
file_handler= FileHandler("errorlog.txt")
file_handler.setLevel(WARNING)

print(pathlib.Path(__file__).parent.absolute())
os.chdir(pathlib.Path(__file__).parent.absolute())
# os.chdir('D:/atc')  ####################Change path Here
project_path = os.getcwd()
app = Flask(__name__)
app.config['SECRET_KEY'] = "hjhl"
app.config['JSON_SORT_KEYS'] = False
app.logger.addHandler(file_handler)
#CORS(app)
################################Login Database Creation 
# #ctrl+1 for commenting and uncommenting
# conn = sqlite3.connect(project_path + '/static/database/atc_login_table.db')
# cursor = conn.cursor()

# #Doping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS User")
# conn.commit()
# conn.close()
# #fields list - name, email, username, password, role,otp, status
# #Creating table as per requirement
# conn = sqlite3.connect(project_path + '/static/database/atc_login_table.db')
# cursor = conn.cursor()
# sql ='''CREATE TABLE User(
#     name CHAR(20) NOT NULL,
#     email CHAR(20) NOT NULL,
#     username CHAR(20) NOT NULL,
#     password CHAR(20) NOT NULL,
#     role CHAR(20) NOT NULL,
#     otp CHAR(20) NOT NULL,
#     status CHAR(20) NOT NULL
# )'''
# cursor.execute(sql)
# conn.commit()
# conn.close()
##############################

#########writing admins to User database
# conn = sqlite3.connect(project_path + '/static/database/atc_login_table.db')
# cursor = conn.cursor()
# cursor.execute('''INSERT INTO User(name, email, username, password, role, otp, status) VALUES 
#     ('Ramana murthy','busetty.ramana@gmail.com','Ramana','anooshaa@999','admin','123','Y')''')  
# cursor.execute('''INSERT INTO User(name, email, username, password, role, otp, status) VALUES 
#     ('Dinesh Busetty','busetty.dinesh@gmail.com','Dinesh','Idinu143@atc','admin','456','Y')''')
# conn.commit()
# conn.close()
##############

#################Retrieve info from login database
# conn = sqlite3.connect(project_path + '/static/database/atc_login_table.db')
# cursor = conn.cursor()
# cursor.execute("select * FROM User")
# table = cursor.fetchall()
# conn.commit()
# conn.close()
# print(table)
###############
############################Droping all tables and creating new table$$$$$$$$$$$$$$$$ Starting point
#ctrl+1 for commenting and uncommenting
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS PlywoodCountTable")
# conn.commit()
# conn.close()
#
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# sql ='''CREATE TABLE PlywoodCountTable(
#     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_type CHAR(50) NOT NULL,
#     product_name CHAR(50) NOT NULL,
#     size CHAR(50) NOT NULL,
#     thickness CHAR(50) NOT NULL,
#     Count_num INT(20) NOT NULL
# )'''
# cursor.execute(sql)
# conn.commit()
# conn.close()
#
# #Droping EMPLOYEE table if already exists.
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS PlywoodCreditTable")
# conn.commit()
# conn.close()
# #ctrl+1 for commenting and uncommenting
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# sql ='''CREATE TABLE PlywoodCreditTable(
#     credit_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(50) NOT NULL,
#     mobileno CHAR(20) NOT NULL,
#     total_credit FLOAT(20) NOT NULL
# )'''
# cursor.execute(sql)
# conn.commit()
# conn.close()
#
# #ctrl+1 for commenting and uncommenting
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS OrdersTable")
# conn.commit()
# conn.close()
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# sql ='''CREATE TABLE OrdersTable(
#     order_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(50) NOT NULL,
#     mobileno CHAR(10) NOT NULL,
#     order_date CHAR(50) NOT NULL,
#     order_items INT(20) NOT NULL,
#     total_amount FLOAT(20) NOT NULL,
#     after_discount_amount FLOAT(20) NOT NULL,
#     paid_amount FLOAT(20) NOT NULL,
#     running_total FLOAT(20) NOT NULL,
#     notes CHAR(50) NOT NULL
# )'''
# cursor.execute(sql)
# conn.commit()
# conn.close()
#
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS Orderitems")
# conn.commit()
# conn.close()
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# sql ='''CREATE TABLE Orderitems(
#     order_id INT(50) NOT NULL,
#     product_type CHAR(50) NOT NULL,
#     product_name CHAR(50) NOT NULL,
#     size CHAR(50) NOT NULL,
#     thickness CHAR(50) NOT NULL,
#     count INT(20) NOT NULL,
#     amount FLOAT(20) NOT NULL
# )'''
# cursor.execute(sql)
# conn.commit()
# conn.close()
#
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS PlywoodCounthistory")
# conn.commit()
# conn.close()
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# sql ='''CREATE TABLE PlywoodCounthistory(
#     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     product_type CHAR(50) NOT NULL,
#     product_name CHAR(50) NOT NULL,
#     size CHAR(50) NOT NULL,
#     thickness CHAR(50) NOT NULL,
#     Count_num INT(20) NOT NULL,
#     posted_date CHAR(50) NOT NULL,
#     posted_user CHAR(50) NOT NULL
# )'''
# cursor.execute(sql)
# conn.commit()
# conn.close()
# #ctrl+1 for commenting and uncommenting
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# cursor.execute("DROP TABLE IF EXISTS ChequeTable")
# conn.commit()
# conn.close()
# conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
# cursor = conn.cursor()
# sql ='''CREATE TABLE ChequeTable(
#     Cheque_id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name CHAR(50) NOT NULL,
#     mobileno CHAR(10) NOT NULL,
#     order_date CHAR(50) NOT NULL,
#     passing_date CHAR(50) NOT NULL,
#     amount FLOAT(20) NOT NULL,
#     validated CHAR(10) NOT NULL
# )'''
# cursor.execute(sql)
# conn.commit()
# conn.close()
# #######################################################################################################



def send_email(to_email, subject, body):#body_dict
    fromaddr = "busetty.dinesh@gmail.com"
    # toaddr = ["Dinesh.Bu@tsincor.com", email]
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = to_email
    msg['Subject'] = subject
    body = body#"Hi,\n\nLink for Activating {}: {}\n\nhttp://127.0.0.1:8000/api/activation/{}_{}".format(body_dict["role"],body_dict["username"], body_dict["username"], body_dict["otp"])
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    # Next, log in to the server
    
    server.login(fromaddr, "Idinu143@avaya")#https://myaccount.google.com/lesssecureapps?pli=1 for permission
    text = msg.as_string()
    server.sendmail(fromaddr, "{}".format(to_email), text)
    server.quit()
          

@app.route('/api/register', methods=['POST'])
def register():
    register_data = request.get_json()
    print(register_data)
    username = register_data.get("username", None)
    password = register_data.get("password", None)
    name = register_data.get("name", None)
    email = register_data.get("email", None)
    role = register_data.get("role", None)
    # TODO reverse name standardize status outputs
    # if User.query.filter_by(username=username.lower()).first():
    con = sqlite3.connect(project_path + '/static/database/atc_login_table.db')
    cursor = con.cursor()
    cursor.execute("select * FROM User where username ='{}' ".format(username))
    rows = cursor.fetchall()
    a = len(rows)
    cursor.execute("select * FROM User where email='{}' ".format(email))
    rows1 = cursor.fetchall()
    b = len(rows1)
    
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if(regex.search(username) != None or username.__contains__(" ")): 
        print("special characters are not allowed in User Name")
        return jsonify({"status": "FAILURE", "message": "special characters are not allowed in User Name"})
    elif a != 0:
        print("Username exists")
        return jsonify({"status": "FAILURE", "message": "Username already Registered"})   
    elif b != 0:
        print("email exists")
        return jsonify({"status": "FAILURE", "message": "Email already Registered"})   
    else:
        print("register success")
        otp = str(randint(1000, 9999))
        # user = User(username=username, password=password, name=name, email=email, role='user', otp=otp, status="N")
        role = "user"
        status = "N"
        body="Hi,\n\nLink for Activating role - {}: {}\n\nhttp://{}:8000/api/activation/{}_{}".format(role,username,app_host, username, otp)
    
        cursor.execute(
            "INSERT INTO User VALUES ('{}','{}','{}','{}','{}','{}','{}')".format(name, email, username, password, role,
                                                                                  otp, status))
        con.commit()
        send_email(to_email="busetty.dinesh@gmail.com", subject="ATC User Activation",body=body)
        return jsonify({"status": "success", "message": "successfully Register"})


@app.route('/api/activation/<user_otp>', methods=['GET'])
def activation(user_otp):
    username, otp = user_otp.split("_")
    #user = User.query.filter_by(username=username).first()
    #print(user.otp, otp)
    con = sqlite3.connect(project_path + '/static/database/atc_login_table.db')
    cursor=con.cursor()
    cursor.execute("select * FROM User where username ='{}'".format(username))
    rows1=cursor.fetchall()
    if rows1[0][6] != "Y" and rows1[0][5] == otp:
        cursor.execute('''update User set status =? where username=?''',("Y",username))
        #cur.execute(sql, task)
        #db.session.add(user)
        con.commit()
        print("activation success")
        return jsonify({"status": "SUCCESS", "message": "SUCCESS"})
    else:
        print("activation failed")
        return jsonify({"status": "FAILURE", "message": "Verify User or OTP"})


@app.route('/api/login', methods=['POST'])
def login():
    req_data = request.get_json()
    print(req_data)
    username = req_data['username']
    password = req_data['password']
    con = sqlite3.connect(project_path + "/static/database/atc_login_table.db")
    cursor = con.cursor()
    # cursor.execute("create table User (name text,email text,username text,password text,role text,otp text,status text)")
    cursor.execute("select * FROM User where USERNAME ='{}'".format(username))
    # cursor.execute("select * FROM APEX_ED.dbo.login_table")
    rows = cursor.fetchall()
    if len(rows) > 0:
        if password == rows[0][3] and rows[0][-1] == 'Y':
            sta = {"status": "success", 
                   "data": {"message": "Successful Login",
                            "username": "{}".format(username), 
                            "name": "{}".format(username),
                            "role": "{}".format(rows[0][4])}}
        elif rows[0][-1] == 'N' or rows[0][-1] == 'n':
            sta = {"status": "failure", "message": "user activation pending"}
        else:
            sta = {"status": "failure", "message": "Failure Login"}
    else:
        sta = {"status": "failure", "message": "Failure Login"}
    print(sta)
    con.close()
    return jsonify(sta)

@app.route("/api/forgot", methods=["POST"])
def forgot():
    req_data = request.get_json()
    email = req_data['email']
    con = sqlite3.connect(project_path + "/static/database/atc_login_table.db")
    cursor = con.cursor()
    cursor.execute("select * FROM User where EMAIL='{}' ".format(email))
    row2 = cursor.fetchall()
    if len(row2) == 1:
        body = "ATC details:\n\t UserName is {} \n\t Password for is {}".format(row2[0][2],row2[0][3])
        send_email(to_email="busetty.dinesh@gmail.com", subject="UserName and Password Details for ATC",body=body)
        sta = {"status": "success", "message": "username and password has been sent to your mail"}
    else:
        sta = {"status": "FAILURE", "message": "NO SUCH MAIL ID IS REGISTERED"}
    con.close()
    return jsonify(sta)       
           
@app.route("/")
def home():
    return render_template("index.html")

def size_cal(zz):
    if "kg" in zz or "ltr" in zz:
        frn1=float(zz.split(" ")[0]) * 1000
    elif "gms" in zz or "ml" in zz:
        frn1=float(zz.split(" ")[0])
    elif " x " in zz:
        frn = zz.split(" x ")
        frn1 = float(frn[0]) * float(frn[1])
        if frn1> 100:
            frn1 = frn1/144
    return frn1

def thickness_cal(zz):
    if "ft" in zz:
        frn1=float(zz.split(" ")[0]) * 300
    elif "mm" in zz:
        frn1=float(zz.split(" ")[0])
    else:
        frn1=float(0)
    return frn1

@app.route("/api/getProducts", methods=["POST"])#to view all data from
def getProducts():
    req_data = request.get_json()#plywood,size,mm,Count_num
    product_type=req_data["product_type"]
    product_name=req_data["product_name"]
    thickness=req_data["thickness"]
    size=req_data["size"]
    weight=req_data["weight"]
    if product_type=="Gum":
        size=weight
    
    if product_type=="" and product_name=="" and thickness=="" and size=="":
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute("select * FROM PlywoodCountTable")
        row = cursor.fetchall()
        countdf=pd.DataFrame(row)
        countdf.columns=["product_id","product_type","product_name","size","thickness","stock"]
        countdf["size_val"] = list(countdf["size"].map(size_cal))
        countdf["thickness_val"] = list(countdf["thickness"].map(thickness_cal))
        countdf.sort_values(by=['product_type','product_name',"thickness_val","size_val"],ascending = [False, True, True, False],inplace=True)
        countdf.drop(["size_val","thickness_val"], axis =1, inplace=True)
        countdf = countdf.to_json(orient="records")
        con.close()
        return jsonify({"status":"success","data":json.loads(countdf)})
    else:
        struc={"product_type":product_type,"product_name":product_name,"thickness":thickness,"size":size}
        non_null_values=[]
        for a,b in struc.items():
            if b!="":
                non_null_values.append('{}=="{}"'.format(a,b))
                
        qry= " where "+" and ".join(non_null_values)
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute("select * FROM PlywoodCountTable"+qry)
        row = cursor.fetchall()
        if len(row)>0:
            countdf=pd.DataFrame(row)
            countdf.columns=["product_id","product_type","product_name","size","thickness","stock"]
            countdf["size_val"] = list(countdf["size"].map(size_cal))
            countdf["thickness_val"] = list(countdf["thickness"].map(thickness_cal))
            countdf.sort_values(by=['product_type', 'product_name', "thickness_val", "size_val"],
                                ascending=[False, True, True, False], inplace=True)
            countdf.drop(["size_val", "thickness_val"], axis=1, inplace=True)
            countdf = countdf.to_json(orient="records")
            con.close()
            return jsonify({"status":"success","data":json.loads(countdf)})
        else:
            con.close()
            return jsonify({"status":"failure","data":"no data"})

@app.route("/api/updateProduct", methods=["POST"])#to view all data from
def updateProduct(): 
#     req_data={"data":{
# "count": 100,
# "length": "50 gms",
# "product_id": 29,
# "product_name": "WATERBOND",
# "product_type": "Gum",
# "thickness": "",
# "weight": "50",
# "weight_type": "kg"}}
#req_data={"username":"Dinesh","data":{"product_type":"Gum","product_id":144,"product_name":"allrounder","length":"125 gms","thickness":"","weight":"125","weight_type":"gms","count":"201"},"role":"admin"}
    req_data = request.get_json()
    print(req_data)
    count=req_data["data"]["count"]
    username=req_data["username"]
    product_name=req_data["data"]["product_name"]
    product_type=req_data["data"]["product_type"]
    thickness=req_data["data"]["thickness"]
    weight=req_data["data"]["weight"]
    order_date=date.today()
    order_date = order_date.strftime("%Y-%m-%d")
    
    product_id=req_data["data"]["product_id"]
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    if product_type=="Plywood":
        thickness_type=req_data["data"]["thickness_type"]
        length=req_data["data"]["length"]
        width=req_data["data"]["width"]
        size='''{} x {}'''.format(length,width)
        thickness="{} {}".format(thickness,thickness_type)
        cursor.execute("select Count_num FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}'".format(product_type,product_name,size,thickness,count))
        count_history = cursor.fetchall()
        count_history=count_history[0][0]
        cursor.execute("update PlywoodCountTable set Count_num ='{}',product_type='{}',product_name='{}',size='{}',thickness='{}' where product_id='{}' ".format(count,product_type,product_name,size,thickness,product_id))
        cursor.execute('''INSERT INTO PlywoodCounthistory(product_type,product_name, size, thickness, Count_num, posted_date, posted_user) VALUES 
            ('{}','{}','{}','{}','{}','{}','{}')'''.format(product_type,product_name,size,thickness,int(count)-int(count_history),order_date,username))  
        conn.commit()
    else:
        weight_type=req_data["data"]["weight_type"]
        size='''{} {}'''.format(weight,weight_type)
        cursor.execute("select Count_num FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}'".format(product_type,product_name,size,thickness,count))
        count_history = cursor.fetchall()
        count_history=count_history[0][0]
        cursor.execute("update PlywoodCountTable set Count_num ='{}',product_type='{}',product_name='{}',size='{}',thickness='{}' where product_id='{}' ".format(count,product_type,product_name,size,thickness,product_id))
        cursor.execute('''INSERT INTO PlywoodCounthistory(product_type,product_name, size, thickness, Count_num, posted_date, posted_user) VALUES 
            ('{}','{}','{}','{}','{}','{}','{}')'''.format(product_type,product_name,size,thickness,int(count)-int(count_history),order_date,username))  
        conn.commit()
    conn.close()
    return jsonify({"status":"success","message":"succesfully updated"}) 
        

@app.route("/api/addProduct", methods=["POST"])#to view all data from
def addProduct():
    #req_data={'username': 'Dinesh', 'data': {'product_type': 'Plywood', 'product_id': '', 'product_name': 'abc', 'width': 2, 'length': 4, 'thickness': 5, 'thickness_type': 'mm', 'weight': '', 'weight_type': '', 'count': '5'}, 'role': 'admin'}
    
    req_data = request.get_json()#plywood,size,mm,Count_num
    print(req_data)
    username=req_data["username"]
    product_type=req_data["data"]["product_type"]
    product_name=req_data["data"]["product_name"]
    thickness=req_data["data"]["thickness"]
    count=req_data["data"]["count"]
    width=req_data["data"]["width"]
    weight=req_data["data"]["weight"]
    order_date=date.today()
    order_date = order_date.strftime("%Y-%m-%d")
    
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute("select product_id from PlywoodCountTable")
    cnt_val=cursor.fetchall()
    print("cnt_valll-",cnt_val)
    cnt_val=[h[0] for h in cnt_val]
    print("cnt_val-",cnt_val)
    #cnt_val=int(cnt_val)
    product_id=max(cnt_val)
    product_id+=1
    conn.close()
    if product_type=="Plywood":
        length=req_data["data"]["length"]
        thickness_type=req_data["data"]["thickness_type"]
        size="{} x {}".format(length,width)
        thickness="{} {}".format(thickness,thickness_type)
        conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
        cursor = conn.cursor()

        cursor.execute('''INSERT INTO PlywoodCounthistory(product_type,product_name, size, thickness, Count_num, posted_date, posted_user) VALUES 
            ('{}','{}','{}','{}','{}','{}','{}')'''.format(product_type,product_name,size,thickness,count,order_date,username))  
        conn.commit()
        cursor.execute("select * FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}'".format(product_type,product_name,size,thickness,count))
        row = cursor.fetchall()
        if len(row)==0:
            cursor.execute('''INSERT INTO PlywoodCountTable(product_id,product_type,product_name, size, thickness, Count_num) VALUES 
            ('{}','{}','{}','{}','{}','{}')'''.format(product_id,product_type,product_name,size,thickness,count))  
            conn.commit()
            conn.close()
        else:
            previous_count=row[0][-1]
            count=int(count)+int(previous_count)
            cursor.execute("update PlywoodCountTable set Count_num ='{}' where product_type='{}' and product_name='{}' and size='{}' and thickness='{}'".format(count,product_type,product_name,size,thickness))
            conn.commit()
            conn.close()           
    elif product_type=="Gum":
        weight_type=req_data["data"]["weight_type"]
        size="{} {}".format(weight,weight_type)
        conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO PlywoodCounthistory(product_type,product_name, size, thickness, Count_num, posted_date, posted_user) VALUES 
            ('{}','{}','{}','{}','{}','{}','{}')'''.format(product_type,product_name,size,thickness,count,order_date,username))  
        conn.commit()
        cursor.execute("select * FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}'".format(product_type,product_name,size,thickness,count))
        row = cursor.fetchall()
        if len(row)==0:
            cursor.execute('''INSERT INTO PlywoodCountTable(product_id,product_type,product_name, size, thickness, Count_num) VALUES 
            ('{}','{}','{}','{}','{}','{}')'''.format(product_id,product_type,product_name,size,thickness,count))  
            conn.commit()
            conn.close()
        else:
            previous_count=row[0][-1]
            count=int(count)+int(previous_count)
            cursor.execute("update PlywoodCountTable set Count_num ='{}' where product_type='{}' and product_name='{}' and size='{}' and thickness='{}'".format(count,product_type,product_name,size,thickness))
            conn.commit()
            conn.close()
    sta = {"status": "success","message":"successfully updated"}
    return jsonify(sta)



@app.route("/api/getUsers", methods=["POST"])#to view all data from
def getUsers():
    req_data = request.get_json()
    name=req_data['name']
    mobileno=req_data['mobile_number']
    if name=="" and mobileno=="":
        conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
        cursor = conn.cursor()
        cursor.execute("select * FROM PlywoodCreditTable")
        row = cursor.fetchall()
        countdf=pd.DataFrame(row)
        countdf.columns=["user_id","name","mobile_number","credit"]
        countdf = countdf.to_json(orient="records")
        conn.close()
        return jsonify({"status":"success","data":json.loads(countdf)})
    else:
        struc={"name":name,"mobileno":mobileno}
        non_null_values=[]
        for a,b in struc.items():
            if b!="":
                non_null_values.append('{} LIKE "%{}%"'.format(a,b))
        qry= " where "+" and ".join(non_null_values)
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute("select * FROM PlywoodCreditTable"+qry)
        row = cursor.fetchall()
        if len(row)!=0:
            countdf=pd.DataFrame(row)
            countdf.columns=["user_id","name","mobile_number","credit"]
            countdf = countdf.to_json(orient="records")
            con.close()
            return jsonify({"status":"success","data":json.loads(countdf)})
        else:
            return jsonify({"status":"failure","data":"no records found"})
    
@app.route("/api/getUserDetails", methods=["POST"])#to view all data from
def getUserDetails():
    req_data = request.get_json()
    name=req_data['name']
    mobileno=req_data['mobile_number']
    struc={"name":name,"mobileno":mobileno}
    non_null_values=[]
    for a,b in struc.items():
        if b!="":
            non_null_values.append('{}=="{}"'.format(a,b))               
    qry= " where "+" and ".join(non_null_values)
    con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
    cursor = con.cursor()
    cursor.execute("select * FROM PlywoodCreditTable"+qry)
    row = cursor.fetchall()
    if len(row)==1:
        countdf=pd.DataFrame(row)
        countdf.columns=["user_id","name","mobile_number","credit"]
        countdf["userExisted"]="1"
        #countdf=countdf[countdf.columns[1:]]
        countdf = countdf.to_json(orient="records")
        con.close()
        return jsonify({"status":"success","data":json.loads(countdf)[0]})
    else:
        con.close()
        return jsonify({"status":"success","data":{'userExisted': '0'}})
    
@app.route("/api/createUser", methods=["POST"])#to view all data from
def createUser():
    req_data = request.get_json()
    name=req_data["data"]['name']
    mobileno=req_data["data"]['mobile_number']
    credit=req_data["data"]['credit']
    con = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = con.cursor()
    cursor.execute("select * FROM PlywoodCreditTable where name ='{}' ".format(name))
    rows = cursor.fetchall()
    a = len(rows)
    # cursor.execute("select * FROM PlywoodCreditTable where mobileno='{}' ".format(mobileno))
    # rows1 = cursor.fetchall()
    # b = len(rows1)
    
    if a != 0:
        print("Username exists")
        return jsonify({"status": "FAILURE", "message": "Username already Registered"})   
    # elif b != 0:
    #     print("mobileno exists")
    #     return jsonify({"status": "FAILURE", "message": "mobileno already Registered"})   
    else:
        print("register success")
        cursor.execute("select credit_id FROM PlywoodCreditTable".format(name))
        rows = cursor.fetchall()
        rows=[j[0] for j in rows]
        credit_id = max(rows)+1
        # cursor.execute("DELETE  FROM PlywoodCreditTable where credit_id IS NULL")
        # con.commit()
        # rows1 = cursor.fetchall()
        cursor.execute('''INSERT INTO PlywoodCreditTable(credit_id,name,mobileno,total_credit) VALUES 
                       ('{}','{}','{}','{}')'''.format(credit_id,name,mobileno,credit))
        con.commit()
        cursor.execute('''select credit_id from  PlywoodCreditTable where name="{}"'''.format(name))
        rows = cursor.fetchall()
        credit_id=rows[0][0]
        con.close()
        return jsonify({"status":"success","message":"succesfully added client","user_id":credit_id })

@app.route("/api/submitOrder", methods=["POST"])#to view all data from
def submitOrder():
    
    req_data = request.get_json()  
    total_amount=req_data["amount_details"]["total_amount"]
    after_discount_amount=float(req_data["amount_details"]["discount_amount"])
    paid_amount=float(req_data["amount_details"]["paid_amount"])
    if "notes" not in req_data["amount_details"]:
        notes = ""
    else:
        notes = req_data["amount_details"]["notes"]
    name=req_data["user_data"]["name"]
    mobileno=req_data["user_data"]["mobile_number"]
    credit=req_data["user_data"]["credit"]
    paying_as=req_data["user_data"]["paying_as"]
    ord_date=req_data["order_date"]
    
    order_item_products=pd.DataFrame.from_dict(req_data["order_items"])
    if paying_as=="":
        return jsonify({"status":"failure","message":"please add paying type CASH or CREDIT"})
    else:
        con = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
        cursor = con.cursor()
        
        for i in range(len(order_item_products)):
            if order_item_products["product_type"][i]=="Gum":
                order_item_products["size"][i]=order_item_products["weight"][i]
        
        product_checklist=[]
        for i in range(len(order_item_products)):
            cursor.execute("select count_num FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}' ".format(order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i]))
            row2=len(cursor.fetchall())>0
            product_checklist.append(row2)
            print(all(ele == True for ele in product_checklist))
        if all(ele == True for ele in product_checklist) or order_item_products["product_type"][0] == "cash":
            cursor.execute("select * FROM PlywoodCreditTable where name ='{}' ".format(name))
            rows = cursor.fetchall()
            if paying_as=="Cash":
                old_credit=0
                name="Cash Party"
            else:
                old_credit=rows[0][-1]
            credit=after_discount_amount+credit-paid_amount
            cursor.execute('''update PlywoodCreditTable set total_credit =? where name=? and mobileno=?''',(credit,name,mobileno))
            # con.commit()
            
            order_date=ord_date#date.today()#need to change
            # order_date = datetime.strptime(order_date,"%Y-%m-%d")#order_date.strftime("%d/%m/%Y")
            # order_date=order_date.strftime("%d/%m/%Y")
            order_items=len(order_item_products)
            cursor.execute('''INSERT INTO OrdersTable(name, mobileno, order_date, order_items,total_amount,after_discount_amount,paid_amount,running_total,notes) VALUES 
                    ('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(name,mobileno,order_date,order_items,total_amount,after_discount_amount,paid_amount,credit,notes))
            # con.commit()
            
            cursor.execute('''select order_id from OrdersTable where name=="{}" and mobileno=="{}" and order_date=="{}" and order_items=="{}" and total_amount=="{}" and after_discount_amount=="{}" and paid_amount=="{}" and running_total=="{}" and notes=="{}"
                    '''.format(name,mobileno,order_date,order_items,total_amount,after_discount_amount,paid_amount,credit,notes))
            rows1 = cursor.fetchall()
            order_id=rows1[0][0]
            
            order_item_products["order_id"]=order_id
            order_item_products=order_item_products[['order_id','product_type', 'product_name', 'size', 'thickness', 'count','amount']]
            for i in range(len(order_item_products)):
                cursor.execute('''INSERT INTO Orderitems(order_id, product_type, product_name, size,thickness,count,amount) VALUES 
                        ('{}','{}','{}','{}','{}','{}','{}')'''.format(order_item_products["order_id"][i],order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i],order_item_products["count"][i],order_item_products["amount"][i]))
                cursor.execute("select count_num FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}' ".format(order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i]))
                row2=cursor.fetchall()
                try:
                    old_count=(row2[0][0])
                    new_count=old_count-int(order_item_products["count"][i])
                    cursor.execute("update PlywoodCountTable set count_num ='{}' where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}' ".format(new_count,order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i]))
                except:
                    pass
            con.commit()
            con.close()
            return jsonify({"status":"success","message":"succesfully submitted data"})
        else:
            con.close()
            return jsonify({"status":"failure","message":"failed to submit data"})
        
@app.route("/api/returnOrder", methods=["POST"])#to view all data from
def returnOrder():
    #req_data={"username":"Dinesh","order_items":[{"product_type":"Plywood","product_id":-1,"product_name":"byson lam","size":"6 x 4","thickness":"8 mm","weight":"","amount":4563,"count":20}],"user_data":{"paying_as":"Credit","mobile_number":"","name":"konark","user_id":2,"IsNewUser":"0","credit":25100},"amount_details":{"total_amount":4563,"discount_amount":"4500","paid_amount":"4500"},"role":"admin"}
    
    req_data = request.get_json()  
    total_amount=req_data["amount_details"]["total_amount"]
    after_discount_amount=float(req_data["amount_details"]["discount_amount"])
    paid_amount=float(req_data["amount_details"]["paid_amount"])
    if "notes" not in req_data["amount_details"]:
        notes = ""
    else:
        notes = req_data["amount_details"]["notes"]
    name=req_data["user_data"]["name"]
    mobileno=req_data["user_data"]["mobile_number"]
    credit=req_data["user_data"]["credit"]
    paying_as=req_data["user_data"]["paying_as"]
    ord_date=req_data["order_date"]
    
    order_item_products=pd.DataFrame.from_dict(req_data["order_items"])
    if paying_as=="":
        ""#return jsonify({"status":"failure","message":"please add paying type CASH or CREDIT"})
    else:
        con = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
        cursor = con.cursor()
        
        for i in range(len(order_item_products)):
            if order_item_products["product_type"][i]=="Gum":
                if "weight" in order_item_products.columns:
                    order_item_products["size"][i]=order_item_products["weight"][i]
        
        product_checklist=[]
        for i in range(len(order_item_products)):
            cursor.execute("select count_num FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}' ".format(order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i]))
            row2=len(cursor.fetchall())>0
            product_checklist.append(row2)
            # print(all(ele == True for ele in product_checklist))


        if all(ele == True for ele in product_checklist) or order_item_products["product_type"][0] == "cash":
            cursor.execute("select * FROM PlywoodCreditTable where name ='{}' ".format(name))
            rows = cursor.fetchall()
            if paying_as=="Cash":
                old_credit=0
                name="Cash Party"
            else:
                old_credit=rows[0][-1]
            if order_item_products["product_type"][0] == "cash":
                credit = credit + paid_amount
            else:
                credit=credit-after_discount_amount+paid_amount
            cursor.execute('''update PlywoodCreditTable set total_credit =? where name=? and mobileno=?''',(credit,name,mobileno))
            # con.commit()
            
            order_date=ord_date#date.today()
            # order_date = datetime.strptime(order_date,"%Y-%m-%d")#order_date.strftime("%d/%m/%Y")
            # order_date=order_date.strftime("%d/%m/%Y")
            order_items=len(order_item_products)
            cursor.execute('''INSERT INTO OrdersTable(name, mobileno, order_date, order_items,total_amount,after_discount_amount,paid_amount,running_total,notes) VALUES 
                    ('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(name,mobileno,order_date,-order_items,-total_amount,-after_discount_amount,-paid_amount,credit,notes))
            # con.commit()
            
            cursor.execute('''select order_id from OrdersTable where name=="{}" and mobileno=="{}" and order_date=="{}" and order_items=="{}" and total_amount=="{}" and after_discount_amount=="{}" and paid_amount=="{}" and running_total=="{}" and notes=="{}"
                    '''.format(name,mobileno,order_date,-order_items,-total_amount,-after_discount_amount,-paid_amount,credit,notes))

            rows1 = cursor.fetchall()
            order_id=rows1[0][0]
            
            order_item_products["order_id"]=order_id
            order_item_products=order_item_products[['order_id','product_type', 'product_name', 'size', 'thickness', 'count','amount']]
            for i in range(len(order_item_products)):
                cursor.execute('''INSERT INTO Orderitems(order_id, product_type, product_name, size,thickness,count,amount) VALUES 
                        ('{}','{}','{}','{}','{}','{}','{}')'''.format(order_item_products["order_id"][i],order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i],-order_item_products["count"][i],-order_item_products["amount"][i]))
                cursor.execute("select count_num FROM PlywoodCountTable where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}' ".format(order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i]))
                row2=cursor.fetchall()
                try:
                    old_count=(row2[0][0])
                    new_count=old_count+int(order_item_products["count"][i])
                    cursor.execute("update PlywoodCountTable set count_num ='{}' where product_type=='{}' and product_name=='{}' and size=='{}' and thickness=='{}' ".format(new_count,order_item_products["product_type"][i],order_item_products["product_name"][i],order_item_products["size"][i],order_item_products["thickness"][i]))
                except:
                    pass
            con.commit()
            con.close()
            return jsonify({"status":"success","message":"succesfully submitted data","order_id":order_id,"credit":credit})
        else:
            con.close()
            return jsonify({"status":"failure","message":"failed to submit data"})

def get_order_items(order_id):
    con = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = con.cursor()
    cursor.execute('''select * from Orderitems where order_id=="{}" '''.format(order_id)) 
    rows = cursor.fetchall()
    if len(rows)>0:
        itemsdf=pd.DataFrame(rows)
        itemsdf.columns=["order_id","product_type","product_name","size","thickness","count","amount"]
        itemsdf=itemsdf[["product_type","product_name","size","thickness","count","amount"]]
        itemsdf = itemsdf.to_json(orient="records")
    else:
        itemsdf=pd.DataFrame([["","","","","","",""]])
        itemsdf.columns=["order_id","product_type","product_name","size","thickness","count","amount"]
        itemsdf=itemsdf[["product_type","product_name","size","thickness","count","amount"]]
        itemsdf = itemsdf.to_json(orient="records")
    return json.loads(itemsdf)
    
@app.route("/api/getOrders", methods=["POST"])#to view all data from
def getOrders():
    # req_data={"mobile_number":"","order_date":"","name":"","pageCounter":1,"username":"Dinesh","role":"admin"}
    req_data = request.get_json()  
    name=req_data["name"]
    mobileno=req_data["mobile_number"]
    order_date_from=req_data["order_date_from"]
    order_date_to=req_data["order_date_to"]
    # if order_date_from!="":
    #     dto=datetime.strptime(order_date_from, "%Y-%m-%d")
    #     order_date_from=dto.strftime("%d/%m/%Y")
    #
    # if order_date_to!="":
    #     dto=datetime.strptime(order_date_to, "%Y-%m-%d")
    #     order_date_to=dto.strftime("%d/%m/%Y")

    con = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = con.cursor()
    if name=="" and mobileno=="" and order_date_from=="" and order_date_to=="":
        cursor.execute('''select * from OrdersTable ''') 
        rows = cursor.fetchall()
        countdf=pd.DataFrame(rows)
        countdf.columns=["order_id","user_name","mobile_number","order_date","order_items_count","total_amount","discount_amount","paid_amount","running_total","notes"]
        countdf["order_items_list"]=list(map(get_order_items,countdf.order_id))
        # cursor.execute('''select name,total_credit from PlywoodCreditTable ''')
        # rows = cursor.fetchall()
        # usersdf = pd.DataFrame(rows)
        countdf = countdf.to_json(orient="records")
        return jsonify({"status":"success","data":json.loads(countdf)})
    else:
        struc={"name":name,"mobileno":mobileno,"order_date_from":order_date_from,"order_date_to":order_date_to}
        non_null_values=[]
        for a,b in struc.items():
            if b!="":
                if a == "order_date_from":
                    non_null_values.append('order_date >= "{}"'.format(b))
                elif a == "order_date_to":
                    non_null_values.append('order_date <= "{}"'.format(b))
                else:
                    non_null_values.append('{} like "%{}%"'.format(a,b))
        qry= " where "+" and ".join(non_null_values)
        # print('''select * from OrdersTable {} '''.format(qry))
        cursor.execute('''select * from OrdersTable {} '''.format(qry)) 
        rows = cursor.fetchall()
        con.close()
        if len(rows)!=0:
            countdf=pd.DataFrame(rows)
            countdf.columns=["order_id","user_name","mobile_number","order_date","order_items_count","total_amount","discount_amount","paid_amount","running_total","notes"]
            countdf["order_items_list"]=list(map(get_order_items,countdf.order_id))
            countdf = countdf.to_json(orient="records")
            return jsonify({"status":"success","data":json.loads(countdf)})
        else:
            return jsonify({"status":"failure","data":"no records found"})

@app.route("/api/getOrderItems", methods=["POST"])#to view all data from
def getOrderItems():
    req_data = request.get_json()
    order_id=req_data["orderid"]
    con = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = con.cursor()
    cursor.execute('''select * from Orderitems where order_id=="{}" '''.format(order_id)) 
    rows = cursor.fetchall()
    countdf=pd.DataFrame(rows)   
    if len(rows)>0:
        itemsdf=pd.DataFrame(rows)
        itemsdf.columns=["order_id","product_type","product_name","size","thickness","count","amount"]
        itemsdf=itemsdf[["product_type","product_name","size","thickness","count","amount"]]

    else:
        itemsdf=pd.DataFrame([["","","","","","",""]])
        itemsdf.columns=["order_id","product_type","product_name","size","thickness","count","amount"]
        itemsdf=itemsdf[["product_type","product_name","size","thickness","count","amount"]]

    price_list= list()
    for row in range(itemsdf.shape[0]):
        if itemsdf.loc[row]["product_type"] == "Gum":
            price_list.append(itemsdf.loc[row]["amount"]/itemsdf.loc[row]["count"])
        elif itemsdf.loc[row]["product_type"] == "Plywood":
            eval_size = eval(itemsdf.loc[row]["size"].replace("x", "*"))
            if eval_size > 50:
                price_list.append((itemsdf.loc[row]["amount"] / (itemsdf.loc[row]["count"]*eval_size)) * 144)
            else:
                price_list.append((itemsdf.loc[row]["amount"] / (itemsdf.loc[row]["count"] * eval_size)))
    itemsdf["price"] = price_list
    itemsdf = itemsdf.to_json(orient="records")
    return jsonify({"status":"success","data":json.loads(itemsdf)})

@app.route("/api/getProductNamesList", methods=["POST"])#to view all data from
def getProductNamesList(): 
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute("select product_name FROM PlywoodCountTable" )
    row = cursor.fetchall()
    row=pd.DataFrame(row)
    row.sort_values(0,inplace=True)
    row.reset_index(drop=True,inplace=True)
    row.columns=["value"]
    row.drop_duplicates(inplace=True)
    row = row.to_json(orient="records")
    conn.close()
    return jsonify({"status":"success","data":json.loads(row)})

@app.route("/api/getSizesList", methods=["POST"])#to view all data from
def getSizesList(): 
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute("select size FROM PlywoodCountTable" )
    row = cursor.fetchall()
    row=pd.DataFrame(row)
    row.sort_values(0,inplace=True)
    row.reset_index(drop=True,inplace=True)
    row.columns=["value"]
    row.drop_duplicates(inplace=True)
    row = row.to_json(orient="records")
    conn.close()
    return jsonify({"status":"success","data":json.loads(row)})

@app.route("/api/getThicknessList", methods=["POST"])#to view all data from
def getThicknessList(): 
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute("select thickness FROM PlywoodCountTable" )
    row = cursor.fetchall()
    row=pd.DataFrame(row)
    row.sort_values(0,inplace=True)
    row.reset_index(drop=True,inplace=True)
    row.columns=["value"]
    row.drop_duplicates(inplace=True)
    row = row.to_json(orient="records")
    conn.close()
    return jsonify({"status":"success","data":json.loads(row)})
    
@app.route("/api/updateUserCredit", methods=["POST"])#to view all data from
def updateUserCredit(): 
    req_data = request.get_json()
    req_data=req_data["data"]
    mobileno=req_data["data"]["mobile_number"]
    name=req_data["data"]["name"]
    credit=req_data["data"]["credit"]
    paying_amount=req_data["data"]["paying_amount"]
    payment_type = req_data["data"]["payment_type"]
    ord_date = req_data["order_date"]
    if payment_type =="Cheque" and "passing_date" in req_data["data"]:
        passing_date = req_data["data"]["passing_date"]
        conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO ChequeTable(name, mobileno, order_date, passing_date,amount,validated) VALUES 
                    ('{}','{}','{}','{}','{}','{}')'''.format(name, mobileno, ord_date, passing_date,
                                                                             paying_amount, "No"))
        conn.commit()
        conn.close()
    credit=credit-paying_amount
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute('''update PlywoodCreditTable set total_credit =? where name=? and mobileno=?''',(credit,name,mobileno))
    conn.commit()
    order_date = ord_date  # date.today()
    # order_date = datetime.strptime(order_date, "%Y-%m-%d")  # order_date.strftime("%d/%m/%Y")
    # order_date = order_date.strftime("%d/%m/%Y")
    order_items=1
    total_amount=0
    after_discount_amount=0
    paid_amount=paying_amount
    notes = ""
    cursor.execute('''INSERT INTO OrdersTable(name, mobileno, order_date, order_items,total_amount,after_discount_amount,paid_amount,running_total,notes) VALUES 
            ('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(name,mobileno,order_date,order_items,total_amount,after_discount_amount,paid_amount,credit,notes))
    conn.commit()
    
    cursor.execute('''select order_id from OrdersTable where name=="{}" and mobileno=="{}" and order_date=="{}" and order_items=="{}" and total_amount=="{}" and after_discount_amount=="{}" and paid_amount=="{}" and running_total=="{}" and notes=="{}"
            '''.format(name,mobileno,order_date,order_items,total_amount,after_discount_amount,paid_amount,credit,notes))
    rows1 = cursor.fetchall()
    order_id=rows1[0][0]
    cursor.execute('''INSERT INTO Orderitems(order_id, product_type, product_name, size,thickness,count,amount) VALUES 
                ('{}','{}','{}','{}','{}','{}','{}')'''.format(order_id,"cash",payment_type,"","","1",paying_amount))
        
    conn.commit()
    conn.close()
    return jsonify({"status":"success","message":"succesfully updated"}) 
    

@app.route("/api/updateUser", methods=["POST"])#to view all data from
def updateUser(): 
    req_data = request.get_json()
    req_data=req_data["data"]
    mobileno=req_data["data"]["mobile_number"]
    name=req_data["data"]["name"]
    credit=req_data["data"]["credit"]
    credit_id=req_data["data"]["user_id"]
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute('''update PlywoodCreditTable set total_credit ="{}", name="{}" , mobileno="{}" where credit_id="{}"'''.format(credit,name,mobileno,credit_id))
    conn.commit()
    #################################
    ord_date = req_data["data"]["order_date"]
    order_date = ord_date  # date.today()
    # order_date = datetime.strptime(order_date, "%Y-%m-%d")  # order_date.strftime("%d/%m/%Y")
    # order_date = order_date.strftime("%d/%m/%Y")
    order_items = 1
    total_amount = 0
    after_discount_amount = 0
    paid_amount = credit
    notes = ""
    cursor.execute('''INSERT INTO OrdersTable(name, mobileno, order_date, order_items,total_amount,after_discount_amount,paid_amount,running_total,notes) VALUES 
            ('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(name, mobileno, order_date, order_items, total_amount,
                                                           after_discount_amount, paid_amount,credit,notes))
    conn.commit()

    cursor.execute('''select order_id from OrdersTable where name=="{}" and mobileno=="{}" and order_date=="{}" and order_items=="{}" and total_amount=="{}" and after_discount_amount=="{}" and paid_amount=="{}" and running_total=="{}"  and notes=="{}"
            '''.format(name, mobileno, order_date, order_items, total_amount, after_discount_amount, paid_amount,credit,notes))
    rows1 = cursor.fetchall()
    order_id = rows1[0][0]
    cursor.execute('''INSERT INTO Orderitems(order_id, product_type, product_name, size,thickness,count,amount) VALUES 
                ('{}','{}','{}','{}','{}','{}','{}')'''.format(order_id, "correction", "correction", "", "", "1",
                                                               credit))

    conn.commit()
    #################################

    conn.close()
    return jsonify({"status":"success","message":"succesfully updated"}) 

@app.route("/api/deleteUser", methods=["POST"])#to view all data from
def deleteUser(): 
    req_data = request.get_json()
    req_data=req_data["data"]
    credit_id=req_data["data"]["user_id"]
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM PlywoodCreditTable where credit_id="{}"'''.format(credit_id))
    conn.commit()
    conn.close()
    return jsonify({"status":"success","message":"succesfully deleted"}) 

@app.route("/api/getUserPagesAccess", methods=["POST"])#to view all data from
def getUserPagesAccess(): 
    req_data = request.get_json()
    print(req_data)
    role=req_data["data"]["role"]
    data={
      "orders_page": True,#false
      "products_page": True,
      "users_page": True,
      "products_history_page": True,
      "new_order_page": True,
      "user_edit": True,
      "product_add": True,
      "product_edit": True
    }
    if role=="user":
        data["users_page"]=False
        data["products_history_page"]=False
        data["user_edit"]=False
        data["product_edit"]=False

        
    return jsonify({"status": "success","data":data })
    

@app.route("/api/getProductsHistory", methods=["POST"])#to view all data from
def getProductsHistory(): 
    req_data = request.get_json()
  
    product_type=req_data["product_type"]
    product_name=req_data["product_name"]
    thickness=req_data["thickness"]
    size=req_data["size"]
    weight=req_data["weight"]
    posted_date=req_data["posted_date"]
    posted_user=req_data["posted_user"]
    # if posted_date!="":
    #     dto=datetime.strptime(posted_date, "%Y-%m-%d")
    #     posted_date=dto.strftime("%d/%m/%Y")
    if product_type=="Gum":
        size=weight
    
    if product_type=="" and product_name=="" and thickness=="" and size=="" and posted_date=="" and posted_user=="":
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute("select * FROM PlywoodCounthistory")
        row = cursor.fetchall()
        countdf=pd.DataFrame(row)
        countdf.columns=["product_id","product_type","product_name","size","thickness","stock","posted_date","posted_user"]
        countdf = countdf.to_json(orient="records")
        con.close()
        return jsonify({"status":"success","data":json.loads(countdf)})
    else:
        struc={"product_type":product_type,"product_name":product_name,"thickness":thickness,"size":size,"posted_date":posted_date,"posted_user":posted_user}
        non_null_values=[]
        for a,b in struc.items():
            if b!="":
                non_null_values.append('{}=="{}"'.format(a,b))
                
        qry= " where "+" and ".join(non_null_values)
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute("select * FROM PlywoodCounthistory"+qry)
        row = cursor.fetchall()
        if len(row)>0:
            countdf=pd.DataFrame(row)
            countdf.columns=["product_id","product_type","product_name","size","thickness","stock","posted_date","posted_user"]
            countdf = countdf.to_json(orient="records")
            con.close()
            return jsonify({"status":"success","data":json.loads(countdf)})
        else:
            con.close()
            return jsonify({"status":"failure","data":"no data"})
        
@app.route("/api/getUsersList", methods=["POST"])#to view all data from
def getUsersList(): 
    con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
    cursor = con.cursor()
    cursor.execute("select name FROM PlywoodCreditTable")
    rows = cursor.fetchall()
    countdf=pd.DataFrame(rows)
    countdf.columns=["name"]    
    return jsonify({"status":"success","data":list(countdf["name"])})

@app.route("/api/checkStock", methods=["POST"])
def checkStock(): 
    req_data = request.get_json()
# {
# "data":{
# "amount": 44,
# "count": 444,
# "product": "Plywood__19 mm__Block Board__8 x 4"
# },
# "role": "user",
# "username": "fgfhghg"
# }
    amount = req_data["data"]["amount"]
    count = req_data["data"]["count"]
    product = req_data["data"]["product"]
    if "Plywood__" in product:
        pz = product.split("__")
        product_type=pz[0]
        product_name=pz[2]
        size=pz[3]
        thickness=pz[1]
        weight = ""

    if "Gum__" in product:
        pz = product.split("__")
        product_type = pz[0]
        product_name = pz[1]
        size = pz[2]
        weight = pz[2]
        thickness = ""
    
    con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
    cursor = con.cursor()
    cursor.execute("select count(*) FROM PlywoodCountTable where product_type='{}' and product_name='{}' and size='{}' and thickness='{}'".format(product_type,product_name,size,thickness))
    rows = cursor.fetchall()
    countdf=rows[0][0]
    con.close()
    con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
    cursor = con.cursor()
    cursor.execute("select * FROM PlywoodCountTable where product_type='{}' and product_name='{}' and size='{}' and thickness='{}'".format(product_type,product_name,size,thickness))
    rows = cursor.fetchall()
    countdf1=rows[0][5]
    con.close()
    if countdf==0:
        return jsonify({"status":"failure", "stock":0})
    else:
        return jsonify({"status":"success","actual_count": countdf1, "stock":1,"data": {"amount":amount,"count":count,"product_type":product_type,
                                                               "product_name":product_name,"size":size,"thickness":thickness,
                                                               "weight":weight}})
    
@app.route("/api/deleteProduct", methods=["POST"])#to view all data from
def deleteProduct(): 
    req_data = request.get_json()
    product_id=req_data["data"]["product_id"]
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM PlywoodCountTable where product_id="{}"'''.format(product_id))
    conn.commit()
    conn.close()
    return jsonify({"status":"success","message":"succesfully deleted"}) 
           
@app.route("/api/signout", methods=["POST"])#to view all data from
def signout(): 
    return jsonify({"status":"success"})

@app.route("/api/loadproductscsv", methods=["POST"])#to view all data from
def loadproductscsv():
    req_data = request.get_json()
    a_file=pd.DataFrame(req_data["uploads"])
    a_file = a_file[~ a_file["product_id"].isnull()]
    a_file = a_file.replace('\r|\n', '', regex=True)
    a_file.columns = pd.Series(a_file.columns.to_list()).replace('\r|\n', '', regex=True)
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    a_file_cols = ["product_id","product_type","product_name","size","thickness","Count_num"]
    a_file = a_file[a_file_cols]
    # a_file.columns = a_file_cols
    a_file["size"]=[gg.split("x")[0].strip()+" x "+gg.split("x")[1].strip() if "x" in gg else " ".join(gg.strip().split()) for gg in a_file["size"]]
    a_file["thickness"][a_file["thickness"].isnull()]=""
    a_file["thickness"]=[" ".join(gg.strip().split()) for gg in a_file["thickness"]]
    a_file["Count_num"] = a_file["Count_num"].astype(int)
    a_file["product_id"] = a_file["product_id"].astype(int)
    if sum([kl in a_file.columns for kl in a_file_cols])==6:
        a_file.to_sql("PlywoodCountTable", conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()
        return jsonify({"status":"success"})
    else:
        conn.close()
        return jsonify({"status": "unmatched columns"})

@app.route("/api/loaduserscsv", methods=["POST"])#to view all data from
def loaduserscsv():
    req_data = request.get_json()
    a_file = pd.DataFrame(req_data["uploads"])
    a_file = a_file[~ a_file["credit_id"].isnull()]
    a_file = a_file.replace('\r|\n', '', regex=True)
    a_file.columns = pd.Series(a_file.columns.to_list()).replace('\r|\n', '', regex=True)
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    a_file_cols = ["credit_id","name","mobileno","total_credit"]
    a_file["mobileno"][a_file["mobileno"].isnull()]=""
    a_file["credit_id"] = a_file["credit_id"].astype(int)
    a_file["total_credit"] = a_file["total_credit"].astype(int)
    if sum([kl in a_file.columns for kl in a_file_cols])==4:
        a_file.to_sql("PlywoodCreditTable", conn, if_exists="replace", index=False)
        conn.commit()
        conn.close()
        return jsonify({"status":"success"})
    else:
        conn.close()
        return jsonify({"status": "unmatched columns"})

@app.route("/api/downloaduserscsv", methods=["GET"])#to view all data from
def downloaduserscsv():
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute("select * FROM PlywoodCreditTable")
    row = cursor.fetchall()
    countdf = pd.DataFrame(row)
    countdf.columns = ["credit_id", "name", "mobileno", "total_credit"]
    countdf = countdf.to_json(orient="records")
    conn.close()
    return jsonify({"status":"success","data":json.loads(countdf)})

@app.route("/api/downloadproductscsv", methods=["GET"])#to view all data from
def downloadproductscsv():
    conn = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = conn.cursor()
    cursor.execute("select * FROM PlywoodCountTable")
    row = cursor.fetchall()
    countdf = pd.DataFrame(row)
    countdf.columns = ["product_id","product_type","product_name","size","thickness","Count_num"]
    countdf = countdf[["product_id","product_type","thickness","product_name","size","Count_num"]]
    countdf["size_val"] = list(countdf["size"].map(size_cal))
    countdf["thickness_val"] = list(countdf["thickness"].map(thickness_cal))
    countdf.sort_values(by=['product_type', 'product_name', "thickness_val", "size_val"],
                        ascending=[False, True, True, False], inplace=True)
    countdf.drop(["size_val", "thickness_val"], axis=1, inplace=True)
    countdf = countdf.to_json(orient="records")
    conn.close()
    return jsonify({"status":"success","data":json.loads(countdf)})


@app.route("/api/getTransactions", methods=["POST"])  # to view all data from
def getTransactions():
    # req_data={"mobile_number":"","order_date":"","name":"","pageCounter":1,"username":"Dinesh","role":"admin"}
    req_data = request.get_json()
    name = req_data["name"]
    mobileno = req_data["mobile_number"]
    order_date_from = req_data["order_date_from"]
    order_date_to = req_data["order_date_to"]
    # if order_date_from != "":
    #     dto = datetime.strptime(order_date_from, "%Y-%m-%d")
    #     order_date_from = dto.strftime("%d/%m/%Y")
    #
    # if order_date_to != "":
    #     dto = datetime.strptime(order_date_to, "%Y-%m-%d")
    #     order_date_to = dto.strftime("%d/%m/%Y")

    con = sqlite3.connect(project_path + '/static/database/atc_main_table.db')
    cursor = con.cursor()
    if name == "" and mobileno == "" and order_date_from == "" and order_date_to == "":
        cursor.execute('''select * from OrdersTable''')
        rows = cursor.fetchall()
        countdf = pd.DataFrame(rows)
        countdf.columns = ["order_id", "user_name", "mobile_number", "order_date", "order_items_count", "total_amount",
                           "discount_amount", "paid_amount"]
        cursor.execute('''select * from Orderitems''')
        rows = cursor.fetchall()
        items = pd.DataFrame(rows)
        items.columns = ["order_id", "product_type", "product_name", "size", "thickness", "count", "amount"]
        total_df = pd.merge(countdf,items,how = "left", on = "order_id")
        total_df = total_df[["order_id", "user_name", "mobile_number", "order_date"
                           ,"product_type", "product_name", "size", "thickness", "count", "amount","discount_amount", "paid_amount"]]
        total_df = total_df.to_json(orient="records")
        return jsonify({"status": "success", "data": json.loads(total_df)})
    else:
        struc = {"name": name, "mobileno": mobileno, "order_date_from": order_date_from, "order_date_to": order_date_to}
        non_null_values = []
        for a, b in struc.items():
            if b != "":
                if a == "order_date_from":
                    non_null_values.append('order_date >= "{}"'.format(b))
                elif a == "order_date_to":
                    non_null_values.append('order_date <= "{}"'.format(b))
                else:
                    non_null_values.append('{} like "%{}%"'.format(a, b))
        qry = " where " + " and ".join(non_null_values)
        # print('''select * from OrdersTable {} '''.format(qry))
        cursor.execute('''select * from OrdersTable {} '''.format(qry))
        rows = cursor.fetchall()

        if len(rows) != 0:
            countdf = pd.DataFrame(rows)
            countdf.columns = ["order_id", "user_name", "mobile_number", "order_date", "order_items_count",
                               "total_amount", "discount_amount", "paid_amount"]
            cursor.execute('''select * from Orderitems''')
            rows = cursor.fetchall()
            items = pd.DataFrame(rows)
            items.columns = ["order_id", "product_type", "product_name", "size", "thickness", "count", "amount"]
            total_df = pd.merge(countdf, items, how="left", on="order_id")
            total_df = total_df[["order_id", "user_name", "mobile_number", "order_date"
                , "product_type", "product_name", "size", "thickness", "count", "amount", "discount_amount",
                                 "paid_amount"]]
            total_df = total_df.to_json(orient="records")
            con.close()
            return jsonify({"status": "success", "data": json.loads(total_df)})
        else:
            return jsonify({"status": "failure", "data": "no records found"})

@app.route("/api/combinedproducts", methods=["POST"])  # to view all data from
def combinedproducts():
    con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
    cursor = con.cursor()
    cursor.execute("select * FROM PlywoodCountTable")
    row = cursor.fetchall()
    countdf = pd.DataFrame(row)
    countdf.columns = ["product_id", "product_type", "product_name", "size", "thickness", "Count_num"]
    countdf.drop(["product_id", "Count_num"], axis=1, inplace=True)
    countdf_gum = countdf[countdf["product_type"]=="Gum"]
    countdf_gum.drop(["thickness"], axis=1, inplace=True)
    countdf_gum = countdf_gum.astype(str).agg('__'.join, axis=1)
    countdf_plywood = countdf[countdf["product_type"] == "Plywood"]
    countdf_plywood = countdf_plywood[["product_type","thickness","product_name","size"]]
    countdf_plywood = countdf_plywood.astype(str).agg('__'.join, axis=1)
    count_final = pd.concat([countdf_plywood,countdf_gum])
    count_final = count_final.to_json(orient="records")
    con.close()
    return jsonify({"status": "success", "data": json.loads(count_final)})

@app.route("/api/edittransaction", methods=["POST"])
def edittransaction():
    req_data = request.get_json()
    old_data = req_data["oldData"]
    new_data = req_data["newData"]
    if old_data["user_data"]["name"] == new_data["user_data"]["name"]:
        order_id = req_data["order_id"]
        return_url = "http://"+app_host+"/api/returnOrder" #for deployment remove :8000
        r = requests.post(return_url, json=old_data)
        old_values = r.json()
        new_data["user_data"]["credit"] = old_values["credit"]
        submit_url = "http://"+app_host+"/api/submitOrder" #for deployment remove :8000
        r = requests.post(submit_url, json=new_data)
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute('''DELETE FROM OrdersTable where order_id="{}"'''.format(old_values["order_id"]))
        cursor.execute('''DELETE FROM OrdersTable where order_id="{}"'''.format(order_id))
        con.commit()
        con.close()
        return jsonify({"status": "success"})
    else:
        return jsonify({"status": "failure", "message": "as the customer names changed"})


@app.route("/api/chequetable", methods=["GET"])
def chequetable():
    con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
    cursor = con.cursor()
    cursor.execute("select * FROM ChequeTable")
    row = cursor.fetchall()
    chequedf = pd.DataFrame(row)
    chequedf.columns = ["cheque_id", "name", "mobileno", "order_date", "passing_date", "amount", "validated"]
    # chequedf = chequedf[chequedf["validated"]=="No"]
    chequedf = chequedf.to_json(orient="records")
    con.close()
    return jsonify({"status": "success", "data": json.loads(chequedf)})

@app.route("/api/chequevalidation", methods=["POST"])
def chequevalidation():
    # req_data={"cheque_id":1,"mobileno":"","name":"test","amount":200,"charges":15,"mode":"passed","username":"Dinesh","role":"admin"}
    req_data = request.get_json()
    cheque_id = req_data["cheque_id"]
    name = req_data["name"]
    mobileno = req_data["mobileno"]
    mode = req_data["mode"]
    amount = req_data["amount"]
    charges = req_data["charges"]

    if mode == "passed":
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute(
            '''update ChequeTable set validated ="Yes" where Cheque_id="{}"'''.format(
                cheque_id))
        con.commit()
        con.close()
    elif mode =="rejected":
        total_amount = 0
        after_discount_amount=0
        paid_amount = amount+charges
        con = sqlite3.connect(project_path + "/static/database/atc_main_table.db")
        cursor = con.cursor()
        cursor.execute("select * FROM PlywoodCreditTable where name ='{}' ".format(name))
        rows = cursor.fetchall()
        old_credit = rows[0][-1]
        credit = old_credit + paid_amount
        cursor.execute('''update PlywoodCreditTable set total_credit =? where name=? and mobileno=?''',
                       (credit, name, mobileno))

        notes = ""
        order_date = date.today()
        # order_date = datetime.strptime(order_date, "%Y-%m-%d")  # order_date.strftime("%d/%m/%Y")
        order_date = order_date.strftime("%Y-%m-%d")
        order_items = 1
        cursor.execute('''INSERT INTO OrdersTable(name, mobileno, order_date, order_items,total_amount,after_discount_amount,paid_amount,running_total,notes) VALUES 
                    ('{}','{}','{}','{}','{}','{}','{}','{}','{}')'''.format(name, mobileno, order_date, order_items,
                                                                             total_amount,
                                                                             after_discount_amount, -paid_amount, credit,
                                                                             notes))
        con.commit()

        cursor.execute('''select order_id from OrdersTable where name=="{}" and mobileno=="{}" and order_date=="{}" and order_items=="{}" and total_amount=="{}" and after_discount_amount=="{}" and paid_amount=="{}" and running_total=="{}"  and notes=="{}"
                    '''.format(name, mobileno, order_date, order_items, total_amount, after_discount_amount,
                               -paid_amount, credit, notes))
        rows1 = cursor.fetchall()
        order_id = rows1[0][0]
        cursor.execute('''INSERT INTO Orderitems(order_id, product_type, product_name, size,thickness,count,amount) VALUES 
                        ('{}','{}','{}','{}','{}','{}','{}')'''.format(order_id, "cheque bounce", "cheque bounce", "", "",
                                                                       "1",
                                                                       credit))
        cursor.execute(
            '''update ChequeTable set validated ="Bounced" where Cheque_id="{}"'''.format(
                cheque_id))
        con.commit()

    return jsonify({"status": "success","data":mode})

if __name__ == "__main__":
    app_host = "0.0.0.0" # for deployment change here to 0.0.0.0
    app.run(host = app_host,port=8000)
