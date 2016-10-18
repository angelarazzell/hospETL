# Generate check in data for inpatients and daycases
# (read adn create from the inpatients/daycases bookings files), 
# upload to storage in Amazon S3 buckets

import random
import time
import boto3
import csv
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

with open('./historic_data/elective_bookings/DC_create.csv','r') as fin, \
     open('./historic_data/check_ins/ipdc_checkin.csv','w') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    count = 0
    for line in reader:        
        count += 1    
        if parse(line[8]) >= datetime.now():
            continue
        elif round(random.randint(0,51)/100) == 0:
            encounterno = 'DC' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([5,6])
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = (appt_date - timedelta(minutes = 65)) + timedelta(minutes = random.gauss(65, 15))
            expected_discharge =  line[10]
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)
        else:
            encounterno = 'DC' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([2,3,4,7])
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            if attend_code == 7:
                arrival_datetime = appt_date + timedelta(minutes = random.gauss(15, 10)) 	
            else: 
            	arrival_datetime = ''
            expected_discharge = ''
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \ 
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)

with open('./historic_data/elective_bookings/DC_modify.csv','r') as fin, \
     open('./historic_data/check_ins/ipdc_checkin.csv','a') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    count = 0
    for line in reader:        
        count += 1    
        if parse(line[8]) >= datetime.now():
            continue
        elif round(random.randint(0,51)/100) == 0:
            encounterno = 'DC' + '%s' % (count) + 'M' 
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([5,6])
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = (appt_date - timedelta(minutes = 65)) + timedelta(minutes = random.gauss(65, 15))
            expected_discharge =  line[10]
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \ 
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)
        else:
            encounterno = 'DC' + '%s' % (count) + 'M'
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([2,3,4,7])
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            if attend_code == 7:
                arrival_datetime = appt_date + timedelta(minutes = random.gauss(15, 10)) 	
            else: 
            	arrival_datetime = ''
            expected_discharge = ''
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)
        
#inpatient stays:
with open('./historic_data/elective_bookings/IP_create.csv','r') as fin, \
     open('./historic_data/check_ins/ipdc_checkin.csv','a') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    count = 0
    for line in reader:        
        count += 1    
        if parse(line[8]) >= datetime.now():
            continue
        elif round(random.randint(0,51)/100) == 0:
            encounterno = 'IP' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([5,6])
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = (appt_date - timedelta(minutes = 65)) + timedelta(minutes = random.gauss(65, 15))
            expected_discharge =  line[10]
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)
        else:
            encounterno = 'IP' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([2,3,4,7]) #did not attend appt
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            if attend_code == 7:
                arrival_datetime = appt_date + timedelta(minutes = random.gauss(15, 10)) 	
            else: 
            	arrival_datetime = ''
            expected_discharge = ''
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)

with open('./historic_data/elective_bookings/IP_modify.csv','r') as fin, \
     open('./historic_data/check_ins/ipdc_checkin.csv','a') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    count = 0
    for line in reader:        
        count += 1    
        if parse(line[8]) >= datetime.now():
            continue
        elif round(random.randint(0,51)/100) == 0:
            encounterno = 'IP' + '%s' % (count) + 'M' 
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([5,6])
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = (appt_date - timedelta(minutes = 65)) + timedelta(minutes = random.gauss(65, 15))
            expected_discharge =  line[10]
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)
        else:
            encounterno = 'DC' + '%s' % (count) + 'M' 
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = random.randint(11,13)
            attend_code = random.choice([2,3,4,7])
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            if attend_code == 7:
                arrival_datetime = appt_date + timedelta(minutes = random.gauss(15, 10)) 	
            else: 
            	arrival_datetime = ''
            expected_discharge = ''
            specialty = line[11]
            checkin_list = [encounterno, pathway_id, medicalid, adm_method, \
                attend_code, intended_management, hospital_id, ward, doctor_id, \
                appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(checkin_list)
            
s3.meta.client.upload_file('./historic_data/check_outs/ipdc_checkin.csv', 'angela-hospital-data', 'historic_data/'+'ipdc_checkin.csv')
