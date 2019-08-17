# nebula
## docker-compose
  ```
  micro-web:
    command: --registry=etcdv3 --registry_address=etcd:2379 web
    image: registry.cn-beijing.aliyuncs.com/wall-js/micro:1.0.0
    ports:
      - "8082:8082"

  com.tradeany.api:
    command: --registry=etcdv3 --registry_address=etcd:2379 api --handler=web --namespace=com.tradeany.api
    image: hregistry.cn-beijing.aliyuncs.com/tradeany/tradeany-api-supplier:0.0.1
    links:
      - etcd
    ports:
      - "8080:8080"

  tradeany-api-supplier:
    image: nebula:latest
    volumes: 
      - /Users/zuoyi-macpro/Data/nebula/runtime:/runtime
    links:
      - com.tradeany.api
      - etcd
```
