# Generate data for emergency encounters
# Upload to storage in Amazon S3 buckets

import json
import sys
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

def encounterData():
    """create fake encounter data for historic emergency admissions and write to csv file"""
    outputFile = open('./historic_data/encounters/encounter_data.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    ref_file = open('./reference_data/doctor_lookup.txt', 'r')
    reader = csv.reader(ref_file)
    provider_codes = []
    for line in reader:
    	provider_codes.append(line[0])
    disposal_codes = [1]*9
    disposal_codes.extend([2]*12)
    disposal_codes.extend([3]*26)
    disposal_codes.extend([4,5,6,7,10,11,12,13,14])
        
    for i in range(20000000):
        
        medical_id = random.randint(1,10000000)
        encounter_id = i #+ 20000001
        
        arrival_date = parse(randomDate("1/1/2000 1:30 PM", "9/19/2016 11:59 PM", random.random()))
        seen_date = (arrival_date) + timedelta(minutes= random.randrange(500))
        leave_date = (seen_date) + timedelta(minutes= random.randrange(600))

        randno = random.randint(1,20)
        hospital_id = 'H' + '%s' % randno
        doctor_id = provider_codes[randno * 5]
        reason_code = random.randrange(39)
        
        discharge_code = random.choice(disposal_codes) 
        if discharge_code == 1:
            admitted_flag = 1
        else:
            admitted_flag = 0

        encounter_list = [medical_id, encounter_id, arrival_date, seen_date, \
            leave_date, hospital_id, doctor_id, admitted_flag, reason_code, discharge_code]
        outputWriter.writerow(encounter_list)
    outputFile.close()

s3.meta.client.upload_file('./historic_data/encounters/encounter_data.csv', 'angela-hospital-data', 'historic_data/'+'encounter_data.csv')

if __name__ == "__main__":
    start_time = datetime.now()
    encounterData()
    print ('total_time: ' + str(datetime.now() - start_time))