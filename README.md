# Tetue
USI Shogi engine powered by deep learning.

## Usage

### Install dependencies

```
pip install -r requirements.txt
```

### Run the engine

```
python -m tetue.usi.mcts_usi
```

It will start wating for input from stdin.

## Train

### Download kifu from floodgate

```bash
bash ./scripts/download-floodgate.sh <year> <year>
# e.g. bash ./scripts/download-floodgate.sh 2021 2022 2023
```

### Convert CSA to HCPE with filters

```
python3 ./scripts/csa_to_hcpe.py kifu/ kifu/kifu_2021-2023_r3500_eval5000.hcpe kifu/kifu_2021-2023_r3500_eval5000_test.hcpe --filter_moves 50 --filter_rating 3500
```

### Start training

```
mkdir checkpoints/
python3 -m tetue.train kifu/kifu_2021-2023_r3500_eval5000.hcpe kifu/kifu_2021-2023_r3500_eval5000_test.hcpe -e 1 -b 2048 --lr 0.001 --eval_interval 1000
```

### Tested GPU environment

```
❯ nvidia-smi -q | head

==============NVSMI LOG==============

Timestamp                                 : Sun Oct 29 10:50:34 2023
Driver Version                            : 470.42.01
CUDA Version                              : 11.4

Attached GPUs                             : 1
GPU 00000000:01:00.0
    Product Name                          : NVIDIA GeForce RTX 3070
```

## Acknowledgements

Tetue borrows [DeepLearningShogi](https://github.com/TadaoYamaoka/DeepLearningShogi/tree/master)'s source code for the search parts.
A big thank you goes out to it.
