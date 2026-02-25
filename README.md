# Infeasibility Detection for IoT Application Placement in Fog Computing

This repository contains the implementation and datasets for the paper **"Enhancing IoT Applications' Placement in the Feasibility Detection and Repair"** published in IEEE.

📄 **Paper Link**: [IEEE Xplore](https://ieeexplore.ieee.org/abstract/document/11119366)

## Overview

Fog computing extends cloud computing to the edge of the network, enabling IoT applications to be deployed closer to data sources. However, determining whether a given placement of IoT applications on fog infrastructure is feasible is a critical challenge. This project focuses on **proactive infeasibility detection** using machine learning techniques to predict whether an application placement will fail before actual deployment.

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

The model uses the following 8 features extracted from fog infrastructure and application characteristics:

| Feature | Description |
|---------|-------------|
| `GW_devCount_vs_appCount` | Gateway device count vs application count ratio |
| `GW_devCount_vs_compCount` | Gateway device count vs component count ratio |
| `GW_upwardBW_vs_appCount` | Gateway upward bandwidth vs application count |
| `GW_resCap_vs_demand` | Gateway resource capacity vs demand |
| `ES_devCount_vs_appCount` | Edge server device count vs application count ratio |
| `ES_devCount_vs_compCount` | Edge server device count vs component count ratio |
| `ES_upwardBW_vs_appCount` | Edge server upward bandwidth vs application count |
| `ES_resCap_vs_demand` | Edge server resource capacity vs demand |

**Target Variable**: `is_fail` (0 = feasible placement, 1 = infeasible placement)

## Model

The implementation uses **XGBoost Regressor** with the following hyperparameters:

- `n_estimators`: 40
- `max_depth`: 6
- `learning_rate`: 0.1
- `objective`: reg:logistic
- `tree_method`: exact

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

1. **all-infra**: Combined dataset from multiple infrastructure configurations
2. **infra-agnostic**: Data designed to be independent of specific infrastructure characteristics
3. **infra-specific-medium**: Data from medium-scale infrastructure setups

Raw data archives (`small.zip`, `medium.zip`, `large.zip`) are available in the `raw_data/` directory for custom preprocessing.

## Citation

If you use this code or dataset in your research, please cite the original paper:

```
Enhancing IoT Applications' Placement in the Fog with Proactive Infeasibility Detection and Repair
IEEE Conference Publication
DOI: 10.1109/... (see IEEE Xplore for full citation)
```

## License

This project is provided for research and educational purposes. Please refer to the original paper for detailed methodology and experimental results.

## Contact

For questions or issues related to this implementation, please open an issue in this repository.
