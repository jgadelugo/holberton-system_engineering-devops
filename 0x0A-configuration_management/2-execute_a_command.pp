# kill process
exec {'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
  creates  => '/killmenow',
  path     => '/usr/bin',
}
