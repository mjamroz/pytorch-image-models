import wandb

sweep_config = {
    "command": ["python", "trainsweep.py", "--config=shroom-config.yaml"],
    "name": "bayes-lr-epoch-search",
    "method": "bayes",
    "metric": {"name": "eval_top1", "goal": "maximize"},
    "parameters": {
        'lr': {'distribution': 'uniform', 'min': 5e-5, "max": 1e-3},
        'epochs': {'distribution': 'int_uniform', 'min': 10, "max": 25},
    },
}

print("sweep_id", wandb.sweep(sweep_config, project="fungi-many"))
