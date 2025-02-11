CREATE USER backendUser WITH PASSWORD 'password';

CREATE DATABASE backend;

GRANT ALL PRIVILEGES ON DATABASE backend TO backendUser;

\c backend;

CREATE TABLE driver (
  id SERIAL NOT NULL PRIMARY KEY,
  name VARCHAR(255),
  surname VARCHAR(255),
  account_balance DECIMAL(10, 2)
);

ALTER TABLE driver OWNER to backendUser;

CREATE TABLE car (
  id SERIAL NOT NULL PRIMARY KEY,
  driver_id INT NOT NULL,
  brand VARCHAR(255),
  model VARCHAR(255),
  registration VARCHAR(255) NOT NULL,
  CONSTRAINT fk_driver FOREIGN KEY(driver_id) REFERENCES driver(id)
);

ALTER TABLE car OWNER to backendUser;

CREATE TABLE ticket (
  id SERIAL NOT NULL PRIMARY KEY,
  car_id INT NOT NULL,
  entrance_date timestamp NOT NULL,
  exit_date timestamp,
  amount DECIMAL(10, 2),
  payed boolean DEFAULT false,
  CONSTRAINT fk_car FOREIGN KEY(car_id) REFERENCES car(id)
);

ALTER TABLE ticket OWNER to backendUser;
