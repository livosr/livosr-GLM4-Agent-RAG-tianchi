# 阿里云天池 - GLM 法律行业大模型挑战赛 - 我们小组实现基于大模型的对话机器人源码

## 背景
阿里云天池-第三届琶洲算法大赛-GLM法律行业大模型挑战赛道

基于 GLM-4 模型，制定技术方案。方案应利用大语言模型的语义理解和函数调用功能，准确解析用户查询，并通过访问相关法律数据库或 API，提供服务，包括解答法律问题、查询案件信息、检索历史案件和分析司法数据。

## 介绍

运用GLM4 API和高效微调GLM4-9B模型，构建法律信息对话机器人。通过封装数据层服务，并使用LLM作为Agent，对输入问题进行有监督微调，将其拆分为若干子问题，依次调用自行设计的数据层服务获取信息，实现基于检索增强生成（RAG）的答案生成。

## 使用方法

1. 安装依赖：
    ```bash
    pip install -r glm4-fintuning-demo/requirements.txt
    ```

2. LoRA/P-tuning v2 GLM4-9B实现子问题分割：
    - 进入 `./glm4-fintuning-demo` 目录
    - 训练模型：
        ```bash
        python finetune.py data THUDM/glm-4-9b-chat configs/lora.yaml
        ```
        或
        ```bash
        python finetune.py data THUDM/glm-4-9b-chat configs/p-tuning.yaml
        ```
    - 分割子问题：
        ```bash
        python inference.py
        ```

3. AI agent 实现RAG 完成查询与答案生成：
    - 进入 `./agent` 目录
    - 运行：
        ```bash
        python agent_with_sub.py
        ```

## 目录简介

1. `/Agent` - AI agent总流程，包括问题理解、子问题分割、参数生成、知识库访问、知识整理及答案生成。
2. `/api` - service层与dao层。
3. `/glm` - 服务入参生成与工具函数。
4. `/glm4-fintuning-demo` - 子问题分割peft。

## 贡献者

盛裕彬，祝月，申琳
