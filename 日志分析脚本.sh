#!/bin/bash
file=$1;
echo "---------------------------------- 文件信息 ----------------------------------";
echo  "日志文件: $file";
file_size=$(stat -c %s $file);
echo "文件大小: $file_size 字节"
#IP列
ip_count=$(cat $file | awk {'print $1'}|sort|uniq|wc -l)
echo "请求IP: $ip_count 个"
#URL列
request_url=$(cat $file| awk {'print $8'}|sort|uniq|wc -l)
echo "请求URL: $request_url 个";

function IP_GET_URL(){
#IP列
 ip=$(cat $file | awk {'print $1'}|sort|uniq)
 
 for i in $ip
 
 do
    echo -e "===============================\033[32m IP: $i \033[0m===============================";
    echo "访问次数 响应状态码 响应长度 请求URL";
    #状态码、响应长度、请求URL
    cat $file  |grep $i|awk {'print $10,$11,$8'}|grep -v '\.js$'|grep -v '\.css$'|sort|uniq -c|sort -nr
    echo ""
 done
}


function IP_request_count(){
   cut -d- -f 1 $file|sort|uniq -c | sort -rn |uniq
}


function Statistics_network_segment(){
   #IP列
   cat $file | awk '{print $1}' | awk -F'.' '{print $1"."$2"."$3".0/24"}' | sort | uniq -c | sort -rn|uniq

}
#状态码
function status_code(){
   cat $file | awk '{print $10}'|sort|uniq -c|sort -rn

}
#请求URL
function URL_request_count(){
   cat $file  |awk '{print $8}'|sort|uniq -c|sort -rn|uniq

}
#请求类型
function Request_type_count(){
   cat $file | awk '{print $7}'|sort|uniq -c|sort -rn
}

#请求URL
function Request_type_count_parm(){

   cat $file |  awk '{print $8}' | egrep '\?|&' | sort | uniq -c | sort -rn|uniq

}

#返回长度、请求URL
function response_length(){
   cat $file |awk '{print $11,$8}'|grep -v '\.js'|grep -v '\.css' | sort -rn |uniq

}

echo "---------------------------------- 状态码统计 ----------------------------------";
status_code

echo "---------------------------------- 请求类型统计 ----------------------------------";
Request_type_count

echo "---------------------------------- 响应长度 ----------------------------------";
response_length

echo "---------------------------------- IP访问次数 ----------------------------------";
IP_request_count



echo "---------------------------------- 网段统计 ----------------------------------";
Statistics_network_segment



echo "---------------------------------- URL访问量统计 ----------------------------------";
URL_request_count



echo "---------------------------------- 带参数的URL访问量统计 ----------------------------------";
Request_type_count_parm


echo "---------------------------------- 每个IP访问的URL(去除js和css文件) ----------------------------------";
IP_GET_URL
