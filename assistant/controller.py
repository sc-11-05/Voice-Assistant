from assistant.nlp_parser import parse_command
from assistant.planner import plan_task
from executor.run_task import run_task


def handle_command(command):

    data = parse_command(command)

    if not data:
        print("Command not understood")
        return

    action = data["intent"]
    entity = data["entity"]

    # run these directly (no planner needed)
    if action in ["schedule", "reasoning", "minimax", "genetic", "annealing", "dls", "iddfs", "bidirectional", "rbfs"]:
        run_task(action)
        return

    path = plan_task(action)

    if not path:
        print("No plan found")
        return

    print("Plan:", path)

    for step in path[1:]:
        run_task(step, entity)