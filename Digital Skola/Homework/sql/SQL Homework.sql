--1. Buat query untuk menghitung total penjualan (dalam jumlah uang) yang dihasilkan oleh setiap produk.

select p.product_name , sum(s.quantity * p.price) as total_sales 
from products p 
	inner join sales s on s.product_id = p.product_id
group by p.product_name;

--2. Buat query untuk menghitung rata-rata harga produk per kategori.

select p.category, avg(p.price) as average
from products p
group by p.category;

-- 3. Buat query untuk menghitung total penjualan yang dihasilkan oleh setiap karyawan.

select e."name", sum(s.quantity * s.price) as total_sales_by_employees
from employees e 
	inner join sales s on e.employee_id = s.employee_id 
group by e."name" ;

-- 4. Buat query untuk mencari penjualan terbesar dan terkecil yang pernah terjadi.
select p.product_name, sum(s.quantity * s.price) as total_sales
from sales s
	inner join products p on p.product_id = s.product_id
group by p.product_name 
order by total_sales desc ;

-- 5. Buat query untuk mencari produk yang memiliki total penjualan tertinggi (berdasarkan jumlah unit yang terjual)
select p.product_name, sum(s.quantity) total_units
from sales s 
	inner join products p on p.product_id = s.product_id 
group by p.product_name
order by total_units desc 
limit 1;

-- 6. Buat query untuk mencari karyawan yang memiliki pendapatan di atas rata-rata.

select e.employee_id, e."name" , e.department_id, e.salary 
from employees e 
where e.salary > (
	select avg(salary)
	from employees e2 
);

-- 7. Buat query untuk menampilkan semua penjualan beserta nama produk dan nama karyawan yang terlibat.

select p.product_name, e."name" 
from sales s 
	inner join products p on p.product_id  = s.product_id 
	inner join employees e on e.employee_id = s.employee_id 
;

-- 8. Buat query untuk menghitung total penjualan yang dihasilkan oleh setiap departemen.

select d.department_name, sum(s.quantity * s.price) 
from sales s
	inner join employees e  on s.employee_id = e.employee_id 
	inner join departments d on d.department_id = e.department_id
group by d.department_name ;

-- 9. Buat query untuk menampilkan nama dan gaji karyawan yang gajinya di atas rata-rata.

select e."name", e.salary 
from employees e 
where e.salary > (
	select avg(salary)
	from employees e2 
);

-- 10. Buat query menggunakan CTE untuk mengetahui jumlah total gaji per departemen dan menampilkan departemen yang total gajinya lebih tinggi dari 100000.

with salary as (
	select d.department_id, sum(e.salary) as total_salary
	from departments d 
		inner join employees e on e.department_id = d.department_id 
	group by d.department_id 
)
select s.*
from departments d
	inner join salary s on s.department_id = d.department_id 
where s.total_salary > 100000;
