# 卡尔曼滤波

## 1️⃣ 卡尔曼滤波概念

卡尔曼滤波（Kalman Filter, KF）是一种用于线性高斯系统的递推最优估计方法。在目标跟踪中，它可以根据历史观测值和运动模型预测目标位置，并融合新的观测更新估计。

卡尔曼滤波主要分为两步：

1. **预测（Predict）**：根据上一次的状态和运动模型预测下一时刻状态。
2. **更新（Update/Correct）**：根据当前观测值修正预测状态。

------

## 2️⃣ 状态定义

以二维位置和速度为例，状态向量可以定义为：
$$
\mathbf{x}_k =
 \begin{bmatrix}
 x_k \ y_k \ v_{x,k} \ v_{y,k}
 \end{bmatrix}
$$
**解释**：

- $x_k, y_k$：目标在时刻 $k$ 的位置。
- $v_{x,k}, v_{y,k}$：目标在时刻 $k$ 的速度。
- 如果是三维目标，可以加 $z$ 和 $v_z$，或者加航向角 $\theta$。

观测向量一般只包含可测量的量，例如位置：

$$
 \mathbf{z}_k =
 \begin{bmatrix}
 x^{\text{meas}}_k \ y^{\text{meas}}_k
 \end{bmatrix}
 $$

------

## 3️⃣ 预测步骤（Predict）

**状态预测公式**：
$$
\mathbf{\hat{x}}_k^- = \mathbf{F} \mathbf{\hat{x}}_{k-1} + \mathbf{B} \mathbf{u}_{k-1}
$$
**协方差预测公式**：

$$
 \mathbf{P}*k^- = \mathbf{F} \mathbf{P}*{k-1} \mathbf{F}^\top + \mathbf{Q}
 $$

**解释**：

- $\mathbf{\hat{x}}_k^-$：预测的状态向量（prior），未结合观测。
- $\mathbf{\hat{x}}_{k-1}$：上一次更新后的状态向量（posterior）。
- $\mathbf{F}$：状态转移矩阵，描述目标从上一个时刻到当前时刻的运动规律。
- $\mathbf{B}$：控制矩阵（如果没有控制输入，可忽略）。
- $\mathbf{u}_{k-1}$：控制输入，例如加速度。
- $\mathbf{P}_k^-$：预测状态协方差矩阵，表示预测的不确定性。
- $\mathbf{P}_{k-1}$：上次更新后的协方差。
- $\mathbf{Q}$：过程噪声协方差矩阵，描述模型不完美或随机扰动。

**举例**：匀速直线运动，采样间隔 $\Delta t$ 时，状态转移矩阵可以写为：

$$
 \mathbf{F} =
 \begin{bmatrix}
 1 & 0 & \Delta t & 0 \
 0 & 1 & 0 & \Delta t \
 0 & 0 & 1 & 0 \
 0 & 0 & 0 & 1
 \end{bmatrix}
 $$

------

## 4️⃣ 更新步骤（Update / Correct）

**卡尔曼增益公式**：

$$
 \mathbf{K}_k = \mathbf{P}_k^- \mathbf{H}^\top (\mathbf{H} \mathbf{P}_k^- \mathbf{H}^\top + \mathbf{R})^{-1}
 $$

**状态更新公式**：

$$
 \mathbf{\hat{x}}_k = \mathbf{\hat{x}}_k^- + \mathbf{K}_k (\mathbf{z}_k - \mathbf{H} \mathbf{\hat{x}}_k^-)
 $$

**协方差更新公式**：

$$
 \mathbf{P}_k = (\mathbf{I} - \mathbf{K}_k \mathbf{H}) \mathbf{P}_k^-
 $$

**解释**：

- $\mathbf{K}_k$：卡尔曼增益矩阵，决定预测与观测的权重。
- $\mathbf{H}$：观测矩阵，将状态映射到观测空间。
  - 对二维位置观测：
     $$
     \mathbf{H} =
     \begin{bmatrix}
     1 & 0 & 0 & 0 \
     0 & 1 & 0 & 0
     \end{bmatrix}
     $$
- $\mathbf{R}$：观测噪声协方差矩阵，描述测量的不确定性。
- $\mathbf{I}$：单位矩阵。
- $\mathbf{z}_k - \mathbf{H}\mathbf{\hat{x}}_k^-$：观测残差（innovation），表示预测与测量的差异。

------

## 5️⃣ 变量在目标跟踪中的意义总结

| 变量           | 含义                    | 示例                     |
| -------------- | ----------------------- | ------------------------ |
| $\mathbf{x}_k$ | 目标状态（位置 + 速度） | `[x, y, vx, vy]`         |
| $\mathbf{z}_k$ | 观测值（可测位置）      | `[x_meas, y_meas]`       |
| $\mathbf{F}$   | 状态转移矩阵            | 匀速运动模型             |
| $\mathbf{P}_k$ | 状态协方差矩阵          | 预测误差大小             |
| $\mathbf{Q}$   | 过程噪声协方差          | 模型不完美或随机运动     |
| $\mathbf{R}$   | 观测噪声协方差          | 测量误差大小             |
| $\mathbf{K}_k$ | 卡尔曼增益              | 决定预测 vs 观测权重     |
| $\mathbf{H}$   | 观测矩阵                | 状态到观测的映射         |
| $\mathbf{u}_k$ | 控制输入                | 例如加速度，可选         |
| $\mathbf{B}$   | 控制矩阵                | 控制输入映射到状态，可选 |

