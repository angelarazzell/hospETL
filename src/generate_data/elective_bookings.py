# Generate bookings data (create or modify)
# for inpatients, outpatients and daycases
# upload to storage in Amazon S3 buckets

import random
import time
import csv
import boto3
import sys
import math
from datetime import datetime, timedelta
from dateutil.parser import parse

s3 = boto3.resource('s3')

#strTimeProp() and randomDate() functions are from the following stack overflow forum:
#http://stackoverflow.com/questions/4874764/problem-with-format-datetime-in-python
def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))

def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

ref_file = open('./reference_data/doctor_lookup.txt', 'r')
reader = csv.reader(ref_file)
provider_codes = []
for line in reader:
    provider_codes.append(line[0])
ref_file.close()

ref_file = open('./reference_data/specialty_lookup.txt', 'r')
reader = csv.reader(ref_file)
spec_list = []
for line in reader:
    spec_list.append(line[0])
ref_file.close()

#Outpatient create
with open('./historic_data/elective_bookings/OP_create.csv','w') as fout:
    outputWriter = csv.writer(fout)
    booking_type = 'OP'
    booking_stage = 'Created'
    intended_management = ''
    for i in range(20000000):
        booking_no = 'OPN' + '%s' % (i+1)
        pathway_id = 'P' + '%s' % (i+1)
        medicalid = random.randint(1,10000000) #choose a random patient ID
        randno = random.randrange(1,20,2)
        hospital_id = 'H' + '%s' % randno
        doctor_id = provider_codes[randno * 5]
        appt_date = parse(randomDate("1/1/2000 1:30 PM", "4/20/2017 11:59 PM", random.random()))
        modify_date = appt_date - timedelta(days = round(random.weibullvariate(45, 2)))
        expected_discharge = appt_date
        specialty = random.choice(spec_list)
        priority = random.choice(['R','R','R','U'])
        booking_list = [booking_no, pathway_id, medicalid, booking_type, booking_stage, intended_management, hospital_id, doctor_id, appt_date, modify_date, expected_discharge, specialty,priority]
        outputWriter.writerow(booking_list)

s3.meta.client.upload_file('./historic_data/elective_bookings/OP_create.csv', 'angela-hospital-data', 'historic_data/'+'OP_create.csv')
print("completed outpatient create")    

#Outpatient modify
with open('./historic_data/elective_bookings/OP_create.csv','r') as fin, \
     open('./historic_data/elective_bookings/OP_modify.csv','w') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    booking_stage = 'Modify'
    booking_type = 'OP'
    intended_management = ''
    count = 0
    for line in reader:
        count += 1
        if round(random.randint(0,75)/100) == 0:
            continue
        booking_no = 'OPM' + '%s' % (count)
        pathway_id = line[1]
        medicalid = line[2]
        hospital_id = line[6]
        doctor_id = line[7]
        appt_date = parse(line[8]) + timedelta(days = round(random.weibullvariate(65, 1.5)))
        tdelta = parse(line[8])-parse(line[9])
        modify_date = parse(line[9]) + timedelta(days = random.randrange(0,max(int(tdelta.days),1)))
        expected_discharge = appt_date
        specialty = line[11]
        priority = line[12]
        booking_list = [booking_no, pathway_id, medicalid, booking_type, booking_stage, intended_management, hospital_id, doctor_id, appt_date, modify_date, expected_discharge, specialty,priority]
        outputWriter.writerow(booking_list)

s3.meta.client.upload_file('./historic_data/elective_bookings/OP_modify.csv', 'angela-hospital-data', 'historic_data/'+'OP_modify.csv')
print("completed outpatient modify")

#Daycase create
with open('./historic_data/elective_bookings/DC_create.csv','w') as fout:
    outputWriter = csv.writer(fout)
    booking_stage = 'Created'
    booking_type = 'IP'
    intended_management = 'Daycase'
    for i in range(11000000):
        booking_no = 'IPC'  + '%s' % (i+1)
        pathway_id = 'P' + '%s' % (i+20000001)
        medicalid = random.randint(1,10000000)
        randno = random.randrange(1,20,2)
        hospital_id = 'H' + '%s' % randno
        doctor_id = provider_codes[randno * 5]
        appt_date = parse(randomDate("1/1/2000 1:30 PM", "4/20/2017 11:59 PM", random.random()))
        modify_date = appt_date - timedelta(days = round(random.weibullvariate(45, 2)))
        expected_discharge = appt_date + timedelta( hours = random.randrange(0,8))
        specialty = random.choice(spec_list)
        priority = random.choice(['R','R','R','U'])
        booking_list = [booking_no, pathway_id, medicalid, booking_type, booking_stage, intended_management, hospital_id, doctor_id, appt_date, modify_date, expected_discharge, specialty,priority]
        outputWriter.writerow(booking_list)
        
