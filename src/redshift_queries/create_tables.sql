DROP TABLE IF EXISTS patient;
create table patient(
	medicalid integer not null distkey sortkey,
	firstname varchar(30) not null,
	lastname varchar(30) not null,
	prefix varchar(30) null,
	gender integer not null,
	dob datetime not null,
	street varchar(100) not null,
	city varchar(30) not null,
	state char(30) not null,
	zipcode integer not null,
	email varchar(100) not null,
	phone_home varchar(20) not null,
	phone_biz varchar(20) not null,
  phone_cell varchar(20) null,
  marital_status varchar(10) null,
  nok_name varchar(50) not null,
	phone_nok varchar(20) not null,
  email varchar(50) not null,
  referrer_code varchar(8) not null,
  provider_code varchar(8) not null,
  social_sec varchar(10) not null,
  occupation varchar(50) null
);

DROP TABLE IF EXISTS encounter;
CREATE TABLE encounter
(
 medicalid integer NOT NULL,
 encounterid integer NOT NULL,
 arrival_date  timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
 seen_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
 leave_date  timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
 hospital_code varchar(10) NOT NULL,
 doctor_id varchar(10) NOT NULL,
 admitted_flag boolean NOT NULL,
 reason_code integer NOT NULL,
 discharge_code  integer NOT NULL
);

DROP TABLE IF EXISTS ref_icdten;
create table ref_icdten
(
icdcode varchar(8) not null,
icd_desc varchar(65) null,
icd_long_desc varchar (255) null,
nf_excl char(1) null
);

DROP TABLE IF EXISTS ref_hospital;
CREATE TABLE ref_hospital
(
 hospital_code  varchar(5)  NOT NULL,
 hospital_desc  varchar(50) NOT NULL
);

DROP TABLE IF EXISTS ref_ercomplaint;
CREATE TABLE ref_ercomplaint
(
 complaint_code  integer NOT NULL,
 complaint_desc  varchar(50) NOT NULL
);

DROP TABLE IF EXISTS elec_booking;
CREATE TABLE elec_booking
(
 medicalid int null,
 booking_type varchar(5) not null,
 booking_stage varchar(15) null, 
 booking_no varchar(20) not null, 
 intended_management varchar(5) null,
 booking_id varchar(20) not null, 
 hospital_id varchar(5) not null, 
 doctor_id varchar(5) not null, 
 appt_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
 modify_date timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
 expected_discharge timestamp DEFAULT ('now'::text)::timestamp without time zone NOT NULL,
 specialty int null 
);

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
