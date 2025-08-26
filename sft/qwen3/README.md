## 1. 安装依赖
pip install torch-2.3.1+cu118-cp310-cp310-linux_x86_64.whl
pip install pyarrow==15.0.0 --no-build-isolation
pip install datasets==3.2.0 --no-deps
pip install modelscope==1.22.0
pip install transformers==4.51.3
pip install peft==0.11.1
pip install accelerate==1.6.0
pip install swanlab==0.5.7
pip install multiprocess
pip install pandas
pip install aiohttp
pip install xxhash
pip install addict

## 2. 生成训练集和测评集
python dataset_parse.py
生成 train.jsonl 和 val.jsonl

## 3. 观测训练进展
https://swanlab.cn/space/~
Use an existing SwanLab account.
api key：Z4x70M1BP5Twi1XWZLgbZ

## 4. 推理模型
python model_inference.py