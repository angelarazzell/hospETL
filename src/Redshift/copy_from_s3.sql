--credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' replace ABC and XYZ with user credentials
--Copy data from S3 into tables

--Reference table imports:

--truncate table ref_erdisposal
copy ref_erdisposal from 's3://angela-hospital-data/reference_data/ER_disposal_code.txt' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ'
csv truncatecolumns;

--truncate table ref_doctor;
copy ref_doctor from 's3://angela-hospital-data/reference_data/doctor_lookup.txt' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ'
csv truncatecolumns;

--truncate table ref_ercomplaint;
copy ref_ercomplaint from 's3://angela-hospital-data/reference_data/ER_complaint_lookup.txt' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--truncate table ref_hospital;
copy ref_hospital from 's3://angela-hospital-data/reference_data/hospitallookup.txt' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ'
csv truncatecolumns;

--truncate table ref_icdten;
copy ref_icdten from 's3://angela-hospital-data/reference_data/ref_icd10.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv delimiter '\t' truncatecolumns;
--DELETE HEADER:
DELETE from ref_icdten where icdcode = 'DCODE'

-----------------------------------------------------------------------------------------------------------------
----historic data imports from S3:

--truncate table patient;
copy patient from 's3://angela-hospital-data/historic_data/pt_dat.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--truncate table encounter;
copy encounter from 's3://angela-hospital-data/encounter_dat.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--------------------------
--truncate table elec_booking;
copy elective_booking from 's3://angela-hospital-data/historic_data/OP_create.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

copy elective_booking from 's3://angela-hospital-data/historic_data/DC_create.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

copy elective_booking from 's3://angela-hospital-data/historic_data/IP_create.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

copy elective_booking from 's3://angela-hospital-data/historic_data/OP_modify.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

copy elective_booking from 's3://angela-hospital-data/historic_data/DC_modify.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

copy elective_booking from 's3://angela-hospital-data/historic_data/IP_modify.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--------------------------
--check ins
copy checkin from 's3://angela-hospital-data/historic_data/ipdc_checkin.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

copy checkin from 's3://angela-hospital-data/historic_data/OP_checkin.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

--------------------------
--check outs
copy checkout from 's3://angela-hospital-data/historic_data/ipdc_checkouts.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;

copy checkout from 's3://angela-hospital-data/historic_data/op_checkouts.csv' 
credentials 'aws_access_key_id=ABC;aws_secret_access_key=XYZ' 
csv truncatecolumns;



