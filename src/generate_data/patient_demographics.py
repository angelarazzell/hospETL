import json
import sys
import random
import csv
from datetime import datetime, timedelta
from faker import Factory
from dateutil.parser import parse

# 3 different consumer nodes
def patient_data(fake):
    """generate fake patient demographic data"""
    mar_stat = ['single', 'married', 'divorced', 'widowed', 'separated', ',single', 'married', 'divorced,,single']
    gender_list = [0,1,2,9,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    provider_codes = ['C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,C11,C12,C13,C14,C15,C16,C17,C18,G19,G20,G21,G22,G23,G24,G25,G26,G27,G28,G29,G30,G31,G32,G33,G34,G35,G36,G37,G38,G39,G40,G41,G42,G43,G44,G45,G46,G47,D48,D49,D50,D51,D52,D53,G54,G55,G56,G57,G58,G59,G60,G61,G62,G63,G64,G65,G66,G67,G68,G69,G70,G71,G72,G73,G74,G75,G76,G77,G78,G79,G80,G81,G82,G83,G84,G85,G86,G87,G88,G89,G90,G91,G92,G93,G94,G95,G96,G97,G98,G99,G100,G101']
    outputFile = open('./historic_data/patient_data.csv', 'w', newline='')
    outputWriter = csv.writer(outputFile)
    
    for i in range(1,10000000):
        gender = random.choice(gender_list)
        if gender == 1:
            firstname = fake.first_name_male()
            prefix = fake.prefix_male()
        elif gender == 2:
            firstname = fake.first_name_female()
            prefix = fake.prefix_female()
        else: 
            firstname = fake.first_name()
            prefix = ''
        
        lastname = fake.last_name()
        dob = fake.date()
        
        if datetime.now() - 16*(timedelta(days=365)) < parse(dob):
            prefix = ''
            occupation = ''
            status = 'single'
        
        else: 
            occupation = random.choice(['',fake.job()])
            status = random.choice(mar_stat)
        
        street = fake.street_address()
        postal_code = fake.postalcode()
        city = fake.city()
        state = fake.state()
        social_sec = fake.ssn() # replace -
        phone_home = fake.phone_number() # '(619) 555-2222'
        phone_biz = fake.phone_number() #'(619) 555-3333'
        phone_contact = fake.phone_number() #'(619) 555-1111'
        phone_cell = ''
        nok_name = fake.name()
        email = fake.email()
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
        
if __name__ == "__main__":
    start_time = datetime.now()
    fake = Factory.create()
    patient_data(fake)
    print ('total_time: ' + str(datetime.now() - start_time))