#fix os error change config
exec { 'change_config':
  command => "sudo /bin/sed -i 's/nofile 4/nofile 6000/g; s/nofile 5/nofile 6000/g' /etc/security/limits.conf",
}

