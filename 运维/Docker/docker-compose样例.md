## docker-compose样例

```
version: "3.6"
services:
  postgres:
    image: postgres
    container_name: postgres
    restart: always
    environment:
      # POSTGRES_DB: db_name
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    ports:
        - 5432:5432
    volumes:
      # - /data/postgresql:/var/lib/postgresql/data
      - /srv/postgresql:/var/lib/postgresql/data

  etcd:
    image: quay.io/coreos/etcd:latest
    container_name: etcd
    restart: always
    ports:
      - 2379:2379
      - 2380:2380
    volumes: 
      # - /srv/docker/etcd:/etcd-data
      - /srv/etcd:/etcd-data 
    environment:
      ETCD_NAME: node1
      ETCD_DATA_DIR: /etcd-data/node1.etcd
      ETCD_INITIAL_ADVERTISE_PEER_URLS: http://127.0.0.1:2380
      ETCD_INITIAL_CLUSTER: node1=http://127.0.0.1:2380
      ETCD_LISTEN_CLIENT_URLS: http://0.0.0.0:2379
      ETCD_LISTEN_PEER_URLS: http://127.0.0.1:2380
      ETCD_ADVERTISE_CLIENT_URLS: http://127.0.0.1:2379

  nsqlookupd:
    image: nsqio/nsq
    command: /nsqlookupd
    ports:
      - "4160:4160"
      - "4161:4161"

  nsqd:
    image: nsqio/nsq
    command: /nsqd -data-path=/data --lookupd-tcp-address=nsqlookupd:4160
    volumes:
      - /srv/nsq:/data
    depends_on:
      - nsqlookupd
    ports:
      - "4150:4150"
      - "4151:4151"

  nsqadmin:
    image: nsqio/nsq
    command: /nsqadmin --lookupd-http-address=nsqlookupd:4161
    depends_on:
      - nsqlookupd  
    ports:
      - "4171:4171"

  envoy:
    image: envoyproxy/envoy:latest
    container_name: envoy 
    volumes: 
      - /Usrv/envoy:/etc/envoy
    ports: 
      - "9901:9901"
      - "10000:10000"
      - "8080:8080"

  nginx:
    image: nginx:latest
    container_name: nginx 
    restart: always
    volumes: 
      - /srv/nginx/etc/nginx/conf.d:/etc/nginx/conf.d
      - /srv/nginx/etc/letsencrypt:/etc/letsencrypt
      - /srv/nginx/var/log/nginx:/var/log/nginx
      # - /srv/nginx/var/www:/var/www
    ports: 
      - "80:80"
      - "443:443"
```
