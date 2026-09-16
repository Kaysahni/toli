/* carrier_scorecard.sql
   owner: Procurement (Nils Ekholm)
   used in: quarterly carrier business reviews
   schedule: Mondays 07:30 */

select
    c.carrier_id,
    c.carrier_name,
    count(distinct s.shipment_id)                                      as loads,
    avg(case when s.picked_up_at <= s.pickup_window_end then 1 else 0 end) as pickup_on_time,
    avg(case when s.status = 'DELIVERED' and s.delivered_at <= s.window_end then 1 else 0 end) as delivery_on_time,
    count(distinct cl.claim_id)                                        as claims,
    sum(cl.settled_eur)                                                as claims_settled_eur
from shipments.carrier c
join shipments.shipment s on s.carrier_id = c.carrier_id
left join claims.claim cl on cl.shipment_id = s.shipment_id
where s.picked_up_at >= date_trunc('quarter', current_date)
group by 1, 2
having count(distinct s.shipment_id) >= 20
order by loads desc;
