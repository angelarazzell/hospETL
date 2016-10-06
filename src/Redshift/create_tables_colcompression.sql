-- Reference table creations
DROP TABLE IF EXISTS ref_icdten;
create table ref_icdten
(
icdcode varchar(8) not null,
icd_desc varchar(65) null,
icd_long_desc varchar (255) null,
nf_excl char(1) null
);

analyze compression ref_hospital;
DROP TABLE IF EXISTS ref_hospital;
CREATE TABLE ref_hospital
(
 hospital_code  varchar(5)  NOT NULL encode raw,
 hospital_desc  varchar(50) NOT NULL encode raw
);

DROP TABLE IF EXISTS ref_ercomplaint;
CREATE TABLE ref_ercomplaint
(
 complaint_code  integer NOT NULL,
 complaint_desc  varchar(50) NOT NULL
);
--------------------------------------------------------------
--Activity data creations
DROP TABLE IF EXISTS patient;
create table patient(
	medicalid integer not null distkey sortkey ENCODE delta,
	firstname varchar(30) not null ENCODE text255,
	lastname varchar(30) not null ENCODE text32K,
	prefix varchar(30) null ENCODE bytedict,
	gender integer not null encode delta,
	dob datetime not null encode lzo,
	street varchar(100) not null encode lzo,
	city varchar(30) not null encode lzo,
	state char(30) not null encode bytedict,
	zipcode integer not null encode delta32k,
	--email varchar(100) not null encode lzo,
	phone_home varchar(20) not null encode lzo,
	phone_biz varchar(20) not null encode lzo,
  phone_cell varchar(20) null encode lzo,
  marital_status varchar(10) null encode bytedict,
  nok_name varchar(50) not null encode text32K,
	phone_nok varchar(20) not null encode lzo,
  email varchar(50) not null encode lzo,
  referrer_code varchar(8) not null encode runlength,
  provider_code varchar(8) not null encode runlength,
  social_sec varchar(10) not null encode lzo,
  occupation varchar(50) null encode lzo
);


DROP TABLE IF EXISTS encounter;
CREATE TABLE encounter_comp
(
 medicalid integer NOT null encode raw,
 encounterid integer NOT null encode delta,
 arrival_date  timestamp DEFAULT ('now'::text)::timestamp without time zone NOT null encode lzo,
 seen_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT null encode lzo,
 leave_date  timestamp DEFAULT ('now'::text)::timestamp without time zone NOT null encode lzo,
 hospital_code varchar(10) NOT null encode bytedict,
 doctor_id varchar(10) NOT null encode bytedict,
 admitted_flag boolean NOT null encode raw,
 reason_code integer NOT null encode delta,
 discharge_code  integer NOT NULL encode delta
);



-- DROP TABLE IF EXISTS elecive_booking;
-- CREATE TABLE elective_booking
-- (
--  medicalid int null,
--  booking_type varchar(5) not null,
--  booking_stage varchar(15) null, 
--  booking_no varchar(20) not null, 
--  intended_management varchar(5) null,
--  booking_id varchar(20) not null, 
--  hospital_id varchar(5) not null, 
--  doctor_id varchar(5) not null, 
--  appt_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
--  modify_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
--  expected_discharge timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
--  specialty int null 
-- );

DROP TABLE IF EXISTS apc_diagnosis;
CREATE TABLE apc_diagnosis
(
 medicalid int null,
 apcid varchar(15) not null,
 procedureid int null, 
 procedurecode varchar(15) not null,
 primaryflag bool not null, 
 sequence_no smallint not null);

DROP TABLE IF EXISTS admissions;
CREATE TABLE admissions
(
  medical_id int null,
  ed_id int null,
  apc_id varchar(15) null,
  admission_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
  doctor_id varchar(10) null,
  hospital_id varchar(10) null,
  discharge_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,  
  dead_on_discharge boolean null,
  ward varchar(25) null,
  expected_discharge_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
  comments varchar(500) not null,
  Admission_status varchar(10) null);

