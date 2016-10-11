--Activity data table creations including compression and distkey, sortkey
DROP TABLE IF EXISTS patient;
CREATE TABLE patient(
	medicalid integer not null sortkey distkey,
	firstname varchar(30) not null ENCODE text255,
	lastname varchar(30) not null ENCODE text32K,
	prefix varchar(30) null ENCODE bytedict,
	gender integer not null encode delta,
	dob datetime not null encode delta,
	street varchar(100) not null encode lzo,
	city varchar(30) not null encode lzo,
	state char(30) not null encode bytedict,
	zipcode integer not null encode delta32k,
	phone_home varchar(20) not null encode lzo,
	phone_biz varchar(20) not null encode lzo,
  phone_cell varchar(20) null encode lzo,
  marital_status varchar(10) null encode bytedict,
  nok_name varchar(50) not null encode text32K,
	phone_nok varchar(20) not null encode lzo,
  email varchar(50) not null encode lzo,
  referrer_code varchar(8) not null encode runlength,
  doctor_code varchar(8) not null encode runlength,
  social_sec varchar(10) not null encode lzo,
  occupation varchar(50) null encode lzo
);

DROP TABLE IF EXISTS encounter;
CREATE TABLE encounter
(
 medicalid integer not null distkey,
 encounterid integer not null encode delta,
 arrival_date  datetime not null encode delta,
 seen_date datetime not null encode delta,
 leave_date  datetime not null sortkey,
 hospital_code varchar(10) not null encode bytedict,
 doctor_id varchar(10) not null encode runlength,
 admitted_flag boolean not null encode raw,
 reason_code integer not null encode delta,
 discharge_code  integer not null encode delta
);

DROP TABLE IF EXISTS elective_booking;
CREATE TABLE elective_booking
(
  booking_id varchar(15) not null encode lzo,
  pathway_id varchar(15) not null distkey,
  medical_id integer not null  encode raw,
  booking_type varchar(20) null  encode lzo,
  booking_stage varchar(10) null  encode lzo,
  intended_management varchar(10) null  encode lzo,
  hospital_id varchar(8) null  encode bytedict,
  doctor_id varchar(10) null  encode bytedict,
  appt_date datetime not null sortkey, 
  modify_date datetime not null  encode lzo,
  expected_discharge datetime null  encode lzo,
  specialty INT null  encode bytedict,
  priority CHAR null  encode lzo)
;

DROP TABLE IF EXISTS checkin;
CREATE TABLE checkin
(
  encounterno varchar(15) not null encode lzo,
  pathway_id varchar(15) not null distkey,
  medical_id int not null,
  adm_method_code varchar(3) null encode bytedict,
  attend_code smallint not null encode lzo,
  intended_management varchar(15) null encode lzo,
  hospital_id varchar(10) not null encode bytedict,
  ward varchar(20) null encode bytedict,
  doctor_id varchar(10) not null encode bytedict,
  appt_date datetime not null sortkey, 
  arrival_datetime datetime null encode delta,
  expected_discharge datetime null encode delta,
  specialty int not null encode bytedict);

DROP TABLE IF EXISTS checkout;
CREATE TABLE checkout
(
  encounterno varchar(15) not null encode lzo,
  pathway_id varchar(15) not null distkey,
  medicalid int not null,
  dead_on_discharge boolean not null encode raw,
  discharge_date datetime sortkey,
  outcome varchar(10) not null encode bytedict);

