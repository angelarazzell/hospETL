
import json
import sys
import random
import csv
import boto3
from datetime import datetime, timedelta
from faker import Factory
from dateutil.parser import parse

s3 = boto3.resource('s3')

def patient_data(gen_data):
    """generates 10,000,000 records of fake patient demographic data
    using the Faker package https://pypi.python.org/pypi/fake-factory/0.7.2"""
    
    mar_stat = ['single','married'] * 3
    mar_stat.extend(['divorced','widowed','separated','','divorced']
    gender_list = [1,2]*25
    gender_list.extend([0,9])
    ref_file = open('./reference_data/doctor_lookup.txt', 'r')
    reader = csv.reader(ref_file)
    provider_codes = []
    for line in reader:
    	provider_codes.append(line[0])

    outputFile = open('./historic_data/patient_data.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    
    for i in range(1,10000000):
        gender = random.choice(gender_list)
        if gender == 1:
            firstname = gen_data.first_name_male()
            prefix = gen_data.prefix_male()
        elif gender == 2:
            firstname = gen_data.first_name_female()
            prefix = gen_data.prefix_female()
        else: 
            firstname = gen_data.first_name()
            prefix = ''
        
        lastname = gen_data.last_name()
        dob = gen_data.date()
        
        if datetime.now() - 16*(timedelta(days=365)) < parse(dob):
            prefix = ''
            occupation = ''
            status = 'single'
        
        else: 
            occupation = random.choice(['',gen_data.job()])
            status = random.choice(mar_stat)
        
        street = gen_data.street_address()
        postal_code = gen_data.postalcode()
        city = gen_data.city()
        state = gen_data.state()
        social_sec = gen_data.ssn() # includes dashes -
        phone_home = gen_data.phone_number() # includes non-numerics
        phone_biz = gen_data.phone_number() 
        phone_contact = gen_data.phone_number()
        phone_cell = ''
        nok_name = gen_data.name()
        email = gen_data.email()
        referrer_code = random.choice(provider_codes)
        provider_code = random.choice(provider_codes)
        
        pati_list = [ i, \
        firstname, \
        lastname, \
        prefix, \
        gender, \
        dob, \
        street, \
        postal_code, \
        city, \
        state, \
        social_sec, \
        occupation, \
        phone_home, \
        phone_biz, \
        phone_contact, \
        phone_cell, \
        status,\
        nok_name,\
        email,\
        referrer_code,\
        provider_code]
        
        outputWriter.writerow(pati_list)
        
    outputFile.close()
    ref_file.close()
    s3.meta.client.upload_file('./historic_data/patient_data.csv', 'angela-hospital-data', 'historic_data/'+'patient_data.csv')
    
if __name__ == "__main__":
    start_time = datetime.now()
    gen_data = Factory.create()
    patient_data(gen_data)
    print ('total_time: ' + str(datetime.now() - start_time))