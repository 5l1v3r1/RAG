# RAG
  RAG is a custom tool designed to create custom reverse shells in a matter of seconds, it allows for user customization to create quick and powerfull shells straight off the get go. 
![How A Normal Shell Works](https://github.com/backslash/RAG/blob/master/Reverse-Shell-illustration.png)
  
 ## Setup
  Setting up RAG is as easy as can be. First off you can either download rag by running setup.py or you can do it by installing each module through the requirements.txt
  ```
  python setup.py install
  ```
  or
  ```
  pip install requirements.txt
  ```
  Once you have gotten all the modules installed open up settings.ini
  ```
[Ip] = 127.0.0.1
[Port] = 80
[StartupPersistance] = TRUE
[FileName] = malware
[StartupTime] = 5
```
You will see something that looks like this:
IP = The target ip you want to connect to.
PORT = Which port you want it to go through
StartupPersitance = Would you like it to be added to the startup menu.
FileName = The name that you want of the file
StartupTime = How long the file should take for bootup (This is to help it avoid av)

## Server
  Once you have generated your shell you can open up your server.py this contains the ability to send commands to the target host once its connected. Warning though it is pre configured to go through port 80. If you dont want it using port 80 just go inside the file and change the value of port.
  
  ## To Do List
  - [ ] Add multiple connections to the server
  - [ ] Add a larger range of configurable options
  - [ ] Make the UI slighly better.

  ## Disclaimer 
    I am not responsible for how you choose to use RAG. This is a hacking tool for read teamers or just people interested in the functionality of reverse shells. I am not responsible for your choices.
