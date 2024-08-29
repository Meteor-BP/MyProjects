from ursinanetworking import *

Server = UrsinaNetworkingServer("localhost", 25565)

@Server.event
def changeName(client, new_name):
    client.name = new_name
    Server.broadcast("messageReceveid", f"{client.name} подключился к игре !")
    print(f"{client.name} подключился к игре !")


@Server.event
def onClientDisconnected(client):
    Server.broadcast("messageReceveid", f"{client.name} отключился !")
    print(f"{client.name} отключился !")

@Server.event
def message(client, message):
    Server.broadcast("messageReceveid", f"{client.name} : {message}")
    
while True:
    Server.process_net_events()