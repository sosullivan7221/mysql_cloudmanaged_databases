# mysql_cloudmanaged_databases
MySQL instances for Azure and GCP

Note: I did not take a screenshot showing the tables being successfully created, however, the screenshot shows that I was unable to create the same table in the database since the table already exists.

## Azure Config Setup

Resource Type: Azure Database for MySQL: Flexible Server
1. Select Resource Group and name your server
2. Create an admin username and password to login to MySQL Workbench
3. Allow public access to the database through a public IP. Azure has a button to quick add 0.0.0.0 as an address.
4. Submit and wait for the instance to be created.

## GCP Config Setup

Resource Type: MySQL
1. Create instance ID and password. Select Enterprise and Sandbox as the CloudSQL edition
2. Use a single shared CPU with 0.614GB of RAM
3. Create a public access route using the IP address 0.0.0.0/0
4. Select 10GB of storage
5. Submit and wait for the instance to be created.

## Using MySQL Workbench

The interface for MySQL is familiar since it's structured similar to other IDEs. However, going in to use it for the first time can be intimidating because there are a lot of settings and tabs to use potentially. Going through it in class helped me feel more comfortable using it.

## Connecting to Python

-Attempted to connect to Python using both the GCP and Azure instances. Encountered two exceptions when running the .py file in this repository:

sqlalchemy.exc.OperationalError: (pymysql.err.OperationalError) (2003, "Can't connect to MySQL server on 'None' ([Errno -2] Name or service not known)")
(Background on this error at: https://sqlalche.me/e/20/e3q8)

for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -2] Name or service not known

-It seems there might be some issue with the credentials but I checked both my instances and didn't see any issues, so I am currently unsure how to approach this issue. I will continue to look into it.
