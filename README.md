# bonne
Shogi AI with deep learning

## Download kifu from floodgate

```bash
bash ./scripts/download-floodgate.sh <year> <year>
# e.g. bash ./scripts/download-floodgate.sh 2021 2022 2023
```

## Convert CSA to HCPE with filters

```
python3 ./scripts/csa_to_hcpe.py kifu/ kifu/kifu_2021-2023_r3500_eval5000.hcpe kifu/kifu_2021-2023_r3500_eval5000_test.hcpe --filter_moves 50 --filter_rating 3500
```

## Train

```
mkdir checkpoints/
python3 -m bonne.train kifu/kifu_2021-2023_r3500_eval5000.hcpe kifu/kifu_2021-2023_r3500_eval5000_test.hcpe -e 1 -b 2048 --lr 0.001 --eval_interval 1000
```
