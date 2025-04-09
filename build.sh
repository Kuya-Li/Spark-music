#!/bin/sh
if [ "$1" = "build" ];then
    mkdir /home/changsheng/project/project83363/project
    cp -a /home/changsheng/project/project83363/server/. /home/changsheng/project/project83363/project/
    cd /home/changsheng/project/project83363/project
    rm -rf /home/changsheng/project/project83363/server
    echo "执行成功"
fi
