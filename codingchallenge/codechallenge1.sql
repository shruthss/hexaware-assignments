/**car rental**/
create database carent
use carent

create table vehicle (
    vehicleid int primary key,
    make varchar(50),
    model varchar(50),
    year int,
    dailyrate decimal(10,2),
    status bit, /* 1 = available, 0 = not available */
    passengercapacity int,
    enginecapacity int
);

-- customer table
create table customer (
    customerid int primary key,
    firstname varchar(50),
    lastname varchar(50),
    email varchar(100),
    phonenumber varchar(20)
);

-- lease table
create table lease (
    leaseid int primary key,
    vehicleid int foreign key references vehicle(vehicleid),
    customerid int foreign key references customer(customerid),
    startdate date,
    enddate date,
    type varchar(20) check (type in('daily','monthly'))
    
);

-- payment table
create table payment (
    paymentid int primary key,
    leaseid int foreign key  references lease(leaseid),
    paymentdate date,
    amount decimal(10,2),
);


insert into vehicle (vehicleid, make, model, year, dailyrate, status, passengercapacity, enginecapacity) values
(1, 'toyota', 'camry', 2022, 50.00, 1, 4, 1450),
(2, 'honda', 'civic', 2023, 45.00, 1, 7, 1500),
(3, 'ford', 'focus', 2022, 48.00, 0, 4, 1400),
(4, 'nissan', 'altima', 2023, 52.00, 1, 7, 1200),
(5, 'chevrolet', 'malibu', 2022, 47.00, 1, 4, 1800),
(6, 'hyundai', 'sonata', 2023, 49.00, 0, 7, 1400),
(7, 'bmw', '3 series', 2023, 60.00, 1, 7, 2499),
(8, 'mercedes', 'c-class', 2022, 58.00, 1, 8, 2599),
(9, 'audi', 'a4', 2022, 55.00, 0, 4, 2500),
(10, 'lexus', 'es', 2023, 54.00, 1, 4, 2500);

insert into customer (customerid, firstname, lastname, email, phonenumber) values
(1, 'john', 'doe', 'johndoe@example.com', '555-555-5555'),
(2, 'jane', 'smith', 'janesmith@example.com', '555-123-4567'),
(3, 'robert', 'johnson', 'robert@example.com', '555-789-1234'),
(4, 'sarah', 'brown', 'sarah@example.com', '555-456-7890'),
(5, 'david', 'lee', 'david@example.com', '555-987-6543'),
(6, 'laura', 'hall', 'laura@example.com', '555-234-5678'),
(7, 'michael', 'davis', 'michael@example.com', '555-876-5432'),
(8, 'emma', 'wilson', 'emma@example.com', '555-432-1098'),
(9, 'william', 'taylor', 'william@example.com', '555-321-6547'),
(10, 'olivia', 'adams', 'olivia@example.com', '555-765-4321');

insert into lease (leaseid, vehicleid, customerid, startdate, enddate, type) values
(1, 1, 1, '2023-01-01', '2023-01-05', 'daily'),
(2, 2, 2, '2023-02-15', '2023-02-28', 'monthly'),
(3, 3, 3, '2023-03-10', '2023-03-15', 'daily'),
(4, 4, 4, '2023-04-20', '2023-04-30', 'monthly'),
(5, 5, 5, '2023-05-05', '2023-05-10', 'daily'),
(6, 4, 3, '2023-06-15', '2023-06-30', 'monthly'),
(7, 7, 7, '2023-07-01', '2023-07-10', 'daily'),
(8, 8, 8, '2023-08-12', '2023-08-15', 'monthly'),
(9, 3, 3, '2023-09-07', '2023-09-10', 'daily'),
(10, 10, 10, '2023-10-10', '2023-10-31', 'monthly');

insert into payment (paymentid, leaseid, paymentdate, amount) values
(1, 1, '2023-01-03', 200.00),
(2, 2, '2023-02-20', 1000.00),
(3, 3, '2023-03-12', 75.00),
(4, 4, '2023-04-25', 900.00),
(5, 5, '2023-05-07', 60.00),
(6, 6, '2023-06-18', 1200.00),
(7, 7, '2023-07-03', 40.00),
(8, 8, '2023-08-14', 1100.00),
(9, 9, '2023-09-09', 80.00),
(10, 10, '2023-10-25', 1500.00);

