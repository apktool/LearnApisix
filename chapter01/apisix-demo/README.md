
# 配置 apisix route 和 upstream

```bash
# 添加 upstream
uv run pytest -s tests/test_apisix.py::test_add_upstream

# 添加 route
uv run pytest -s tests/test_apisix.py::test_add_route
```

# 配置 apisix 端口

```text
apisix.node_listen: 9080       # http  访问端口
apisix.ssl.listen.port: 9443   # https 访问端口

# admin 接口
apisix.enable_admin: true
deployment.admin.admin_key: []
deployment.admin.admin_listen.ip: 0.0.0.0
deployment.admin.admin_listen.port: 9180
```