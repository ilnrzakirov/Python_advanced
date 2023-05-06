SELECT c.full_name as client1, c2.full_name, c.city, m.full_name as client2 FROM customer as c
    JOIN customer c2 on m.manager_id = c2.manager_id AND c.full_name != c2.full_name
    JOIN manager m on m.manager_id = c.manager_id
    WHERE m.manager_id == c.manager_id AND c.manager_id == c2.manager_id
