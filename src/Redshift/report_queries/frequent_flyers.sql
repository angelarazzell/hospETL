
-- Identify super-utilizers of Emergency Department. Alerts staff of safeguarding issues or patients looking for drugs, etc
drop table if exists #frequent;
drop table if exists #encounter;

select medicalid, count(*) as visitno, max(leave_date) as max_leave
into #frequent
from encounter
where leave_date >= '01 jan 2015'
group by medicalid
having count(*) > 3;

select e.*, h.hospital_desc, comp.*, row_number() over (partition by e.medicalid order by leave_date desc) as rownum
into #encounter
from encounter e, ref_hospital h, ref_ercomplaint comp
where h.hospital_code = e.hospital_code
and comp.complaint_code= e.reason_code
and leave_date >= '01 jan 2015';

select freq.medicalid, p.firstname, p.lastname, e1.hospital_desc as Hospital1, e1.arrival_date as ArrivalDate1
        , e1.complaint_desc as Complaint1, e2.hospital_desc as Hospital2, e2.arrival_date as ArrivalDate2
        , e2.complaint_desc as Complaint2, e3.hospital_desc as Hospital3, e3.arrival_date as ArrivalDate3
        , e3.complaint_desc as Complaint3, e4.hospital_desc as Hospital4, e4.arrival_date as ArrivalDate4
        , e4.complaint_desc as Complaint4, visitno-4 as AdditionalVisits
        
from #frequent freq
  inner join #encounter e1
  on freq.medicalid = e1.medicalid
  and freq.max_leave = e1.leave_date
  
  inner join #encounter e2
  on freq.medicalid = e2.medicalid
  and e2.rownum = 2

  inner join #encounter e3
  on freq.medicalid = e3.medicalid
  and e3.rownum = 3

  inner join #encounter e4
  on freq.medicalid = e4.medicalid
  and e4.rownum = 4
  
  left join patient p
  on p.medicalid = freq.medicalid
        
order by medicalid;
drop table #frequent;
drop table #encounter;
