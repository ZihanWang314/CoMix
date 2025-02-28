set -x

# if [ "$#" -lt 1 ]; then
#     echo "Usage: run_gemma_2b.sh <save_path> [other_configs...]"
#     exit 1
# fi

# save_path=$1

# Shift the arguments so $@ refers to the rest
# shift 2


torchrun main.py \
    data.train_files=data/gsm8k/train.parquet \
    data.val_files=data/gsm8k/test.parquet \
    +data.text_keys=['question','answer'] \
    data.micro_batch_size_per_gpu=4 \
    model.partial_pretrain=EleutherAI/pythia-14m \
    trainer.default_local_dir=output \
    trainer.project_name=gsm8k-sft \
    trainer.experiment_name=gsm8k-sft-pythia-14m \
    trainer.total_epochs=2 \
    trainer.logger=['console','wandb'] \
    trainer.default_hdfs_dir=null $@
    # +fsdp=false \
