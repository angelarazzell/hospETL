import random
import boto3
import csv
from datetime import datetime, timedelta
from dateutil.parser import parse

s3 = boto3.resource('s3')

with open('./historic_data/check_ins/ipdc_checkin.csv','r') as fin,\
    open('./historic_data/check_outs/ipdc_checkouts.csv','w') as fout:
    count = 0
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    for line in reader: 
        if line[5] == 'Daycase':
            encounterno = line[0]
            pathway_id = line[1]
            medicalid = line[2]
            dead_on_discharge = round(random.randint(0,51)/100)
            discharge_date = parse(line[9])+timedelta(minutes=round(random.weibullvariate(300, 1.5)))
            outcome = random.choice(['Discharged','FollowUp'])
            checkout_list = [encounterno, pathway_id, medicalid, dead_on_discharge,discharge_date,outcome]
        else:
            encounterno = line[0]
            pathway_id = line[1]
            medicalid = line[2]
            dead_on_discharge = round(random.randint(0,54)/100)
            discharge_date = parse(line[9])+timedelta(days=round(random.weibullvariate(3, 1.5)))
            outcome = random.choice(['Discharged','FollowUp'])
            checkout_list = [encounterno, pathway_id, medicalid, dead_on_discharge,discharge_date,outcome]
            outputWriter.writerow(checkout_list)
            
# Upload file to S3
s3.meta.client.upload_file('./historic_data/check_outs/ipdc_checkouts.csv', 'angela-hospital-data', 'historic_data/'+'ipdc_checkouts.csv')

with open('./historic_data/check_ins/OP_checkin.csv','r') as fin,\
    open('./historic_data/check_outs/op_checkouts.csv','w') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    for line in reader: 
        encounterno = line[0]
        pathway_id = line[1]
        medicalid = line[2]
        dead_on_discharge = 0
        discharge_date = parse(line[9])+timedelta(minutes=round(random.weibullvariate(40, 1.5)))
        outcome = random.choice(['Discharged','FollowUp'])
        checkout_list = [encounterno, pathway_id, medicalid, dead_on_discharge,discharge_date,outcome]
        outputWriter.writerow(checkout_list)

# Upload file to S3
s3.meta.client.upload_file('./historic_data/check_outs/op_checkouts.csv', 'angela-hospital-data', 'historic_data/'+'op_checkouts.csv')


