
-- Identify super-utilizers of Emergency Department. Alerts staff of safeguarding issues or patients looking for drugs, etc
create table #frequent cte_frequent;
select medicalid, count(*) as visitno, min(leave_date) as min_leave
into #frequent cte_frequent
from encounter
where leave_date >= '01 jan 2015'
group by medicalid
having count(*) > 3;

select p.medicalid, p.firstname, p.lastname, e1.hospital_desc as Hospital1, e1.arrival_date as ArrivalDate1
        , e1.complaint_desc as Complaint1, e2.hospital_desc as Hospital2, e2.arrival_date as ArrivalDate2
        , e2.complaint_desc as Complaint2, e3.hospital_desc as Hospital3, e3.arrival_date as ArrivalDate3
        , e3.complaint_desc as Complaint3, e4.hospital_desc as Hospital4, e4.arrival_date as ArrivalDate4
        , e4.complaint_desc as Complaint4
from cte_frequent cte
  inner join (select e.*, h.hospital_desc, comp.*
        from encounter e, ref_hospital h, ref_ercomplaint comp
        where h.hospital_code = e.hospital_code
        and comp.complaint_code= e.reason_code
        and leave_date >= '01 jan 2015') e1
  on cte.medicalid = e1.medicalid
  and cte.min_leave = e1.leave_date
  
  inner join (select e.*, h.hospital_desc, comp.*
        from encounter e, ref_hospital h, ref_ercomplaint comp
        where h.hospital_code = e.hospital_code
        and comp.complaint_code= e.reason_code
        and leave_date >= '01 jan 2015') e2
  on cte.medicalid = e2.medicalid
  and e1.leave_date < e2.leave_date
  
  inner join (select e.*, h.hospital_desc, comp.*
        from encounter e, ref_hospital h, ref_ercomplaint comp
        where h.hospital_code = e.hospital_code
        and comp.complaint_code= e.reason_code
        and leave_date >= '01 jan 2015') e3
  on cte.medicalid = e3.medicalid
  and e2.leave_date < e3.leave_date

  inner join (select e.*, h.hospital_desc, comp.*
        from encounter e, ref_hospital h, ref_ercomplaint comp
        where h.hospital_code = e.hospital_code
        and comp.complaint_code= e.reason_code
        and leave_date >= '01 jan 2015') e4
  on cte.medicalid = e4.medicalid
  and e3.leave_date < e4.leave_date
  
  left join patient p
  on p.medicalid = cte.medicalid

drop table #frequent

