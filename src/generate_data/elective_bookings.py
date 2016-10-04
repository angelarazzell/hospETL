import random
import time
import csv
import sys
import math
from datetime import datetime, timedelta
from dateutil.parser import parse

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

provider_codes = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','G19','G20','G21','G22','G23','G24','G25','G26','G27','G28','G29','G30','G31','G32','G33','G34','G35','G36','G37','G38','G39','G40','G41','G42','G43','G44','G45','G46','G47','D48','D49','D50','D51','D52','D53','G54','G55','G56','G57','G58','G59','G60','G61','G62','G63','G64','G65','G66','G67','G68','G69','G70','G71','G72','G73','G74','G75','G76','G77','G78','G79','G80','G81','G82','G83','G84','G85','G86','G87','G88','G89','G90','G91','G92','G93','G94','G95','G96','G97','G98','G99','G100','G101']
spec_list = [100,101,102,103,104,105,106,107,108,110,120,130,140,141,142,143,144,150,160,161,170,171,172,173,174,180,191,211,212,213,214,215,216,217,218,219,220,221,222,223,241,242,251,252,253,254,255,256,257,258,259,260,261,262,263,264,280,290,291,190,192,300,301,302,303,304,305,306,307,308,309,310,311,313,314,315,316,317,318,319,320,321,322,323,324,325,327,328,329,330,331,340,341,342,343,344,345,346,350,352,360,361,370,371,400,401,410,420,421,422,424,430,450,460,501,502,503,560,650,651,652,653,654,655,656,657,658,659,660,661,662,663,700,710,711,712,713,715,720,721,722,723,724,725,726,727,800,811,812,822,834,840,920]

#OP create
with open('./historic_data/elective_bookings/OP_create.csv','w') as fout:
    outputWriter = csv.writer(fout)
    booking_type = 'OP'
    booking_stage = 'Created'
    intended_management = ''
    for i in range(20000000):
        booking_no = 'OPN' + '%s' % (i+1)
        pathway_id = 'P' + '%s' % (i+1)
        medicalid = random.randint(1,10000000)
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
print("completed outpatient create")

#OP modify
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
print("completed daycase create")

#IP create
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
print("completed daycase modify")

#IP modify
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
print("completed inpatient modify")
        
        
        