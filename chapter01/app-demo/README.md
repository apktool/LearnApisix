
# 启动命令

**正常服务**
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/canary
uv run canary/normal.py
```

**灰度服务**
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)/canary
uv run canary/gray.py
```

# 访问命令

```bash
# 访问正常服务
curl -X GET http://localhost:8001/api/canary/v1/

# 访问灰度服务
curl -X GET http://localhost:8002/api/canary/v1/
```

# 更新 grpc 接口

```bash
python3 -m grpc_tools.protoc -Icanary=. --python_out=. --pyi_out=. --grpc_python_out=. canary.proto
```