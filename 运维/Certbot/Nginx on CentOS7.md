## Nginx on CentOS7

#### Install

> $ yum -y install yum-utils

> $ yum-config-manager --enable rhui-REGION-rhel-server-extras rhui-REGION-rhel-server-optional


> $ sudo yum install certbot python2-certbot-nginx

#### Get Started
> $ sudo certbot --nginx

#### Automating renewal

> $ sudo certbot renew --dry-run

> $ certbot renew

#### Cron
`
0 0,12 * * * python -c 'import random; import time; time.sleep(random.random() * 3600)' && certbot renew
`