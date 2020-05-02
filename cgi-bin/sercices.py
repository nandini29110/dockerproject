import os
os.system("tput setaf 1")
print("\t\t HEY!!! welcome to docker services")
os.system("systemctl start docker")
print("\t\tDocker services are started make and launch your oun container")
os.system("tput setaf 7")
while(1):
    name = input("ENter name of your container:")
    image = int(input("select image - \n 1. centos:7 \n 2. centos:latest \n 3. ubuntu:14.7 \n 4. mysql:5.7"))
    network = input("""Enter network name:""")
    print("""choose a network:\n1: Bridge \n2: Host\n3: NUll""")
    n=int(input())
    if n==1:
         net_driver = 'bridge'
    elif n == 2:
         net_driver = 'host'
    elif n == 3:
         nrt_driver = 'null'

    os.system("docker network create {0} --driver {1}".format(network,net_driver ))

    print("\n\n---Do you want to allot any centralized volume to your container for storage?   , if yes press y :")
    s = input()
    if s == 'y':
        storage = input("enter name of storage:")
        os.system("docker volume create {}".format(storage))
    

    

    if image == 1:
        os.system("docker container run --network {0} -v {2}:/var/www/html --name {1} centos:7".format(network,name,storage))
        print("your container has been launched, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker images")
 
    elif image == 2:
        os.system("docker container run --network {0} -v {2}:/var/www/html --name {1} centos:7".format(network,name,storage))
        print("your container has been launched, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker images")

    elif image == 3:
        os.system("docker container run --network {0} -v {2}:/var/www/html --name {1} centos:7".format(network,name,storage))
        print("your container has been launched, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker images")

    elif image == 4:
        print("MYSQL IMAGE NEEDS ENVIRONMANTAL VARAIBLES\n FILL UP FOLLOWING ENTRY :-\n ")
        Mysql_Root_password = input("Mysql root password:")
        Mysql_user= input("Mysql user:")
        Mysql_password = input("Mysql password:")
        Mysql_database = input("Mysql Database:")
        os.system("docker container run -e MYSQL_ROOT_PASSWORD = {0} -e MYSQL_USER = {1} -e MYSQL_PASSWORD = {2} -e MYSQL_DATABASE = {3} --network {4} -v {6}:/var/www/html --name {5} centos:7".format(Mysql_Root_password,Mysql_user,Mysql_password,Mysql_database,network,name,storage))



        print("your container has been launched, to verify press 1: , unless press:0")
        x=int(input())
        if x==1:
            os.system("docker container ls")
    print("\n\n\t\t\twant to launch more container: press Y or N \n\n")
    y=input()
    if y == "Y":
        pass
    else:
      break
    
print("""n\n-------------------------------------------------------
        os.system("tput setaf 1")
        \t\t\t SERVICES INSIDE YOUR CONTAINER
        \n\n
        select option:
        1. Information about your container
        2. launch a web server inside the container
        5: ping to any site
        6: Exit forom here?


        """)
q = int(input())
if q ==1 :
    os.system("docker container inspect {}".format(name))
elif q==2:
    os.system("docker start {}".format(name))
    os.system("docker attach {}".format(name))
    os.system("docker exec {} yum install httpd".format(name))
    os.system("pwd")

