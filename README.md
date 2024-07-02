# yuyuelin_b

#### 介绍
竹杖芒鞋轻胜马，谁怕？一蓑烟雨任平生。

#### 软件架构
peft 按照readme.md配置就行
注意一下pytorch与cuda的版本适配问题
peft运行：
python finetune.py  data  THUDM/glm-4-9b-chat  configs/lora.yaml 
或
python finetune.py  data  THUDM/glm-4-9b-chat  configs/ptuning_v2.yaml