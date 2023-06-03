## What is this ?
- A sample application that has ORM support for User Models, can does CRUD ops on top on a SQL type DB, postgres support is included in the box but you can use anything you want 


## Why this ? 
- A lot of interviews would ask you to create a full stack DB application that has these components. 
- A DB [State Support; Push the application state in form of pojos to tables]
- A Controller [HTTP Server; Support HTTP Protocol and push out a bunch of APIs using json in request/response flows]
- A Auth Token Manager [A simple JWT type thingy would work out of box here !]
- Some custom business Logic 
        
        - [Maybe support a zerodha type investment ledger and support ROI calculation and TOTAL_PORTFOLIO calculation at any time X]
        
        - [Maybe a custom ticker manager; give out train/parking tickets]
        
        - [Some Random Problem]


## HLD
![HLD_IMAGE](./images/hld.png)

## How does this help ?
- The auth module takes care of /signup and /login flow with auth_token [Authorisation : Bearer <AUTH_TOKEN>] type support.

- Writing custom business logic becomes easier from here on. 

- You have to design DataBase Tables for your custom business logic, and a LLD and HLD diagrams.

- Add business logic modules inside src/* as individual building blocks and then just include the router inside src/server. 

## How to run ? 
- Make sure docker-compose in installed and docker-daemon in running. Read Docker is you are a noobie !

- run `docker-compose -f dev/docker-compose-dev.yml build` and `docker-compose -f dev/docker-compose-dev.yml up`

- goto : localhost:8890/docs to test out the APIs


## RoadMap 
- 1. Adding support for Tests; inside tests/
- 2. Solve a problem on top of this


 





