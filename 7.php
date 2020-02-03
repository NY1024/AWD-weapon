//记录访问痕迹
<?php
date_default_timezone_set('Asia/Shanghai');//设定默认时区
$ip = $_SERVER["REMOTE_ADDR"]; //ip
$filename = $_SERVER["PHP_SELF"]; //PHP_SELF 当前执行脚本的文件名
$parameter = $_SERVER["QUERY_STRING"];//查询的字符串，即payload
$time = date('Y-m-d H:i:s',time());
$logadd  = '时间:'.$time.'-->'.'访问连接:'.'http://'.$ip.$filename.'?'.$parameter."\r\n";

//写入文件
$fh = fopen("log.txt","a");
fwrite($fh,$logadd);
fclose($fh);
?>
