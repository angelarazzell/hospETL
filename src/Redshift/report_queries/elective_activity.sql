--create inpatient and daycase activity view from elective bookings data.
create or replace view rep.vw_inpatientdc as
select
  coalesce(cin.encounterno,book.booking_id) as encounterno,
	book.pathway_id,
	book.medical_id,	
	book.booking_type,
	case when cout.encounterno is not null then 'CheckedOut'
  	when cin.encounterno is not null then 'CheckedIn'
  	else 'Future' end as stage,
	book.intended_management,	
	book.hospital_id,
	book.doctor_id,
	book.appt_date,
	book.modify_date,	
	coalesce(cin.expected_discharge,book.expected_discharge),	
	book.specialty,
	book.priority,
	cin.adm_method_code,
	cin.attend_code,
	cin.ward,
	cin.arrival_datetime,
	cout.dead_on_discharge,
	cout.discharge_date,
	cout.outcome as attd_outcome
	
from (select pathway_id, max(modify_date) as max_modify
      from elective_booking_bp
      group by pathway_id) pathw
  inner join elective_booking_bp book
    on book.pathway_id = pathw.pathway_id
    and book.modify_date = pathw.max_modify
  left join checkin_bp cin
    on cin.pathway_id = book.pathway_id
    and cin.appt_date = book.appt_date
  left join checkout_bp cout
    on cin.encounterno = cout.encounterno
  
where booking_type = 'IP';
--------------------------------------------------------------
--create outpatient activity view from elective bookings data.
create or replace view rep.vw_outpatient as
select
  coalesce(cin.encounterno,book.booking_id) as encounterno,
	book.pathway_id,
	book.medical_id,	
	book.booking_type,
	case when cout.encounterno is not null then 'CheckedOut'
  	when cin.encounterno is not null then 'CheckedIn'
  	else 'Future' end as stage,
	book.intended_management,	
	book.hospital_id,
	book.doctor_id,
	book.appt_date,
	book.modify_date,	
	coalesce(cin.expected_discharge,book.expected_discharge),	
	book.specialty,
	book.priority,
	cin.adm_method_code,
	cin.attend_code,
	cin.ward,
	cin.arrival_datetime,
	cout.dead_on_discharge,
	cout.discharge_date,
	cout.outcome as attd_outcome
	
from (select pathway_id, max(modify_date) as max_modify
      from elective_booking
      group by pathway_id) pathw
  inner join elective_booking book
    on book.pathway_id = pathw.pathway_id
    and book.modify_date = pathw.max_modify
  left join checkin cin
    on cin.pathway_id = book.pathway_id
    and cin.appt_date = book.appt_date
  left join checkout cout
    on cin.encounterno = cout.encounterno
  
where booking_type = 'OP';
