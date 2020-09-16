import re


def test():
    ''' Define example test cases for parsing. '''
    # output = parse("")
    # output = parse("HELP")
    # output = parse('GET-POPULATION')
    # output = parse('GET-POPULATION "University of Vermont"')
    # output = parse('GET-POPULATION university')
    # output = parse('GET-POPULATION university "University of Vermont"')
    output = parse('GET-POPULATION university "Harvard University"')
    print(output)


def parse(user_in):
    '''
    1. Create a list of words and strings ("*") from user input.
    2. Find function that corresponds to list of words with match().
    '''
    if len(user_in) == 0:
        return "No input."

    find_arg = list(filter(lambda x: x != '', re.split(r'"(.*?)"', user_in)))
    tokens = find_arg[0].split()

    if len(find_arg) > 2:
        return "Error: more than one argument."
    elif len(find_arg) > 1:
        tokens.append(find_arg[1])
    return match(tokens)


def match(tokens):
    '''
    Simulate a switch statement to run appropriate query with user argument.
    '''

    tlen = len(tokens)
    if tlen < 3:
        if tokens[0] == "HELP":
            return run_help()  # issues HELP command
        return error_msg()

    fullcommand = tokens[0] + " " + tokens[1]
    arg = tokens[2]
    switch = {
        "GET-POPULATION state": simulate_sql,
        "GET-POPULATION university": simulate_sql,
        "GET-CITY university": simulate_sql,
        "GET-CAPITAL university": simulate_sql,
        "LIST-UNIVERSITY state": simulate_sql,
        "IN-STATE-CAPITAL": simulate_sql
    }
    func = switch.get(fullcommand, error_msg())
    return func(arg)


def simulate_sql(arg):
    ''' Placeholder function until database functionality is implemented. '''
    test_output = "Query command issued with argument: '"
    test_output += arg
    test_output += "'. SQLite functionality TODO."
    return test_output


def error_msg():
    ''' Generic error message. '''
    msg = 'Invalid command and/or option.'
    msg += ' Run "HELP" to see valid commands and options.'
    return msg


def run_help():
    ''' TODO '''
    return "TODO"


test()
