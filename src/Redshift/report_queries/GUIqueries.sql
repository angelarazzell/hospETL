--emergency visits and breach numbers

CREATE OR REPLACE VIEW rep.vw_emergencycount AS 
 SELECT sum(
        CASE
            WHEN date_diff('hours', enc.arrival_date, enc.seen_date) > 6 THEN 1
            ELSE 0
        END) AS breach, sum(
        CASE
            WHEN date_diff('hours', enc.arrival_date, enc.seen_date) <= 6 THEN 1
            ELSE 0
        END) AS nonbreach, hos.hospital_desc
   FROM encounter enc, ref_hospital hos
  WHERE hos.hospital_code = enc.hospital_code AND enc.arrival_date >= date_add('day', -28, getdate())
  GROUP BY hos.hospital_desc;

------------------------------------------------------------------------------------------------------
--quarterly IP activity

create or replace view rep.vw_ipsparkline as
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
  --quarter by quarter activity differences:
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
