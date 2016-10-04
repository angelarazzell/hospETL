import json
import sys
import random
import time
import csv
from datetime import datetime, timedelta
from dateutil.parser import parse
from faker import Factory

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

def encounter_data(fake):
    """create fake encounter data for historic emergency admissions and write to csv file"""
    outputFile = open('./historic_data/encounters/encounter_data.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    disposal_codes = [1]*9
    disposal_codes.extend([2]*12)
    disposal_codes.extend([3]*26)
    disposal_codes.extend([4,5,6,7,10,11,12,13,14])
    provider_codes = ['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C11','C12','C13','C14','C15','C16','C17','C18','G19','G20','G21','G22','G23','G24','G25','G26','G27','G28','G29','G30','G31','G32','G33','G34','G35','G36','G37','G38','G39','G40','G41','G42','G43','G44','G45','G46','G47','D48','D49','D50','D51','D52','D53','G54','G55','G56','G57','G58','G59','G60','G61','G62','G63','G64','G65','G66','G67','G68','G69','G70','G71','G72','G73','G74','G75','G76','G77','G78','G79','G80','G81','G82','G83','G84','G85','G86','G87','G88','G89','G90','G91','G92','G93','G94','G95','G96','G97','G98','G99','G100','G101']
    
    for i in range(100):
        
        medical_id = random.randint(1,10000000)
        encounter_id = i + 20000001
        
        arrival_date = parse(randomDate("1/1/2000 1:30 PM", "9/19/2016 11:59 PM", random.random()))
        seen_date = (arrival_date) + timedelta(minutes= random.randrange(500))
        leave_date = (seen_date) + timedelta(minutes= random.randrange(600))
        
        #arrival_date = str(arrival_date)
        #seen_date = str(seen_date)
        #leave_date = str(leave_date)
        
        randno = random.randint(1,20)
        hospital_id = 'H' + '%s' % randno
        doctor_id = provider_codes[randno * 5]
        reason_code = random.randrange(39)
        
        discharge_code = random.choice(disposal_codes) 
        if discharge_code == 1:
            admitted_flag = 1
        else:
            admitted_flag = 0

        encounter_list = [medical_id, encounter_id, arrival_date, seen_date, leave_date, hospital_id, doctor_id, admitted_flag, reason_code, discharge_code]
        outputWriter.writerow(encounter_list)
    outputFile.close()
 
if __name__ == "__main__":
    start_time = datetime.now()
    fake = Factory.create()
    encounter_data(fake)
    print ('total_time: ' + str(datetime.now() - start_time))