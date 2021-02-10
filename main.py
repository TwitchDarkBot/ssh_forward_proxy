from multiprocessing import Process
import json
#import logging

def process(config):
    from os import system
    ip = config["ip"]
    port = config["port"]
    login = config["login"]
    id_rsa = config["id_rsa"]
    password = config["password"]
    local_port = config["local_port"]
    forward_port = config["forward_port"]


    system("ssh -L {lport}:127.0.0.1:{fport} {ip} -p {port} -l {user} -i {id_rsa}".format(lport=local_port,fport=forward_port,ip=ip,port=port,user=login,id_rsa=id_))


    pass

def main():
    pass


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit()
    pass