s3.meta.client.upload_file('./historic_data/elective_bookings/DC_create.csv', 'angela-hospital-data', 'historic_data/'+'DC_create.csv')
print("completed daycase create")

#Inpatient create
with open('./historic_data/elective_bookings/IP_create.csv','w') as fout:
    outputWriter = csv.writer(fout)
    booking_stage = 'Created'
    booking_type = 'IP'
    intended_management = 'Inpatient'
    for i in range(9000000):
        booking_no = 'APCC'  + '%s' % (i+1)
        pathway_id = 'P' + '%s' % (i+31000001)
        medicalid = random.randint(1,10000000)
        randno = random.randrange(1,20,2)
        hospital_id = 'H' + '%s' % randno
        doctor_id = provider_codes[randno * 5]
        appt_date = parse(randomDate("1/1/2000 1:30 PM", "4/20/2017 11:59 PM", random.random()))
        modify_date = appt_date - timedelta(days = round(random.weibullvariate(45, 2)))
        expected_discharge = appt_date + timedelta(days = math.ceil(random.weibullvariate(10, 1.5)))
        specialty = random.choice(spec_list)
        priority = random.choice(['R','R','R','U'])
        booking_list = [booking_no, pathway_id, medicalid, booking_type, booking_stage, intended_management, hospital_id, doctor_id, appt_date, modify_date, expected_discharge, specialty,priority]
        outputWriter.writerow(booking_list)
        
s3.meta.client.upload_file('./historic_data/elective_bookings/IP_create.csv', 'angela-hospital-data', 'historic_data/'+'IP_create.csv')
print("completed inpatient create")

#Daycase modify
with open('./historic_data/elective_bookings/DC_create.csv','r') as fin,\
      open('./historic_data/elective_bookings/DC_modify.csv','w') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    booking_stage = 'Modify'
    booking_type = 'IP'
    intended_management = 'Daycase'
    count = 0
    for line in reader:
        if round(random.randint(0,75)/100) == 0:
            continue
        count += 1
        booking_no = 'DCM' + '%s' % (count)
        pathway_id = line[1]
        medicalid = line[2]
        hospital_id = line[6]
        doctor_id = line[7]
        appt_date = parse(line[8]) + timedelta(days = round(random.weibullvariate(65, 1.5)))
        tdelta = parse(line[8])-parse(line[9])
        modify_date = parse(line[9]) + timedelta(days = random.randrange(0,max(int(tdelta.days),1)))
        expected_discharge = appt_date + timedelta( hours = random.randrange(0,8))
        specialty = line[11]
        priority = line[12]
        booking_list = [booking_no, pathway_id, medicalid, booking_type, booking_stage, intended_management, hospital_id, doctor_id, appt_date, modify_date, expected_discharge, specialty,priority]
        outputWriter.writerow(booking_list)
        
s3.meta.client.upload_file('./historic_data/elective_bookings/DC_modify.csv', 'angela-hospital-data', 'historic_data/'+'DC_modify.csv')
print("completed daycase modify")

#Inpatient modify
with open('./historic_data/elective_bookings/IP_create.csv','r') as fin,\
      open('./historic_data/elective_bookings/IP_modify.csv','w') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    booking_stage = 'Modify'
    booking_type = 'IP'
    intended_management = 'Inpatient'
    count = 0
    for line in reader:
        if round(random.randint(0,75)/100) == 0:
            continue
        count += 1
        booking_no = 'APCM' + '%s' % (count)
        pathway_id = line[1]
        medicalid = line[2]
        hospital_id = line[6]
        doctor_id = line[7]
        appt_date = parse(line[8]) + timedelta(days = round(random.weibullvariate(65, 1.5)))
        tdelta = parse(line[8])-parse(line[9])
        modify_date = parse(line[9]) + timedelta(days = random.randrange(0,max(int(tdelta.days),1)))
        expected_discharge = appt_date +  timedelta(days = math.ceil(random.weibullvariate(10, 1.5)))
        specialty = line[11]
        priority = line[12]
        booking_list = [booking_no, pathway_id, medicalid, booking_type, booking_stage, intended_management, hospital_id, doctor_id, appt_date, modify_date, expected_discharge, specialty,priority]
        outputWriter.writerow(booking_list)
        
s3.meta.client.upload_file('./historic_data/elective_bookings/IP_modify.csv', 'angela-hospital-data', 'historic_data/'+'IP_modify.csv')
print("completed inpatient modify")
        
        
        