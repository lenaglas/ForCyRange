FROM ubuntu:20.04
COPY ./start.sh ./start.sh
RUN apt-get update
RUN apt-get install -y sudo 
RUN apt-get install -y screen 
RUN apt-get install -y python3.8 
RUN apt-get install -y python3-pip 
RUN apt-get install -y build-essential
RUN apt-get install -y iputils-ping 
RUN apt-get install -y net-tools 
RUN apt-get install -y git
RUN apt-get install -y screen 
RUN apt-get -y install syslog-ng 
RUN git clone git://github.com/mininet/mininet 
RUN /mininet/util/install.sh -a 
RUN git clone https://github.com/nowsecure/fsmon.git 
WORKDIR /fsmon
RUN pwd
RUN make install
WORKDIR ..
RUN pwd
RUN chmod +x ./start.sh

   
CMD ["./start.sh"]

