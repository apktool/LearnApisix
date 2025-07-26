
# 检查 consul 是否可用

```bash
curl -vvvv -X  GET http://localhost:8500/v1/catalog/services
curl -vvvv -X  GET http://localhost:8500/v1/health/service/canary
```

# 部署插件

将 smart_consul 目录复制到 apisix 的 discovery 目录下面

然后参考 config.yaml 部署配置 apisix

# 测试灰度是否生效

```bash
curl -H "X-API-GRAY:true" -X GET http://localhost:9080/api/canary/v1/
# {"Hello":"Gray World"}

curl -H "X-API-GRAY:false" -X GET http://localhost:9080/api/canary/v1/
# {"Hello":"Normal World"}

curl -X GET http://localhost:9080/api/canary/v1/
# {"Hello":"Normal World"}
```
