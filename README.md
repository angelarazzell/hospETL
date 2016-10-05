
HospETL
=======

Generate fictional hospital data to deliver a prototype of an analytics platform.

Investigate Amazon Redshift as a distributed data warehouse solution, in order to deliver a dashboard in Flask to display reporting metrics such as:
- Inpatient Activity
- Emergency Activity including waiting time breaches
- Frequent Flyer report (patients who frequently visit the emergency department)

## Details

Design the schema for operational activity data
- Inpatient and outpatient activity
- Elective Bookings, Check-ins, Check-outs
- Emergency Encounters
- Patient Demographics
- Reference Data

## Pre-requisites

Python 3
AWS account
Boto3: to upload files to Amazon S3.
Amazon Redshift cluster: this project used 4 dc1.large nodes.
Flask: running from an AWS t2.micro instance.



