import wandb

sweep_config = {
    "command": ["python", "trainsweep.py", "--config=plants-config.yaml"],
    "name": "bayes-lr-search",
    "method": "bayes",
    "metric": {"name": "eval_top1", "goal": "maximize"},
    "parameters": {
        'lr': {'distribution': 'uniform', 'min': 1e-4, "max": 5e-2},
        'drop': {'distribution': 'uniform', 'min': 0.0, "max": 0.4},
    },
}

print("sweep_id", wandb.sweep(sweep_config, project="plants-many"))
