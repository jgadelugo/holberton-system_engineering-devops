# puppet code - use strace to find out why apache is returning a 500 error

exec { 'fix_500_erri':
  command => "/bin/sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
}
