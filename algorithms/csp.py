def is_valid(assignment, var, value, constraints):

    for (v1, v2) in constraints:

        if v1 == var and v2 in assignment:

            if assignment[v2] == value:
                return False

        if v2 == var and v1 in assignment:

            if assignment[v1] == value:
                return False

    return True


def backtrack(assignment, variables, domains, constraints):

    if len(assignment) == len(variables):
        return assignment

    var = [v for v in variables if v not in assignment][0]

    for value in domains[var]:

        if is_valid(assignment, var, value, constraints):

            assignment[var] = value

            result = backtrack(assignment, variables, domains, constraints)

            if result:
                return result

            del assignment[var]

    return None


def csp_solver(variables, domains, constraints):

    return backtrack({}, variables, domains, constraints)