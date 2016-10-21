#Connect to Redshift cluster to output data for Reporting Flask App
from flask import render_template, request, jsonify
from app import app

import json
#import demjson
import psycopg2
from getpass import getpass
from pandas import read_sql

pwd = getpass('password')

with open('./app/config.yml','r') as fin:
 for line in fin:
  config = json.loads(fin)
config['password'] += pwd

def create_conn(*args,**kwargs):
 config = kwargs['config']
  try:
   con=psycopg2.connect(dbname=config['dbname'], host=config['host'],
                              port=config['port'], user=config['user'],
                              password=config['password'])
   return con
  except Exception as err:
   print(err)

@app.route('/')
@app.route('/index')
def homepage():
 return render_template("homepage.html")

@app.route('/sparkline/<booking_type>')
def sparkline(booking_type):
 con = create_conn(config=config)
 df = read_sql(('select * from rep.vw_sparkline '
                   'where booking_type = %(btype)s '
                   'order by hospital_desc'),
                   params={"btype":booking_type},
                     index_col=['booking_type'], con=con)
 response_list = []
 jsonresponse = []
 for val in df.values:
  response_list.append(val)
 jsonresponse = [{"hospital_name": str(x[0]),
        "q1": str(x[1]),
        "q2":  str(x[2]),
        "q3":  str(x[3]),
        "q4":  str(x[4]),
        "Q4Q1": str(x[5]),
        "Q1Q2":  str(x[6]),
        "Q2Q3":  str(x[7]),
        "Q3Q4":  str(x[8])} for x in response_list]
 return render_template("sparkbase.html",output = jsonresponse)

@app.route('/emergency')
def mytest():
 con = create_conn(config=config)
 dataframe = read_sql("select * from rep.vw_EmergencyCount", con=con)
 response_list = []
 jsonresponse = []
 for i, val in enumerate(dataframe.values):
  response_list.append(val)
 jsonresponse = [{"hospital_name": str(x[2]),
        "non_breach": str(x[1]),
        "breach":  str(x[0])} for x in response_list]
 return render_template("mybase.html",output = jsonresponse)

@app.route("/frequentflyers")
def frequent_flyers():
 con = create_conn(config=config)
 df = read_sql("select * from report_frequent", con=con)
 response_list = []
 jsonresponse = []
 for i, val in enumerate(df.values):
  response_list.append(val)
 jsonresponse = [{"medicalid": str(x[0]),
        "firstname": str(x[1]),
        "lastname": str(x[2]),
        "hospital1": str(x[3]),
        "arrivaldate1": str(x[4]),
        "complaint1": str(x[5]),
        "hospital2": str(x[6]),
        "arrivaldate2": str(x[7]),
        "complaint2": str(x[8]),
        "hospital3": str(x[9]),
        "arrivaldate3": str(x[10]),
        "complaint3": str(x[11]),
        "hospital4": str(x[12]),
        "arrivaldate4": str(x[13]),
        "complaint4": str(x[14])} for x in response_list]
 return render_template("base.html", output = jsonresponse)
