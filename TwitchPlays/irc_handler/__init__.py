import sys
import socket
import string

from TwitchPlays.config import CHANNEL
from TwitchPlays.config import HOST
from TwitchPlays.config import PORT
from TwitchPlays.config import TOKEN
from TwitchPlays.config import NICK
from TwitchPlays.config import IDENT
from TwitchPlays.config import REALNAME

def irc_controller(game_controller):
    readbuffer=""

    s=socket.socket( )
    s.connect((HOST, PORT))
    s.send("PASS %s\r\n" % TOKEN)
    s.send("NICK %s\r\n" % NICK)
    s.send("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME))
    s.send("JOIN %s\r\n" % CHANNEL)

    while 1:
        readbuffer=readbuffer+s.recv(1024)
        temp=string.split(readbuffer, "\n")
        readbuffer=temp.pop( )

        for line in temp:
            line=string.rstrip(line)
            line=string.split(line)

            game_controller(line)

            if(line[0]=="PING"):
                s.send("PONG %s\r\n" % line[1])