analyze compression elective_booking;
DROP TABLE IF EXISTS elective_booking_comp;
CREATE TABLE elective_booking_comp
(
  booking_id varchar(15) not null encode lzo,
  pathway_id varchar(15) not null encode lzo,
  medical_id integer not null  encode raw,
  booking_type varchar(20) null  encode lzo,
  booking_stage varchar(10) null  encode lzo,
  intended_management varchar(10) null  encode lzo,
  hospital_id varchar(8) null  encode bytedict,
  doctor_id varchar(10) null  encode bytedict,
  appt_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL  encode lzo, 
  modify_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL  encode lzo,
  expected_discharge timestamp DEFAULT ('now'::text)::timestamp without time zone NULL  encode lzo,
  specialty INT NULL  encode bytedict,
  priority CHAR NULL  encode lzo)


analyze compression checkin;
--drop TABLE checkin_comp;
create TABLE checkin_comp
(
  encounterno varchar(15) not null encode lzo,
  pathway_id varchar(15) not null encode lzo,
  medical_id int not null encode raw,
  adm_method_code varchar(3) null encode bytedict,
  attend_code smallint not null encode lzo,
  intended_management varchar(15) null encode lzo,
  hospital_id varchar(10) not null encode bytedict,
  ward varchar(20) null encode bytedict,
  doctor_id varchar(10) not null encode bytedict,
  appt_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL encode lzo, 
  arrival_datetime timestamp DEFAULT ('now'::text)::timestamp without time zone NULL encode lzo,
  expected_discharge timestamp DEFAULT ('now'::text)::timestamp without time zone NULL encode lzo,
  specialty int not null encode bytedict);

ANALYZE COMPRESSION checkout
CREATE TABLE checkout_comp
(
  encounterno varchar(15) not null encode lzo,
  pathway_id varchar(15) not null encode lzo,
  medicalid int not null encode raw,
  dead_on_discharge boolean not null encode raw,
  discharge_date timestamp DEFAULT ('now'::text)::timestamp without time zone NULL encode lzo,
  outcome varchar(10) not null encode bytedict);
  

------
--best practice
DROP TABLE IF EXISTS elective_booking_bp;
CREATE TABLE elective_booking_bp
(
  booking_id varchar(15) not null encode lzo,
  pathway_id varchar(15) not null encode lzo distkey,
  medical_id integer not null  encode raw,
  booking_type varchar(20) null  encode lzo,
  booking_stage varchar(10) null  encode lzo,
  intended_management varchar(10) null  encode lzo,
  hospital_id varchar(8) null  encode bytedict,
  doctor_id varchar(10) null  encode bytedict,
  appt_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL  encode lzo sortkey, 
  modify_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL  encode lzo,
  expected_discharge timestamp DEFAULT ('now'::text)::timestamp without time zone NULL  encode lzo,
  specialty INT NULL  encode bytedict,
  priority CHAR NULL  encode lzo)
;

--drop TABLE checkin_comp;
create TABLE checkin_bp
(
  encounterno varchar(15) not null encode lzo,
  pathway_id varchar(15) not null encode lzo distkey,
  medical_id int not null encode raw,
  adm_method_code varchar(3) null encode bytedict,
  attend_code smallint not null encode lzo,
  intended_management varchar(15) null encode lzo,
  hospital_id varchar(10) not null encode bytedict,
  ward varchar(20) null encode bytedict,
  doctor_id varchar(10) not null encode bytedict,
  appt_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL encode lzo sortkey, 
  arrival_datetime timestamp DEFAULT ('now'::text)::timestamp without time zone NULL encode lzo,
  expected_discharge timestamp DEFAULT ('now'::text)::timestamp without time zone NULL encode lzo,
  specialty int not null encode bytedict);

--ANALYZE COMPRESSION checkout
CREATE TABLE checkout_bp
(
  encounterno varchar(15) not null encode lzo distkey,
  pathway_id varchar(15) not null encode lzo,
  medicalid int not null encode raw,
  dead_on_discharge boolean not null encode raw,
  discharge_date timestamp DEFAULT ('now'::text)::timestamp without time zone NULL encode lzo sortkey,
  outcome varchar(10) not null encode bytedict);
