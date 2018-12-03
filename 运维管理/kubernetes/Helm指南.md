#Helm指南
### helm安装脚本
> curl https://raw.githubusercontent.com/kubernetes/helm/master/scripts/get | bash

### 或者https://github.com/helm/helm/releases下载后手动安装
> tar -zxvf helm-v2.11.0-linux-amd64.tar.gz && mv linux-amd64/helm /usr/local/bin/helm

## TillerServer安装

### 创建rbac-config.yaml文件

```
apiVersion: v1
kind: ServiceAccount
metadata:
  name: tiller
  namespace: kube-system
---
apiVersion: rbac.authorization.k8s.io/v1beta1
kind: ClusterRoleBinding
metadata:
  name: tiller
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: cluster-admin
subjects:
  - kind: ServiceAccount
    name: tiller
    namespace: kube-system
```

> kubectl create -f rbac-config.yaml

### helm初始化tiller
> helm init --service-account tiller --upgrade -i registry.cn-hangzhou.aliyuncs.com/surenpi/tiller:v2.11.0 --stable-repo-url https://kubernetes.oss-cn-hangzhou.aliyuncs.com/charts

### helm添加istio仓库地址
> helm repo add istio https://istio.io/charts


### 如果使用的Helm版本早于2.9.0，则需要手工清除Job资源：
> kubectl -n istio-system delete job --all

### 清除CRD的话，则需要执行如下命令：
> kubectl delete -f install/kubernetes/helm/istio/templates/crds.yaml -n istio-system

### helm安装指令
> curl -L https://git.io/getLatestIstio | sh -

> helm install istio/istio --name istio --namespace istio-system

> helm install install/kubernetes/helm/istio --name istio --namespace istio-system

	

