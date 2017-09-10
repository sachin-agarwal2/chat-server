import socket
import thread
import sys
conn_list=[]
add_list=[]
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
def utility():
    print("\n")
    print("   command                        : functions")
    print("1) show                           : show all clients")
    print("2) msg_all                        : broadcast msg")
    print("3) reply                          : reply to any client")
    print("4) disconnect                     : disconnect client")
    print("5) quit                           : close socket")
def show():
    for i in range(0,len(add_list)):
        print str(i+1)+") ip address"+str(add_list[i][0])+" at port"+str(add_list[i][1])
def msg_all():
    m=raw_input("broadcast messege")
    for i in range(0,len(add_list)):
        conn_list[i].sendall(m)
def reply(cmd):
    no=cmd[6:]
    no=no-1
    msg=raw_input("msg for"+str(add_list[no][0])+"port"+str(add_list[no][1]))
    conn_list[no].sendall(msg)
def disconnect(cmd):
    no=cmd[11:]
    no=no-1
    conn_list[no].close()
    conn_list.pop[no]
    add_list.pop[no]
def quit_all():
    for i in range(0,len(add_list)):
        conn_list[i].close()
        conn_list.pop[i]
        add_list.pop(i)
    s.shutdown()
    s.close()
    sys.exit()
def response():
    while 1:
        cmd=raw_input('')
        if "show" in cmd:
            show()
        elif "msg_all" in cmd:
            msg_all()
        elif "reply" in cmd:
            reply(cmd)
        elif "disconnect" in cmd:
            disconnect(cmd)
        elif "quit" in cmd:
            quit_all()
        else:
            utility()
def chat(conn,addr):
    while 1:
        m=conn.recv(1024)
        if len(m)<1:
             break
        print "msg from ip"+str(addr[0])+"at port"+str(addr[1])+m
        buff=buff+m
        st="msg from ip"+str(addr[0])+"at port"+str(addr[1])+buff
        for b in range(0,len(add_list)):
            if add_list[b] is not addr:
                conn_list[b].send(st)
    b=add_list.index(addr)
    conn.close()
    conn_list.pop(b)
    add_list.pop(b)
host=''
port=9999
print " binding socket"
try:
    s.bind((host,port))
except:
    print "error in binding"
    sys.exit()
print "listening for socket"
s.listen(10)
print("accepting connection")
utility()
thread.start_new_thread(response,())
while 1:
    conn,add=s.accept()
    conn_list.append(conn)
    add_list.append(add)
    print("connected to"+str(add[0])+"port:"+str(add[1]))
    thread.start_new_thread(chat,(conn,add))

sts.exit()
s.close()