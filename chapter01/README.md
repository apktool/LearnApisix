

基于 apisix 实现灰度切换。

实现一个简单的 python 应用程序，可以注册到 consul 上面。
然后实现一个 apisix 的 discovery plugin，使其可以根据 url 前缀实现自动切换
