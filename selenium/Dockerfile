FROM centos

RUN yum update -y
RUN yum install -y epel-release
RUN yum install -y \
    firefox \
    fvwm \
    ipa-{,p}gothic-fonts \
    ipa-{,p}mincho-fonts \
    java-1.8.0-openjdk \
    python-pip \
    tigervnc-server \
    xorg-x11-server-Xvfb \
    xwd \
    netpbm-progs
RUN pip install --upgrade pip
RUN pip install -U selenium
RUN systemd-machine-id-setup
RUN mkdir $HOME/.vnc

COPY selenium-server-standalone-3.6.0.jar /root
COPY geckodriver /root
COPY passwd /root/.vnc/passwd
COPY sample.py /root/sample.py
COPY seleniumUtil.py /root/seleniumUtil.py
COPY script.sh /root/script.sh

WORKDIR /root

ENV LANG ja_JP.UTF-8

CMD /root/script.sh
