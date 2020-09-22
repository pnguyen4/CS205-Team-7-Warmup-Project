def test():
    print("Enter Command (run 'HELP' to see the guide):")
    #get user input
    userInput = input()
    tokens = parser(userInput)
    #print(tokens)
    output = match(tokens)
    print(output)


def parser(userInput):
    #split text into list
    text = userInput.split(' ')
    #get command one
    command = text[0]
    #declare target string
    target = ''
    #get the words between command and end of list
    for word in range(1,len(text)):
        target = target + text[word] + ' '
    #remove extra space at end of target word
    target = target.rstrip()
    return [command, target]


def match(tokens):
    switch = {
	"HELP": run_help,
	#"LOAD-DATA": todo,
        "GET-POPULATION-STATE": simulate_sql,
        "GET-POPULATION-UNIVERSITY": simulate_sql,
        "GET-CITY-UNIVERSITY": simulate_sql,
        "GET-CAPITAL-STATE": simulate_sql,
        "LIST-UNIVERSITY-STATE": simulate_sql,
        "IN-STATE-CAPITAL-UNIVERSITY": simulate_sql,
	"GET-STATE-UNIVERSITY": simulate_sql,
	"GET-NUM-INSTITUTIONS-STATE": simulate_sql
    }
    command = tokens[0].upper()
    func = switch.get(command, error_msg)
    arg = tokens[1].replace('"', '')
    return func(arg)


def load_data(null_arg=''):
    # This function should overwrite existing database (if there is one) and load csv data
    return "TODO"


def simulate_sql(arg):
    ''' Placeholder function until database functionality is implemented. '''
    test_output = "Query command issued with argument: '"
    test_output += arg
    test_output += "'. SQLite functionality TODO."
    return test_output


def error_msg(null_arg=''):
    return 'Invalid command. Run "HELP" to see valid commands and options.'


def run_help(null_arg=''):
    help = "Command Structure: [command] [string]\n"
    help += "\nCommand List (not case sensitive):"
    help += "\n\tget-population-university"
    help += "\n\tget-population-state"
    help += "\n\tget-city-university"
    help += "\n\tget-capital-state"
    help += "\n\tlist-university-state"
    help += "\n\tin-state-capital-university"
    help += "\n\tget-state-university"
    help += "\n\tget-num-institutions-state"
    return help

test()
