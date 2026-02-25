# Infeasibility Detection for IoT Application Placement in Fog Computing

This repository contains the implementation and datasets for the paper **"Enhancing IoT Applications' Placement in the Fog with Proactive Infeasibility Detection and Repair"** published in IEEE.

📄 **Paper Link**: [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11119366)

## Overview

Fog computing extends cloud computing to the edge of the network, enabling IoT applications to be deployed closer to data sources. However, determining whether a given placement of IoT applications on fog infrastructure is feasible is a critical challenge. This project focuses on **proactive infeasibility detection** using machine learning techniques to predict whether an application placement will fail before actual deployment.

### Key Contributions

- **Placement system framework** with the capability to detect and repair infeasible placement problems, ensuring reactive and efficient decision-making
- **ML model for infeasibility detection** leveraging a novel feature set that effectively represents both the infrastructure and application set
- **Heuristic algorithm** for repairing infeasible placement problems by rejecting low-priority applications' deployment requests
- **Dataset** with approximately 20,000 placement problems across various scales (small, medium, large infrastructures)
- **Comparative evaluation** with state-of-the-art Large Language Models (LLM) as baseline

## Project Structure

```
InfeasibilityDetection/
├── dataset/                    # Training and testing datasets
│   ├── all-infra/             # Combined infrastructure dataset
│   │   ├── train.csv
│   │   └── test.csv
│   ├── infra-agnostic/        # Infrastructure-agnostic dataset
│   │   ├── train.csv
│   │   └── test.csv
│   └── infra-specific-medium/ # Infrastructure-specific (medium scale) dataset
│       ├── train.csv
│       └── test.csv
├── evaluation/                 # Evaluation scripts
│   ├── all-infra.py           # Evaluation on combined infrastructure data
│   ├── infra-agnostic.py     # Infrastructure-agnostic evaluation
│   └── infra-specific.py     # Infrastructure-specific evaluation
└── raw_data/                   # Raw data archives
    ├── small.zip
    ├── medium.zip
    └── large.zip
```

## Features

The model uses the following 8 features extracted from fog infrastructure and application characteristics. These features represent statistical information from the most critical sub-nets in each network layer (Gateway and Edge Server layers):

| Feature | Description |
|---------|-------------|
| `GW_devCount_vs_appCount` | Gateway device count vs application count ratio |
| `GW_devCount_vs_compCount` | Gateway device count vs component count ratio |
| `GW_upwardBW_vs_appCount` | Gateway upward bandwidth vs application count |
| `GW_resCap_vs_demand` | Gateway resource capacity vs demand (most critical resource type) |
| `ES_devCount_vs_appCount` | Edge server device count vs application count ratio |
| `ES_devCount_vs_compCount` | Edge server device count vs component count ratio |
| `ES_upwardBW_vs_appCount` | Edge server upward bandwidth vs application count |
| `ES_resCap_vs_demand` | Edge server resource capacity vs demand (most critical resource type) |

**Target Variable**: `is_fail` (0 = feasible placement, 1 = infeasible placement)

### Feature Design Rationale

The feature set is designed to be **infrastructure-agnostic** by using statistical information from critical sub-nets rather than specific infrastructure details. For each network layer, the model captures:
- Node density relative to applications and components
- Bandwidth availability per application
- Resource capacity-to-demand ratios

This design enables the model to generalize across different infrastructure configurations, including those not present in the training data.

## Model

The implementation uses **XGBoost Regressor** with the following hyperparameters:

| Hyperparameter | Value |
|----------------|-------|
| `objective` | `reg:logistic` |
| `tree_method` | `exact` |
| `learning_rate` | `0.1` |
| `max_depth` | `6` |
| `n_estimators` | `40` |

The model outputs continuous values indicating the likelihood of infeasibility, which are converted to binary predictions using a threshold of 0.5.

### Performance

The model achieves:
- **86% infeasibility detection accuracy**
- Strong generalizability across different infrastructure scales
- Outperforms state-of-the-art LLMs with few-shot prompting

## Requirements

- Python 3.x
- pandas
- scikit-learn
- xgboost

Install dependencies:
```bash
pip install pandas scikit-learn xgboost
```

## Usage

### Run Evaluation on Different Datasets

**All Infrastructure Dataset:**
```bash
cd evaluation
python all-infra.py
```

**Infrastructure-Agnostic Dataset:**
```bash
python infra-agnostic.py
```

**Infrastructure-Specific Dataset:**
```bash
python infra-specific.py
```

Each script will output:
- Accuracy
- Recall
- Precision

## Datasets

Three dataset variants are provided to evaluate model performance under different scenarios:

| Dataset | Description | Infrastructure Scale |
|---------|-------------|---------------------|
| **all-infra** | Combined dataset from multiple infrastructure configurations | Small + Medium + Large |
| **infra-agnostic** | Cross-infrastructure generalization test | Trained on S+M, tested on L |
| **infra-specific-medium** | Medium-scale infrastructure only | Medium |

### Dataset Statistics

| Scale | Cloud | Edge Servers | Gateways | End Fog Nodes | Appliances | Problems |
|-------|-------|--------------|----------|---------------|------------|----------|
| Small | 1 | 3 | 3 | 20 | 40 | 9,000 |
| Medium | 1 | 3 | 20 | 200 | 400 | 6,000 |
| Large | 1 | 5 | 30 | 300 | 500 | 5,000 |

Raw data archives (`small.zip`, `medium.zip`, `large.zip`) are available in the `raw_data/` directory for custom preprocessing.

### Data Generation

The dataset is generated using Data Stream Processing (DSP) applications as the use case. Each application contains:
- 1-10 data sources
- 1-5 operator types (1-10 components each)
- 1-10 data consumers

Applications are incrementally added to infrastructure until the problem becomes infeasible, ensuring a balanced distribution of feasible and infeasible problems.

## Citation

If you use this code or dataset in your research, please cite:

```bibtex
@inproceedings{xia2025enhancing,
  title={Enhancing IoT Applications' Placement in the Fog with Proactive Infeasibility Detection and Repair},
  author={Xia, Ye and Zhang, Xing},
  booktitle={2025 10th International Conference on Fog and Mobile Edge Computing (FMEC)},
  pages={74--80},
  year={2025},
  organization={IEEE}
}
```

## License

This project is provided for research and educational purposes. Please refer to the original paper for detailed methodology and experimental results.

## Contact

For questions or issues related to this implementation, please open an issue in this repository.
