# TensorRT-LLM 学习

## 1 概述

TensorRT LLM 用于加速和优化Nvidia GPU 上最新大型语言模型（LLM）的推理性能。

### **1.1关键功能**

+ **基于 Pytorch 架构**

  + **API 及部署能力**

    提供高层级 Python LLM API，操作便捷；

    支持多样化推理部署场景，覆盖单 GPU、多 GPU 及多节点部署。

  + **功能与生态集成**

    内置支持：包含各类并行策略及高级功能，无需额外开发基础并行能力；

    生态兼容：可与 更广泛的推理生态系统无缝集成，重点提及 NVIDIA Dynamo 和 Triton 推理服务器。

  + **架构设计与定制性**

    架构特点：采用模块化设计，便于开发者修改；基于 PyTorch 原生架构，降低开发适配门槛；

    定制能力：预设多个热门模型，开发者可通过 PyTorch 原生代码对模型进行定制，快速适配特定业务需求。

+ **最先进的性能**

  - **DeepSeek R1**：[在 Blackwell GPU 上创下世界纪录的推理性能](https://developer.nvidia.com/blog/nvidia-blackwell-delivers-world-record-deepseek-r1-inference-performance/)
  - **Llama 4 Maverick**：[在 B200 GPU 上突破 1,000 TPS/用户大关](https://developer.nvidia.com/blog/blackwell-breaks-the-1000-tps-user-barrier-with-metas-llama-4-maverick/)

+ **全面的模型支持**

  TensorRT LLM 支持最新、最流行的 LLM 架构：

  - **语言模型**：GPT-OSS、Deepseek-R1/V3、Llama 3/4、Qwen2/3、Gemma 3、Phi 4…
  - **多模式模型**：LLaVA-NeXT、Qwen2-VL、VILA、Llama 3.2 Vision……

  **TensorRT LLM 致力于在第 0 天**支持最受欢迎的模型。

+  **高级优化和生产功能**

  - **飞行中批处理和分页注意力**：in-flight batching 通过动态管理请求执行、处理上下文和生成阶段来消除等待时间，从而最大限度地提高 GPU 利用率并减少延迟。
  - **多 GPU 多节点推理**：通过模型定义 API，在多个 GPU 和节点之间实现具有张量、管道和专家并行性的无缝分布式推理。
  - **高级量化**：
    - **FP4 量化**：NVIDIA B200 GPU 上具有优化的 FP4 内核的原生支持
    - **FP8 量化**：利用 Hopper 架构在 NVIDIA H100 GPU 上自动转换
  - **推测解码**：多种算法，包括 EAGLE、MTP 和 NGram
  - **KV 缓存管理**：具有智能块重用和内存优化的分页 KV 缓存
  - **分块预填充**：通过将上下文拆分为可管理的块来有效处理长序列
  - **LoRA 支持**：支持 HuggingFace 和 NeMo 格式的多适配器，高效微调和适配
  - **检查点加载**：灵活地从各种格式（HuggingFace、NeMo、自定义）加载模型
  - **引导解码**：使用停用词、脏话和自定义约束进行高级采样
  - **分解服务（测试版）**：在不同的 GPU 上分离上下文和生成阶段，以实现最佳资源利用率

+ **最新 GPU 架构支持**

  TensorRT LLM 支持全系列 NVIDIA GPU 架构：

  - **NVIDIA Blackwell**：B200、GB200、RTX Pro 6000 SE，带 FP4 优化
  - **NVIDIA Hopper**：H100、H200、GH200，配备 FP8 加速
  - **NVIDIA Ada Lovelace**：L40/L40S，具有 FP8 加速的 RTX 40 系列
  - **NVIDIA Ampere**：A100、RTX 30 系列，适用于生产工作负载

## 安装

安装和运行 TensorRT LLM 有多种方法。对于大多数用户来说，以下选项应按从简单到复杂的顺序排列。就支持的功能而言，这些方法是等效的。

注意：**本项目将下载并安装其他第三方开源软件项目。使用前请查看这些开源项目的许可条款。**

1. [NGC 上预构建的发布容器镜像](https://nvidia.github.io/TensorRT-LLM/installation/containers.html#containers)

   镜像地址网站：https://catalog.ngc.nvidia.com/orgs/nvidia/teams/tensorrt-llm/containers/release/tags?version=spark-single-gpu-dev

   ```shell
   docker run --ipc host --gpus all -p 8000:8000 -it nvcr.io/nvidia/tensorrt-llm/release
   ```

   

2. [PyPI](https://pypi.org/project/tensorrt-llm)上预先构建的发布轮（请参阅[通过 pip 在 Linux 上安装](https://nvidia.github.io/TensorRT-LLM/installation/linux.html#linux)）

3. [在 Linux 上从源代码构建](https://nvidia.github.io/TensorRT-LLM/installation/build-from-source-linux.html#build-from-source-linux)