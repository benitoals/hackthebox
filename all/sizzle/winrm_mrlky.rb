require 'winrm'
opts = { 
  endpoint: 'http://10.10.10.103:5985/wsman',
  user: 'mrlky',
  password: 'Football#7'
}
conn = WinRM::Connection.new(opts)
conn.shell(:powershell) do |shell|
  output = shell.run('$PSVersionTable') do |stdout, stderr|
    STDOUT.print stdout
    STDERR.print stderr
  end
  puts "The script exited with exit code #{output.exitcode}"
end
