<?php
if (isset($_POST['modo'])) {
$txt = $_POST['modo'];
}
if (isset($_POST['id'])) {
$id = $_POST['id'];
  if ($id!='nada'){
    shell_exec("sudo /usr/bin/python /var/www/html/main.py -sqlAdd $id > /dev/null 2>&1 & echo $!");
  }
}
$myfile = fopen("modo.txt", "w");
fwrite($myfile, $txt);
fclose($myfile);
?>
