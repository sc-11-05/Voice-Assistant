from algorithms.fol import KnowledgeBase
from algorithms.csp import csp_solver


def reasoning_demo():

    kb = KnowledgeBase()

    kb.add_fact("Human(Socrates)")
    kb.add_rule("Human(x)", "Mortal(x)")

    kb.infer()

    print("Inference:", kb.ask("Mortal(Socrates)"))


def scheduling_demo():

    variables = ["AI", "DSA", "WEB"]

    domains = {
        "AI": ["9AM", "10AM"],
        "DSA": ["9AM", "10AM"],
        "WEB": ["9AM", "10AM"]
    }

    constraints = [
        ("AI", "DSA"),
        ("DSA", "WEB")
    ]

    result = csp_solver(variables, domains, constraints)

    print("Schedule:", result)