# puppet code - use strace to find out why apache is returning a 500 error

exec { 'fix_error':
  command => "/bin/sed -i 's/15/4096/g' /etc/default/nginx; ; sudo service nginx restart",
}
