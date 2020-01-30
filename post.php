//code by it4min
//itLocation v2
//t.me/LinuxH
<?php
$json = (file_get_contents('php://input'));
$dejson = json_decode($json, true);
$location = $dejson['data'];
shell_exec("python3 send.py ".$location);
?>

