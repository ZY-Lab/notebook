#K8S安装使用

### docker修改源 /etc/docker/daemon.json 文件并添加上 registry-mirrors 键值。
{
  "registry-mirrors": ["https://registry.docker-cn.com"]
}

### centos修改主机名称
> hostnamectl set-hostname  node1

### flannel安装基本
> kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml

### kubectl常用命令

> kubectl get pod --all-namespaces -o wide

> kubectl describe po podname -n kube-system

> kubectl port-forward $POD_NAME 9090:9090 -n kube-system 

> kubectl edit svc grafana -n monitoring

> kubectl proxy --address='192.168.3.221' --port=8081 --accept-hosts='^*$'
> kubectl proxy --address=192.168.3.221 --disable-filter=true

#### 删除kube-system下Evicted状态的pod
> kubectl get pods -n kube-system |grep Evicted| awk '{print $1}'|xargs kubectl delete pod  -n kube-system

### 私有镜像仓库拉取镜像
kubectl create secret docker-registry registrysecret --docker-server=registry.cn-hangzhou.aliyuncs.com  --docker-username=admin --docker-password=admin123 --docker-email=admin@ctsi.com.cn --namespace=default