/*q1--Update the daily rate for a Mercedes car to 68.*/

update vehicle set dailyrate=68 where make = 'merecedes';

/*q2--Delete a specific customer and all associated leases and payments.*/

delete from Payment where leaseID IN (select leaseID from Lease where customerID = 7);
delete from Lease where customerID = 7;
delete from Customer where customerID = 7;

/*q3--Rename the "paymentDate" column in the Payment table to "transactionDate".*/

exec sp_rename 'payment.paymentdate', 'transactiondate', 'column';

/*q4--Find a specific customer by email.*/

select * from Customer
where email = 'robert@example.com'

/*q5--Get active leases for a specific customer.*/

select * from lease
where customerid = 4 and enddate >= cast(getdate() as date);

/*q6--Find all payments made by a customer with a specific phone number.*/
select p.paymentid,p.leaseid,p.transactiondate,p.amount from payment p join lease l on p.leaseid=l.leaseid
join customer c on l.customerid=c.customerid where c.phonenumber='555-123-4567'

/*q7--Calculate the average daily rate of all available cars.*/

select AVG(dailyRate) AS averageDailyRate from Vehicle
where status = 1;

/*q8--Find the car with the highest daily rate.*/

select top 1 * from vehicle
order by dailyrate desc;

/*q9--Retrieve all cars leased by a specific customer.*/

select v.* from Vehicle v
join Lease l on v.vehicleID = l.vehicleID
where l.customerID = 8;

/*q10--Find the details of the most recent lease.*/
select top 1 * from lease
order by enddate desc;

/*q11--List all payments made in the year 2023.*/
select * from payment
where year(transactiondate) = 2023;

/*q12--Retrieve customers who have not made any payments.*/

select * from Customer
where customerID NOT IN (
  select distinct customerID
  from Lease l
  join Payment p ON l.leaseID = p.leaseID
);
/***returns same***/
select c.*
from customer c
left join lease l on c.customerid = l.customerid
left join payment p on l.leaseid = p.leaseid
where p.paymentid is null;

/*q13--Retrieve Car Details and Their Total Payments.*/

select vehicleid, make, model,
  (
    select sum(p.amount)
    from lease l
    join payment p on l.leaseid = p.leaseid
    where l.vehicleid = v.vehicleid
  ) as totalpayments
from vehicle v;

/*q14--Calculate Total Payments for Each Customer.*/
select customerid, firstname, lastname,
  (
    select sum(p.amount)
    from lease l
    join payment p on l.leaseid = p.leaseid
    where l.customerid = c.customerid
  ) as totalpaid
from customer c;

/*q15--List Car Details for Each Lease.*/

select l.leaseID, v.*, l.startDate, l.endDate
from Lease l
join Vehicle v on l.vehicleID = v.vehicleID;

/*q16--Retrieve Details of Active Leases with Customer and Car Information.*/

select l.*, c.firstname, c.lastname, v.make, v.model
from lease l
join customer c on l.customerid = c.customerid
join vehicle v on l.vehicleid = v.vehicleid
where l.enddate >= cast(getdate() as date);

/*q17--Find the Customer Who Has Spent the Most on Leases.*/
select top 1 customerid, firstname, lastname, totalspent
from (
    select c.customerid, c.firstname, c.lastname, sum(p.amount) as totalspent
    from customer c
    join lease l on c.customerid = l.customerid
    join payment p on l.leaseid = p.leaseid
    group by c.customerid, c.firstname, c.lastname
) as customer_totals
order by totalspent desc;

/*q18--List All Cars with Their Current Lease Information.*/

select v.vehicleID, v.make, v.model, l.startDate, l.endDate
from Vehicle v
left join Lease l on v.vehicleID = l.vehicleID AND l.endDate >= cast(getdate() as date)
left join Customer c on l.customerID = c.customerID;




















