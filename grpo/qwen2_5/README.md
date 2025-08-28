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
pip install -i https://mirrors.aliyun.com/pypi/simple/  trl
pip install -i https://mirrors.aliyun.com/pypi/simple/ deepspeed==0.12.6


## 2. 下载数据集
python download_datasets.py

## 3. 执行训练
accelerate launch \
    --num_processes 2 \
    --config_file config/deepspeed_zero3.yaml \
    train_qwen2_5_thinking.py \
    --config config/grpo-qwen-2.5-3b-deepseek-r1-zero-countdown.yaml