# Configures a web server for deployment of a sample static website.

# Custom Nginx configuration file
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;

    location /sample_static {
        alias /data/sample_web_static;
        index index.html index.htm;
    }

    location /redirect_example {
        return 301 http://example.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

# Ensure Nginx package is installed
package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
} ->

# Create necessary directories
file { '/data':
  ensure  => 'directory'
} ->

file { '/data/sample_web_static':
  ensure => 'directory'
} ->

file { '/var/www/html':
  ensure => 'directory'
} ->

# Create sample index.html file
file { '/data/sample_web_static/index.html':
  ensure  => 'present',
  content => "Welcome to my sample static website!\n"
} ->

# Create Nginx configuration file
file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
} ->

# Restart Nginx service
exec { 'nginx restart':
  path => '/etc/init.d/'
}
