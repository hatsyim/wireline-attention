# Wireline Attention
This repository contains codes and resources to reproduce Wireline Attention project. The project itself was made for ErSE 222 - Machine Learning in 
Geoscience course in KAUST as the final project.

## 0. Introduction
Mainly inspired by FORCE 2020 Facies Prediction competition (https://github.com/bolgebrygg/Force-2020-Machine-Learning-competition), we aim to seek a 
better solution for petrophysical analysis workflow. Thus, we propose an integrated petrophysical analysis workflow which we call Wireline Attention (or
WAtt in short).

## 1. Installation
The environment that was used to run notebooks in this repository can be installed by:

<code>###pls put environment installation here</code>

The data to reproduce the work can be obtained from:

https://drive.google.com/drive/folders/1xklSNkMVdYesDObvyl7zYYU8C5BJYb0f?usp=sharing

## 2. Instruction
The content of the notebooks contained within <code>/notebook</code> is summarized in the table below.

| No | Notebook name |Description |
| --- | --- | --- |
| 1 | [00_eda.ipynb](https://github.com/hatsyim/wireline_attention/blob/main/notebook/00_eda.ipynb) | Data augmentation and processing of the wireline data |
| 2 | [01_wireline_attention.ipynb](https://github.com/hatsyim/wireline_attention/blob/main/notebook/01_wireline_attention.ipynb) | Pre-training and fine-tuning (DTS prediction & facies classification) of WAtt |
| 3 | [02_visualization.ipynb](https://github.com/hatsyim/wireline_attention/blob/main/notebook/01_visualization.ipynb) | Visualize the results |

The project's presentation can be accessed through:

https://drive.google.com/file/d/1kU4t6RSz7MNE9sAdxEx205_d9QBSHiWk/view?usp=sharing

## 3. Remarks
Final result of the fine-tuning
- DTS prediction (R<sup>2</sup>): 0.928
- Facies prediction (FORCE score): -0.775

We notice that the results could still be improved by:
<code>###pls add something here</code>

## Thank you for your attention!

