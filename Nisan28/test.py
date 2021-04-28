import requests
from requests.auth import HTTPBasicAuth
import json


class Couchbase:
    def __init__(self, clusterName, indexMemoryQuota, balanced, nodes, eventingMemoryQuota, ramTotal, hddTotal ):
        self.clusterName = clusterName
        self.indexMemoryQuota = indexMemoryQuota
        self.balanced = balanced
        self.nodes = nodes
        self.eventingMemoryQuota = eventingMemoryQuota
        self.ramTotal = ramTotal
        self.hddTotal = hddTotal



class Manage:
    def __init__(self, ip, port, username, password):
        self.ip=ip
        self.port=port
        self.username=username
        self.password=password
    
    def getCluster(self):
        url="http://"+self.ip+":"+self.port+"/pools/default"
        print(url)
        response = requests.get(url, auth=HTTPBasicAuth(self.username, self.password))
        clusters = response.json()
        nodelist=[]         
        for i in clusters["nodes"]:
             nodelist.append(i['hostname'])
        return Couchbase(clusters["clusterName"], clusters["indexMemoryQuota"], clusters["balanced"], nodelist, clusters["eventingMemoryQuota"], clusters["storageTotals"]["ram"]["total"],clusters["storageTotals"]["hdd"]["total"])
        

user=Manage("192.168.135.148", "8094", "Administrator", "123123")
print(user.ip,user.username,user.password)
cluster=user.getCluster()
print(cluster.clusterName,cluster.indexMemoryQuota,cluster.balanced,cluster.nodes,cluster.eventingMemoryQuota,cluster.ramTotal,cluster.hddTotal)
