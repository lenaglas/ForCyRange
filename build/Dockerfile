FROM ubuntu:20.04
COPY ./start.sh ./start.sh
RUN apt-get update
RUN apt-get install -y sudo \
    && apt-get install -y python3.8 \
    && apt-get install -y python3-pip \
    && apt-get install -y iputils-ping \
    && apt-get install -y net-tools \
    && apt-get install -y git \ 
    && apt-get install -y screen \
    && git clone git://github.com/mininet/mininet \
    && /mininet/util/install.sh -a \
    && git clone https://github.com/nowsecure/fsmon.git \
    && /fsmon/make install 

   
CMD ["./start.sh"]


