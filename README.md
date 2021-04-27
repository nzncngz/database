# Couchbase Docker Lab

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
$ docker-compose -f docker-compose.yml up & 
 ```

A new cluster will be created on below and then the 2nd node will be added to the cluster.

![Vertical](https://user-images.githubusercontent.com/22845579/116284591-ec382400-a795-11eb-8570-33474ecb6d6f.png)


# Reference

https://docs.couchbase.com/server/current/rest-api/rest-views-get.html

 

 