------

✅ 这样整套公式在 Typora 里直接复制即可，带 $$ 环绕即可渲染。

------

如果你愿意，我可以帮你画一张**目标跟踪的卡尔曼滤波流程图**，把预测、更新、残差、增益都标出来，更直观。

你希望我画吗？

------

## 1️⃣ 状态定义（3D目标）

三维目标通常需要跟踪位置、速度，有时还会加航向角（heading）或尺寸（length, width, height）。最基础的状态向量：

$$
 \mathbf{x}_k =
 \begin{bmatrix}
 x_k \ y_k \ z_k \ v_{x,k} \ v_{y,k} \ v_{z,k}
 \end{bmatrix}
 $$

**解释**：

- $x_k, y_k, z_k$：目标在三维空间中的位置。
- $v_{x,k}, v_{y,k}, v_{z,k}$：目标在三维空间中的速度。
- 如果需要跟踪航向角 $\theta$ 或尺寸，可在状态向量中增加相应分量，例如 `[x, y, z, vx, vy, vz, heading]`。

观测向量通常只包含可测量的量，例如三维位置：

$$
 \mathbf{z}_k =
 \begin{bmatrix}
 x^{\text{meas}}_k \ y^{\text{meas}}_k \ z^{\text{meas}}_k
 \end{bmatrix}
 $$

------

## 2️⃣ 预测步骤（Predict）

**状态预测公式**：

$$
 \mathbf{\hat{x}}_k^- = \mathbf{F} \mathbf{\hat{x}}_{k-1} + \mathbf{B} \mathbf{u}_{k-1}
 $$

**协方差预测公式**：
$$
\mathbf{P}_k^- = \mathbf{F} \mathbf{P}_{k-1} \mathbf{F}^\top + \mathbf{Q}
$$
**解释**：

- $\mathbf{\hat{x}}_k^-$：预测的状态向量（prior）。
- $\mathbf{F}$：状态转移矩阵。三维匀速运动模型：

$$
 \mathbf{F} =
 \begin{bmatrix}
 1 & 0 & 0 & \Delta t & 0 & 0 \
 0 & 1 & 0 & 0 & \Delta t & 0 \
 0 & 0 & 1 & 0 & 0 & \Delta t \
 0 & 0 & 0 & 1 & 0 & 0 \
 0 & 0 & 0 & 0 & 1 & 0 \
 0 & 0 & 0 & 0 & 0 & 1
 \end{bmatrix}
 $$

- $\mathbf{u}_{k-1}$：控制输入（例如加速度），可选。
- $\mathbf{B}$：控制矩阵，可选。
- $\mathbf{P}_k^-$：预测状态协方差矩阵。
- $\mathbf{Q}$：过程噪声协方差矩阵，描述运动模型的不确定性。

------

## 3️⃣ 更新步骤（Update）

**卡尔曼增益**：

$$
 \mathbf{K}_k = \mathbf{P}_k^- \mathbf{H}^\top (\mathbf{H} \mathbf{P}_k^- \mathbf{H}^\top + \mathbf{R})^{-1}
 $$

**状态更新**：

$$
 \mathbf{\hat{x}}_k = \mathbf{\hat{x}}_k^- + \mathbf{K}_k (\mathbf{z}_k - \mathbf{H} \mathbf{\hat{x}}_k^-)
 $$

**协方差更新**：
$$
 \mathbf{P}_k = (\mathbf{I} - \mathbf{K}_k \mathbf{H}) \mathbf{P}_k^-
$$
**解释**：

- $\mathbf{H}$：观测矩阵，将状态映射到观测空间。三维位置观测：

$$
 \mathbf{H} =
 \begin{bmatrix}
 1 & 0 & 0 & 0 & 0 & 0 \
 0 & 1 & 0 & 0 & 0 & 0 \
 0 & 0 & 1 & 0 & 0 & 0
 \end{bmatrix}
 $$

- $\mathbf{R}$：观测噪声协方差矩阵，描述测量的不确定性。
- $\mathbf{K}_k$：卡尔曼增益，决定预测 vs 观测的权重。
- $\mathbf{z}_k - \mathbf{H}\mathbf{\hat{x}}_k^-$：创新/残差。

------

## 4️⃣ 变量在3D目标跟踪中的意义

| 变量           | 含义           | 示例                       |
| -------------- | -------------- | -------------------------- |
| $\mathbf{x}_k$ | 目标状态       | `[x, y, z, vx, vy, vz]`    |
| $\mathbf{z}_k$ | 观测值         | `[x_meas, y_meas, z_meas]` |
| $\mathbf{F}$   | 状态转移矩阵   | 三维匀速运动               |
| $\mathbf{P}_k$ | 状态协方差     | 表示预测误差大小           |
| $\mathbf{Q}$   | 过程噪声协方差 | 模型不完美或随机运动       |
| $\mathbf{R}$   | 观测噪声协方差 | 测量误差大小               |
| $\mathbf{K}_k$ | 卡尔曼增益     | 决定预测 vs 观测权重       |
| $\mathbf{H}$   | 观测矩阵       | 状态到观测的映射           |
| $\mathbf{u}_k$ | 控制输入       | 加速度或外力，可选         |
| $\mathbf{B}$   | 控制矩阵       | 控制输入映射到状态，可选   |

