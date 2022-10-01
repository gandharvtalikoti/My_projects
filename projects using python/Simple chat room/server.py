import socket
import threading

# Connection Data
HOST = "127.0.0.1"
PORT = 9090


'''
These define the type of socket we want to use. 
The first one (AF_INET) indicates that we are using an internet socket rather than an unix socket. 
The second parameter stands for the protocol we want to use. 
SOCK_STREAM indicates that we are using TCP and 
not UDP.
'''

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

# We then put our server into listening mode, so that it waits for clients to connect.
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = [] # list of nicknames


# broadcast
'''Sending Messages To All Connected Clients'''
'''
Here we define a little function that is going to help us broadcasting messages and makes 
the code more readable. What it does is just sending a message to each client that is connected and therefore in the clients list. 
We will use this method in the other methods.
'''
def broadcast(message):
    for client in clients:
        client.send(message)


# recieve
# Receiving / Listening Function
def receive():
    while True:
        # Accept new Connections
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request And Store Nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024)

        if nickname in nicknames:
            # print("client already there")
            client.send('Already there'.encode('utf-8'))

        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined!\n".encode('utf-8'))
        client.send('Connected to server!\n'.encode('utf-8'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


# handle

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left!'.encode('ascii'))
            nicknames.remove(nickname)
            break

print("server running!")
receive()
