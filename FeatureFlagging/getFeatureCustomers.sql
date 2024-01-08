select c.contact_name, c.address, c.country, c.id from feature_customer
join customer c on feature_customer.customer_id = c.id
where feature_customer.feature_id = {{features.id}}