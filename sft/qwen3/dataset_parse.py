from modelscope.msdatasets import MsDataset
import json
import random
import os

random.seed(42)

ds = MsDataset.load('krisfu/delicate_medical_r1_data', subset_name='default', split='train')
data_list = list(ds)
random.shuffle(data_list)

split_idx = int(len(data_list) * 0.9)

train_data = data_list[:split_idx]
val_data = data_list[split_idx:]

current_dir = os.path.dirname(os.path.abspath(__file__))

train_dataset_path = os.path.join(current_dir, "datasets/train.jsonl")
test_dataset_path = os.path.join(current_dir, "datasets/val.jsonl")

with open(train_dataset_path, 'w', encoding='utf-8') as f:
    for item in train_data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

with open(test_dataset_path, 'w', encoding='utf-8') as f:
    for item in val_data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')

print(f"The dataset has been split successfully.")
print(f"Train Set Size：{len(train_data)}")
print(f"Val Set Size：{len(val_data)}")