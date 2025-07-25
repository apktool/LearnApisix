
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