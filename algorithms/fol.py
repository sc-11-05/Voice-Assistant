class KnowledgeBase:

    def __init__(self):
        self.facts = set()
        self.rules = []

    def add_fact(self, fact):
        self.facts.add(fact)

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def infer(self):

        new_facts = set(self.facts)

        for premise, conclusion in self.rules:

            for fact in self.facts:

                if fact.startswith(premise.replace("(x)", "")):

                    entity = fact.split("(")[1].replace(")", "")

                    new_fact = conclusion.replace("x", entity)

                    new_facts.add(new_fact)

        self.facts = new_facts

    def ask(self, query):

        return query in self.facts