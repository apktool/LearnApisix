
# 项目介绍

本项目联合形成一个简单的灰度发布的简单用例。


| 名称 | 说明 |
|:----|:----|
| apisix-discovery | 为了灰度服务而开发的 discovery 插件 |
| app-demo | 一个正常应用，一个灰度应用 |
| apisix-demo | 添加 route 和 upstream，使其支持 http 请求和 grpc 请求 |


依次将上述项目部署成功后可以使用。


灰度发布的核心思想如下所示：

1. 正常服务和灰度服务分别注册到 consul 上面，但是灰度服务注册到 consul 时追加后缀 `-gray`
2. 正常的处理过程中，由 apisix discovery 根据灰度标识 `X-API-GRAY` 来判断应该路由到 consul 的正常服务还是灰度服务


# 流程说明

1. 当 client 发起请求的时候，携带 `X-API-GRAY` 向 apisix 发起请求。
   - 对于 http 请求，该标识放在 Header 里面
   - 对于 grpc 请求，该标识放在 Metadata 里面
2. APISIX 接收到请求之后，将请求转发到下游对应的 upstream 里面获取 service_name
   - 对于 http 请求，截取 `/api/service_name/v1` 中的 service_name
   - 对于 grpc 请求，截取 `/service_name.ServiceName.MethodName` 中的 service_name
3. 根据 `X-API-GRAY` 和 `service_name` 来决定取 consul 中的哪个服务
   - 如果 `X-API-GRAY=true`，那么取 consul 中的 `service_name-gray 服务`
   - 如果 `X-API-GRAY=false`，那么取 consul 中的 `service_name 服务`


# 其他问题

1. 为什么同一个服务要向 consul 上面注册两次（http, rpc）
   > 因为 http 和 rpc 各自占了 1 个端口。 假定只用 grpc 的端口向 consul 上注册，那么发送 http 请求时就会出现   curl: (1) Received HTTP/0.9 when not allowed 这样的现象。
   > 归其原因是 http 请求发到了 grpc 的接口上面，grpc 无法处理该请求导致。反之亦然。
   
2. 为什么要向 consul 的 meta 里面写 scheme 信息
   > apisix upstream 需要根据协议类型来将请求转发到不同的端口（http 请求转发到 consul 上的 service_name http 端口），但是 consul 本身并不感服务类型。所以在服务注册的时候，将 scheme 保存到 meta 里面，供 apisix 使用。