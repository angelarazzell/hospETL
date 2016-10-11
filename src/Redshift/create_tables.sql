-- Reference table creations
DROP TABLE IF EXISTS ref_icdten;
CREATE TABLE ref_icdten
(
  icdcode varchar(8) not null,
  icd_desc varchar(65) null,
  icd_long_desc varchar (255) null,
  nf_excl char(1) null);

DROP TABLE IF EXISTS ref_hospital;
CREATE TABLE ref_hospital
(
  hospital_code varchar(5) not null,
  hospital_desc varchar(50) not null);

DROP TABLE IF EXISTS ref_ercomplaint;
CREATE TABLE ref_ercomplaint
(
  complaint_code integer not null,
  complaint_desc varchar(50) not null);

DROP TABLE IF EXISTS ref_doctor;
CREATE TABLE ref_doctor
(
  dr_code varchar(5) not null,
  dr_name varchar(50) not null);
 
DROP TABLE IF EXISTS ref_erdisposal;
CREATE TABLE ref_erdisposal
(
  disposal_code integer not null,
  disposal_desc varchar(100) not null);
 
--------------------------------------------------------------
--Activity data creations
DROP TABLE IF EXISTS patient;
CREATE TABLE patient(
  medicalid integer not null,
  firstname varchar(30) not null,
  lastname varchar(30) not null,
  prefix varchar(30) null,
  gender integer not null,
  dob datetime not null,
  street varchar(100) not null,
  city varchar(30) not null,
  state char(30) not null,
  zipcode integer not null,
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
  occupation varchar(50) null);

DROP TABLE IF EXISTS encounter;
CREATE TABLE encounter
(
  medicalid integer not null,
  encounterid integer not null,
  arrival_date timestamp default ('now'::text)::timestamp without time zone not null,
  seen_date timestamp default ('now'::text)::timestamp without time zone not null,
  leave_date timestamp default ('now'::text)::timestamp without time zone not null,
  hospital_code varchar(10) not null,
  doctor_id varchar(10) not null,
  admitted_flag boolean not null,
  reason_code integer not null,
  discharge_code integer not null);

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
  admission_date timestamp default ('now'::text)::timestamp without time zone not null,
  doctor_id varchar(10) null,
  hospital_id varchar(10) null,
  discharge_date timestamp default ('now'::text)::timestamp without time zone not null, 
  dead_on_discharge boolean null,
  ward varchar(25) null,
  expected_discharge_date timestamp default ('now'::text)::timestamp without time zone not null,
  comments varchar(500) not null,
  Admission_status varchar(10) null);

DROP TABLE IF EXISTS elective_booking;
CREATE TABLE elective_booking
(
  booking_id varchar(15) not null,
  pathway_id varchar(15) not null,
  medical_id integer not null,
  booking_type varchar(20) null,
  booking_stage varchar(10) null,
  intended_management varchar(10) null,
  hospital_id varchar(8) null, 
  doctor_id varchar(10) null, 
  appt_date timestamp default ('now'::text)::timestamp without time zone not null, 
  modify_date timestamp default ('now'::text)::timestamp without time zone not null,
  expected_discharge timestamp default ('now'::text)::timestamp without time zone null, 
  specialty INT null,
  priority CHAR null);
 
DROP TABLE IF EXISTS checkin;
CREATE TABLE checkin
(
  encounterno varchar(15) not null,
  pathway_id varchar(15) not null, 
  medical_id int not null,
  adm_method_code varchar(3) null,
  attend_code smallint not null,
  intended_management varchar(15) null,
  hospital_id varchar(10) not null,
  ward varchar(20) null, 
  doctor_id varchar(10) not null,
  appt_date timestamp default ('now'::text)::timestamp without time zone not null, 
  arrival_datetime timestamp default ('now'::text)::timestamp without time zone null, 
  expected_discharge timestamp default ('now'::text)::timestamp without time zone null, 
  specialty int not null);
 
DROP TABLE IF EXISTS checkout;
CREATE TABLE checkout
(
  encounterno varchar(15) not null,
  pathway_id varchar(15) not null,
  medicalid int not null,
  dead_on_discharge boolean not null,
  discharge_date timestamp default ('now'::text)::timestamp without time zone null,
  outcome varchar(10) not null);

