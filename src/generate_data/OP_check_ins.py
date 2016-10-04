import random
import time
import csv
from datetime import datetime, timedelta
from dateutil.parser import parse

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

with open('./historic_data/elective_bookings/OP_created_sat.csv','r') as fin, \
     open('./historic_data/check_ins/OP_checkin_sat.csv','w') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    count = 0
    for line in reader:        
        count += 1    
        if parse(line[8]) >= datetime.now():
            encounterno = 'OPE' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            #adm_method = random.randint(11,13)
            adm_method = ''
            attend_code = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,2])
            #randno = random.randrange(1,20,2)
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = ''
            expected_discharge =  line[10]
            specialty = line[11]
            booking_list = [encounterno, pathway_id, medicalid, adm_method, attend_code, intended_management, hospital_id, ward, doctor_id, appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(booking_list)
        elif round(random.randint(0,51)/100) == 0:
            encounterno = 'OPE' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = ''
            attend_code = random.choice([5,6])
            #randno = random.randrange(1,20,2)
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = (appt_date - timedelta(minutes = 65)) + timedelta(random.gauss(65, 15))
            expected_discharge =  line[10]
            specialty = line[11]
            booking_list = [encounterno, pathway_id, medicalid, adm_method, attend_code, intended_management, hospital_id, ward, doctor_id, appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(booking_list)
        else:
            encounterno = 'OPE' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = ''
            attend_code = random.choice([2,3,4,7])
            #randno = random.randrange(1,20,2)
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            if attend_code == 7:
                arrival_datetime = appt_date + timedelta(random.gauss(15, 10)) 	
            else: 
            	arrival_datetime = ''
            expected_discharge = ''
            specialty = line[11]
            booking_list = [encounterno, pathway_id, medicalid, adm_method, attend_code, intended_management, hospital_id, ward, doctor_id, appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(booking_list)
#        if count == 100:
#            break

with open('./historic_data/elective_bookings/OP_modify_sat.csv','r') as fin, \
     open('./historic_data/check_ins/OP_checkin_sat.csv','a') as fout:
    reader = csv.reader(fin, delimiter=',')
    outputWriter = csv.writer(fout)
    count = 0
    for line in reader:        
        count += 1    
        if parse(line[8]) >= datetime.now():
            encounterno = 'OPEM' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            #adm_method = random.randint(11,13)
            adm_method = ''
            attend_code = random.choice([0,0,0,0,0,0,0,0,0,0,0,0,2])
            #randno = random.randrange(1,20,2)
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = ''
            expected_discharge =  line[10]
            specialty = line[11]
            booking_list = [encounterno, pathway_id, medicalid, adm_method, attend_code, intended_management, hospital_id, ward, doctor_id, appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(booking_list)
        elif round(random.randint(0,51)/100) == 0:
            encounterno = 'OPEM' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = ''
            attend_code = random.choice([5,6])
            #randno = random.randrange(1,20,2)
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            arrival_datetime = (appt_date - timedelta(minutes = 65)) + timedelta(random.gauss(65, 15))
            expected_discharge =  line[10]
            specialty = line[11]
            booking_list = [encounterno, pathway_id, medicalid, adm_method, attend_code, intended_management, hospital_id, ward, doctor_id, appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(booking_list)
        else:
            encounterno = 'OPEM' + '%s' % (count)
            pathway_id = line[1]
            medicalid = line[2]
            adm_method = ''
            attend_code = random.choice([2,3,4,7])
            #randno = random.randrange(1,20,2)
            intended_management = line[5]
            hospital_id = line[6]
            doctor_id = line[7]
            randno2 = random.randint(1,20)
            ward = hospital_id + '%s' % randno2
            appt_date = parse(line[8])
            if attend_code == 7:
                arrival_datetime = appt_date + timedelta(random.gauss(15, 10)) 	
            else: 
            	arrival_datetime = ''
            expected_discharge = ''
            specialty = line[11]
            booking_list = [encounterno, pathway_id, medicalid, adm_method, attend_code, intended_management, hospital_id, ward, doctor_id, appt_date, arrival_datetime, expected_discharge, specialty]
            outputWriter.writerow(booking_list)
#        if count == 15:
#            break
        
