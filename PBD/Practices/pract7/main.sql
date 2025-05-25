

CREATE TABLE supplier (
  supplier_id bigserial NOT NULL PRIMARY KEY,
  quantity integer NOT NULL
);


CREATE TABLE medications (
  medications_id bigserial NOT NULL PRIMARY KEY,
  quantity integer NOT NULL,
  supplier_id bigint NOT NULL
);


CREATE TABLE client (
  clients_id bigserial NOT NULL PRIMARY KEY,
  FCs varchar(50) NOT NULL,
  address varchar(50) NOT NULL,
  policynumber integer NOT NULL
);


CREATE TABLE payment (
  payment_id bigserial NOT NULL PRIMARY KEY,
  cost integer NOT NULL
);


CREATE TABLE payment_appointment (
  payment_id bigint NOT NULL,
  entry_id bigint NOT NULL,
  payment_appointment_id bigserial PRIMARY KEY
);


CREATE TABLE recommendations (
  entry_id bigint NOT NULL,
  recommendation_id bigint NOT NULL PRIMARY KEY
);


CREATE TABLE feedback (
  review_id bigserial NOT NULL PRIMARY KEY,
  clients_id bigint NOT NULL,
  review_text text NOT NULL,
  rating integer NOT NULL
);


CREATE TABLE employee (
  employee_id bigint NOT NULL PRIMARY KEY,
  FCs text NOT NULL,
  phone_number text NOT NULL,
  address text NOT NULL
);


CREATE TABLE appointment (
  clients_id bigint NOT NULL,
  employe_id bigint,
  time bigint NOT NULL,
  date date NOT NULL,
  office varchar(50) NOT NULL,
  medications_id bigint NOT NULL,
  id_of_the_record_type bigint NOT NULL,
  entry_id bigint NOT NULL PRIMARY KEY,
  recommendation_id bigint NOT NULL
);


CREATE TABLE employee_post (
  employee_post_id bigserial NOT NULL PRIMARY KEY,
  employee_id bigint NOT NULL,
  post_id bigint NOT NULL
);


CREATE TABLE type_of_appointment (
  id_of_the_appointment_type bigint NOT NULL PRIMARY KEY,
  title varchar(50) NOT NULL
);


CREATE TABLE post (
  post_id bigint NOT NULL PRIMARY KEY,
  diploma varchar(50) NOT NULL,
  accreditation text NOT NULL
);


CREATE TABLE cheque (
  cheque_id bigserial NOT NULL PRIMARY KEY,
  cost integer NOT NULL,
  date date NOT NULL,
  payment_id bigint NOT NULL
);


ALTER TABLE appointment ADD CONSTRAINT appointment_clients_id_fk FOREIGN KEY (clients_id) REFERENCES client (clients_id);
ALTER TABLE appointment ADD CONSTRAINT appointment_employe_id_fk FOREIGN KEY (employe_id) REFERENCES employee (employee_id);
ALTER TABLE appointment ADD CONSTRAINT appointment_id_of_the_record_type_fk FOREIGN KEY (id_of_the_record_type) REFERENCES type_of_appointment (id_of_the_appointment_type);
ALTER TABLE appointment ADD CONSTRAINT appointment_recommendation_id_fk FOREIGN KEY (recommendation_id) REFERENCES recommendations (recommendation_id);
ALTER TABLE feedback ADD CONSTRAINT feedback_clients_id_fk FOREIGN KEY (clients_id) REFERENCES client (clients_id);
ALTER TABLE employee_post ADD CONSTRAINT employee_post_employee_id_fk FOREIGN KEY (employee_id) REFERENCES employee (employee_id);
ALTER TABLE employee_post ADD CONSTRAINT employee_post_post_id_fk FOREIGN KEY (post_id) REFERENCES post (post_id);
ALTER TABLE payment_appointment ADD CONSTRAINT payment_appointment_entry_id_fk FOREIGN KEY (entry_id) REFERENCES appointment (entry_id);
ALTER TABLE payment_appointment ADD CONSTRAINT payment_appointment_payment_id_fk FOREIGN KEY (payment_id) REFERENCES payment (payment_id);
ALTER TABLE medications ADD CONSTRAINT medications_supplier_id_fk FOREIGN KEY (supplier_id) REFERENCES supplier (supplier_id);
ALTER TABLE appointment ADD CONSTRAINT appointment_medications_id_fk FOREIGN KEY (medications_id) REFERENCES medications (medications_id);
ALTER TABLE cheque ADD CONSTRAINT cheque_payment_id_fk FOREIGN KEY (payment_id) REFERENCES payment (payment_id);
