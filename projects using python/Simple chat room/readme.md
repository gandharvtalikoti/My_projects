

Implementing The Server
Now let’s start by implementing the server first. For this we will need to import two libraries, namely socket and threading. The first one will be used for the network connection and the second one is necessary for performing various tasks at the same time.

import socket
import threading
The next task is to define our connection data and to initialize our socket. We will need an IP-address for the host and a free port number for our server. In this example, we will use the localhost address (127.0.0.1) and the port 55555. The port is actually irrelevant but you have to make sure that the port you are using is free and not reserved. If you are running this script on an actual server, specify the IP-address of the server as the host. Check out this list of reserved port numbers for more information.

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
When we define our socket, we need to pass two parameters. These define the type of socket we want to use. The first one (AF_INET) indicates that we are using an internet socket rather than an unix socket. The second parameter stands for the protocol we want to use. SOCK_STREAM indicates that we are using TCP and not UDP.

After defining the socket, we bind it to our host and the specified port by passing a tuple that contains both values. We then put our server into listening mode, so that it waits for clients to connect. At the end we create two empty lists, which we will use to store the connected clients and their nicknames later on.

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)
Here we define a little function that is going to help us broadcasting messages and makes the code more readable. What it does is just sending a message to each client that is connected and therefore in the clients list. We will use this method in the other methods.

Now we will start with the implementation of the first major function. This function will be responsible for handling messages from the clients.

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
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break
As you can see, this function is running in a while-loop. It won’t stop unless there is an exception because of something that went wrong. The function accepts a client as a parameter. Everytime a client connects to our server we run this function for it and it starts an endless loop.

What it then does is receiving the message from the client (if he sends any) and broadcasting it to all connected clients. So when one client sends a message, everyone else can see this message. Now if for some reason there is an error with the connection to this client, we remove it and its nickname, close the connection and broadcast that this client has left the chat. After that we break the loop and this thread comes to an end. Quite simple. We are almost done with the server but we need one final function.

# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
When we are ready to run our server, we will execute this receive function. It also starts an endless while-loop which constantly accepts new connections from clients. Once a client is connected it sends the string ‘NICK’ to it, which will tell the client that its nickname is requested. After that it waits for a response (which hopefully contains the nickname) and appends the client with the respective nickname to the lists. After that, we print and broadcast this information. Finally, we start a new thread that runs the previously implemented handling function for this particular client. Now we can just run this function and our server is done.

Notice that we are always encoding and decoding the messages here. The reason for this is that we can only send bytes and not strings. So we always need to encode messages (for example using ASCII), when we send them and decode them, when we receive them.

receive()
Implementing The Client
A server is pretty useless without clients that connect to it. So now we are going to implement our client. For this, we will again need to import the same libraries. Notice that this is now a second separate script.

import socket
import threading
The first steps of the client are to choose a nickname and to connect to our server. We will need to know the exact address and the port at which our server is running.

# Choosing Nickname
nickname = input("Choose your nickname: ")

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
As you can see, we are using a different function here. Instead of binding the data and listening, we are connecting to an existing server.

Now, a client needs to have two threads that are running at the same time. The first one will constantly receive data from the server and the second one will send our own messages to the server. So we will need two functions here. Let’s start with the receiving part.

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break
Again we have an endless while-loop here. It constantly tries to receive messages and to print them onto the screen. If the message is ‘NICK’ however, it doesn’t print it but it sends its nickname to the server. In case there is some error, we close the connection and break the loop. Now we just need a function for sending messages and we are almost done.

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))
The writing function is quite a short one. It also runs in an endless loop which is always waiting for an input from the user. Once it gets some, it combines it with the nickname and sends it to the server. That’s it. The last thing we need to do is to start two threads that run these two functions.

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
And now we are done. We have a fully-functioning server and working clients that can connect to it and communicate with each other. 

Running The Chat
Let’s go for a test run. Just keep in mind that we always need to start the server first because otherwise the clients can’t connect to a non-existing host. Here you can see an example of a chat with two clients (you can also connect with 20 if you want):

