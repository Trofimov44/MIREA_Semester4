-- 1. supplier
INSERT INTO supplier (quantity) VALUES
(100),
(200);

-- 2. medications
INSERT INTO medications (quantity, supplier_id) VALUES
(50, 1),
(30, 2);

-- 3. client
INSERT INTO client (FCs, address, policynumber) VALUES
('John Doe', '123 Main St, City', 123456),
('Jane Smith', '456 Oak Ave, Town', 789012);

-- 4. payment
INSERT INTO payment (cost) VALUES
(150),
(300);

-- 5. employee
INSERT INTO employee (employee_id, FCs, phone_number, address) VALUES
(1, 'Dr. Alice Brown', '555-0101', '789 Pine Rd, City'),
(2, 'Nurse Bob Green', '555-0102', '321 Elm St, Town');

-- 6. post
INSERT INTO post (post_id, diploma, accreditation) VALUES
(1, 'MD', 'Certified Physician'),
(2, 'RN', 'Registered Nurse');

-- 7. employee_post
INSERT INTO employee_post (employee_id, post_id) VALUES
(1, 1),
(2, 2);

-- 8. type_of_appointment
INSERT INTO type_of_appointment (id_of_the_appointment_type, title) VALUES
(1, 'General Checkup'),
(2, 'Specialist Consultation');

-- 9. recommendations
INSERT INTO recommendations (entry_id, recommendation_id) VALUES
(1, 1),
(2, 2);

-- 10. appointment
INSERT INTO appointment (clients_id, employe_id, time, date, office, medications_id, id_of_the_record_type, entry_id, recommendation_id) VALUES
(1, 1, 1625097600, '2025-06-01', 'Office A', 1, 1, 1, 1),
(2, 2, 1625184000, '2025-06-02', 'Office B', 2, 2, 2, 2);

-- 11. payment_appointment
INSERT INTO payment_appointment (payment_id, entry_id) VALUES
(1, 1),
(2, 2);

-- 12. feedback
INSERT INTO feedback (clients_id, review_text, rating) VALUES
(1, 'Great service, very professional!', 5),
(2, 'Satisfactory, but wait time was long.', 3);

-- 13. cheque
INSERT INTO cheque (cost, date, payment_id) VALUES
(150, '2025-06-01', 1),
(300, '2025-06-02', 2);