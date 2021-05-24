# Parallel_HPC_Server(Pynoco)

## Introduction
The server manager manage the flow of information between the server and an endpoint device (PC, laptop, tablet or smartphone).
The server could be on-premises, in a data center or the public cloud
Distributing high traffic sites among several servers
The manager decides which servers can handle that traffic

## Problem Statement
In current tech world there is a need of parallel job to do its application level load balancing while ensuring that system load is balanced.
Change of destination decision algorithm during runtime is a challenging task in a load balancer. we mostly have to stop the load balancer which reults in packet loss and considerable time lapse. 

## Solution
- Separate Process Creation for each listener
- Listeners are defined in our Config File
- Listener creates sub-process to route the request to the destination
- You can change Algorithm on runtime by sending a Http Post Request 

## Advantages
- Reduced Downtime
- Scalable
- Redundancy
- Flexibility

## Algorithms Used
- Round-robin
- Weighted

## To run file:
- Go inside Python Load Balancer directory:
  - run `python3 setup.py build`
  - run `python3 PynocoLB.py serverconfig.cfg`

- Start Servers:
  - cd server1 and run `npm start `
  - cd server2 and run `npm start`

## To Change LoadBalancing Algorithm 
Send Post Request like this to **127.0.0.1:9090**

`{ "servers":[ {"addr":"127.0.0.1", "port":8001}, {"addr":"127.0.0.1", "port":8001}, {"addr":"127.0.0.1", "port":5000}] }`

## Conclusion
  
- Successful creation of a dynamic load balancer using HTTP Post Server
- Providing each listener a specific process helped to increase the efficiency of load balancer
- Dynamic changing of runtime algorithm achieved which helped in reducing the packet loss which was a major concern.  


