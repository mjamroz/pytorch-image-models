import wandb
#wandb.init()
api = wandb.Api()
run = api.from_path("mijam23/fungi-many/runs/y7pwwxv7")
project="mijam23/fungi-many"
for run in api.runs(project):
    run = api.from_path(f"{project}/runs/{run.id}")
    for artifact in run.logged_artifacts():
        if artifact.type == "model":
            print("DEL" if "best" not in artifact.aliases else "KEEP",artifact)
            if "best" not in artifact.aliases:
                artifact.delete()
            #else:
            #    print("KEEP", artifact)
