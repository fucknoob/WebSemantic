select count(*) from  (
select distinct id_usr  from web_cache where usr='igor.moraes' and processed='S' )
