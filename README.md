# Umina-task-2023

<!-- ABOUT THE PROJECT -->
## Sale order multiple warehouse

This Odoo 17 module "sale_order_line_multiple_warehouse" is based on Umina task 2023: [a relative link](Programavimo_uzduotis.pdf)<br/>

### Tech stack:
* Odoo 17
* PostgreSQL 15
* Docker compose

### Prerequisites

* Docker & docker-compose


### Setup

1. In project root directory create `.env` file. It should have these environment variables:
   ```env
   POSTGRES_DB=postgres
   POSTGRES_USER=odoo17
   ```
2. In project root directory create `odoo_pg_pass` file. It should have password as a value:
   ```pan
   mytest
   ```
3. In project `config` directory create `odoo.conf` file. Example:
   ```pan
   [options]
   ; This is the password that allows database operations:
   admin_passwd = myodoo
   db_host = db
   db_port = 5432
   db_user = odoo17
   db_password = mytest
   addons_path = /mnt/extra-addons,
   
   limit_time_cpu = 3600
   limit_time_real = 3600
   limit_time_real_cron = 3600
   
   workers = 9
   max_cron_threads = 2
   
   limit_memory_soft = 6039797760
   limit_memory_hard = 7247757312
   ```
4. Run Odoo 17
   ```sh
   docker-compose up -d
   ```

## Odoo configuration
Before using "sale_order_line_multiple_warehouse" module you need to configure Odoo.

 1. Create multiple warehouses.
![1](https://github.com/JobTasks/Umina-task-2023/assets/40775067/0620a482-23ad-4038-b8ba-408edf514f62)

 2. Create some products and make them storable type.
![2](https://github.com/JobTasks/Umina-task-2023/assets/40775067/7bb00307-826a-4f6b-bc94-66a1c608987f)

## Module usage
 1. Create Sale order. Add multiple order lines with different warehouses.
![SO](https://github.com/JobTasks/Umina-task-2023/assets/40775067/9def1f41-1f88-4b78-bec0-564c785fe640)

 2. Confirm sale order. Multiple deliveries are created depending on sale order lines warehouses.
![3](https://github.com/JobTasks/Umina-task-2023/assets/40775067/f8c9beb3-d9ef-4383-9c35-00341207f417)

 3. Products are grouped in deliveries by warehouses.
![5](https://github.com/JobTasks/Umina-task-2023/assets/40775067/31e6c906-6c82-4bc3-853f-595520706e2f)
![4](https://github.com/JobTasks/Umina-task-2023/assets/40775067/727c2454-6331-4bd0-8321-e535d9866040)
 5. Forecasted report is opened for specific warehouse chosen in sale order line.
![6](https://github.com/JobTasks/Umina-task-2023/assets/40775067/7ad201f1-8437-4031-ba60-b9eb6c37fae3)


 


## Improvements

1. Check if new features haven't broken standard Odoo tests.
2. Write Unit tests for new features.
3. Ensure that the forecasted pop-up window shows data for the chosen warehouse (opened report works correctly)


