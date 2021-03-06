# Couchbase Docker Lab

# CASE 1 

# Purpose

Creating a distributed couchbase cluster consisting of 2 nodes

Lab environment on below



| VM name       |   Role                             | OS      |  Networking     | 
| ------------- |   :-------------:                  | -----:  | -----:          |
| control       |   Couchbase Node1/Node2            | centos  | 192.168.135.148 |

All applications run on the virtual machine as a container.

# Prerequisites

    Vagrant        2.2.15 
    Virtualbox     6.1.18 
    Docker         20.10.6
    Docker-compose 1.25
 
# Installation

vm creating

``` bat  
$ git clone https://github.com/nzncngz/database.git
$ cd database; vagrant up &
 ```
 
Our goal is to install a couchbase cluster with 2 nodes. Both nodes will be created as containers via docker compose.

``` bat  
$ sudo usermod -aG docker vagrant; docker-compose -f docker-compose.yml up & 
 ```

A new cluster will be created on below and then the 2 nodes will be added to the cluster.

![Vertical](https://user-images.githubusercontent.com/22845579/116284591-ec382400-a795-11eb-8570-33474ecb6d6f.png)

Adding the second node cluster

![Vertical](https://user-images.githubusercontent.com/22845579/116288871-9ca82700-a79a-11eb-9a2d-dad8a46f812f.png)


Performing balance transaction between nodes

![Vertical](https://user-images.githubusercontent.com/22845579/116288693-708ca600-a79a-11eb-8374-76f5ee552049.png)





# CASE 2

# Purpose

Realization of the request, which receives the cluster information on the database, as a module with the python api

# Installation

Login centos vm then run python script with vagrant

``` bat
$ python test.py
 ```

Result test.py on below

![Vertical](https://user-images.githubusercontent.com/22845579/116431205-3bdb2600-a850-11eb-8347-79a48c5a86c5.png)


# Reference

https://docs.couchbase.com/server/current/rest-api/rest-views-get.html

 

 
