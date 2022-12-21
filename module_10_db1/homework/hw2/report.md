

SELECT table_phones.colour, COUNT(tc.phone_id) as count FROM table_phones JOIN table_checkout tc on table_phones.id = tc.phone_id GROUP BY tc.phone_id ORDER BY -count

синий,176 <br>
синий,164<br>
красный,163<br>
синий,160<br>
красный,141<br>
красный,125<br>
золотой,28<br>
голубой,23<br>
голубой,20<br>

чаще покупают синие
<br>
самый не популярний голубой
