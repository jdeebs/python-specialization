sql = 'INSERT INTO stock (item_id, item_name, manufacturer_name, price, quantity) VALUES (%s, %s, %s, %s, %s)'

val1 = (4, 'Paper', 'Georgia-Pacific Corp.', 35, 40)
val2 = (5, 'Butter', 'Organic Valley', 18, 37)
val3 = (6, 'Pencils', 'Staedtler', 17, 55)