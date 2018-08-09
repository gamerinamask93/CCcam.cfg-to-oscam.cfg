import os
print "####################################################################"
print "welcome to the"
print "AUTOMATED FREE OSCAM SCRIPT"
print "V0.1                                      Written By Antony"
print "####################################################################"
print " "
print "THIS SCRIPT IS AN AUTOMATIC CONVERTER FOR CCcam.cfg to oscam.server"
print " "
print "NOTE: this script needs a dummy oscam.server to start so just make"
print "      a blank file called oscam.server in same DIR as this"
print " "
print "NOTE 2: Use this AFTER a new CCcam.cfg has been generated"
print "===================================================================="
print "removing oscam.server"
os.remove("oscam.server")
print "removed oscam.server"
print "parsing CCcam.cfg"
f = open('CCcam.cfg')
print "reading and writing a new oscam.server file"
for line in f:
    domain = line.split(' ')[1]
    port = line.split(' ')[2]
    user = line.split(' ')[3]
    password = line.split(' ')[4]
   #print(domain,port,user,password)
    server = open("oscam.server","a")
    server.write("[reader]\n")
    label = ("label=")
    domain1 = label+domain
    server.write(domain1)
    server.write('\n')
    server.write("enable=1\n")
    server.write("protocol=cccam\n")
    device = ("device=")
    comma = (",")
    device1 = device+domain+comma+port
    server.write(device1)
    server.write('\n')
    user1 = ("user=")
    user2 = user1+user
    server.write(user2)
    server.write('\n')
    pwd = ("password=")
    pwd1 = pwd+password
    server.write(pwd1)
    server.write("cccversion=2.1.2\n")
    server.write("group=1\n")
    server.write("inactivitytimeout=1\n")
    server.write("reconnecttimeout=20\n")
    server.write("lb_weight=100\n")
    server.write("cccmaxhops=10\n")
    server.write("ccckeepalive=1\n")
    server.write("cccwantemu=0\n")
    server.write('\n')
    server.close()
    print "+1"
print "Process Complete"
