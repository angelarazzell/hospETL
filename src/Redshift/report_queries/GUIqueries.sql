
--create view rep.vw_EmergencyVisit as
select 
  case when datediff(hours,enc.arrival_date,enc.seen_date) > 6 
        then 'Breach'
        else 'NonBreach'
  end as Breach,
  count(*) as NoVisits,
  hos.hospital_desc

from encounter enc, ref_hospital hos

where arrival_date >= dateadd(day, -14, getdate()) 

group by case when datediff(hours,enc.arrival_date,enc.seen_date) > 6 
        then 'Breach'
        else 'NonBreach'
  end,
  hos.hospital_desc
  

--quarterly IP activity
--create or replace view rep.vw_ipsparkline as
select hos.hospital_desc,
  sum(case when datepart(quarter, discharge_date) = datepart(quarter,dateadd(quarter, 1, start_period))
          and  datepart(year, discharge_date) = datepart(year, start_period)
      then 1
      else 0 end) as Q1,
  sum(case when datepart(quarter, discharge_date) =  datepart(quarter,dateadd(quarter, 2, start_period))
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1
      else 0 end) as Q2,
  sum(case when datepart(quarter, discharge_date) =  datepart(quarter,dateadd(quarter, 3, start_period))
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1
      else 0 end) as Q3,   
  sum(case when datepart(quarter, discharge_date) =  datepart(quarter, end_period)
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1
      else 0 end) as Q4,
  sum(case when datepart(quarter, discharge_date) = datepart(quarter, start_period)
          and  datepart(year, discharge_date) = datepart(year, start_period)
      then 1 else 0 end) -sum(case when datepart(quarter, discharge_date) = datepart(quarter,dateadd(quarter, 1, start_period))
          and  datepart(year, discharge_date) = datepart(year, start_period)
      then 1
      else 0 end) as Q1diff,
  sum(case when datepart(quarter, discharge_date) =  datepart(quarter,dateadd(quarter, 2, start_period))
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1 else 0 end) - sum(case when datepart(quarter, discharge_date) = datepart(quarter,dateadd(quarter, 1, start_period))
          and  datepart(year, discharge_date) = datepart(year, start_period)
      then 1
      else 0 end) as Q2diff,
  sum(case when datepart(quarter, discharge_date) =  datepart(quarter,dateadd(quarter, 3, start_period))
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1 else 0 end) - sum(case when datepart(quarter, discharge_date) = datepart(quarter,dateadd(quarter, 2, start_period))
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1
      else 0 end) as Q3diff,
  sum(case when datepart(quarter, discharge_date) =  datepart(quarter,dateadd(quarter, 4, start_period))
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1 else 0 end) - sum(case when datepart(quarter, discharge_date) = datepart(quarter,dateadd(quarter, 3, start_period))
          and  datepart(year, discharge_date) = datepart(year, end_period)
      then 1
      else 0 end) as Q4diff
 
from rep.vw_inpatientdc ip
  left join ref_hospital hos
    on hos.hospital_code = ip.hospital_id
  cross join (select cast('30 sep 16' as datetime) as end_period,
      cast('1 jul 15' as datetime) as start_period) dateparams
  
where discharge_date between start_period and end_period

group by hos.hospital_desc;

-------
--readmissions
select datediff(hours,arrival_date,seen_date) as wait_time, e.*, h.hospital_desc, c.complaint_desc 

from encounter e, ref_hospital h, ref_ercomplaint c 

where e.hospital_code = h.hospital_code 
and e.reason_code = c.complaint_code 
and arrival_date >= dateadd(day, -7, getdate()) 
and datediff(hours,arrival_date,seen_date) > 6 

order by datediff(hours,arrival_date,seen_date) desc
-----------------------------------------------------------------
