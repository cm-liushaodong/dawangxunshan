from modelscope.msdatasets import MsDataset


ds = MsDataset.load('zouxuhong/Countdown-Tasks-3to4', cache_dir='/home/hadoop-ht-oedatamining/dawangxunshan/grpo/qwen2_5/datasets', subset_name='default', split='train')

