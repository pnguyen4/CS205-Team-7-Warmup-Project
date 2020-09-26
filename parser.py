import loading_database as dbIO

def test():
    print("Enter Command (run 'HELP' to see the guide):")
    while True:
        print(" > ", end='')
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
        "QUIT": exit,
	"HELP": run_help,
	"LOAD-DATA": load_data,
        "GET-POPULATION-STATE": dbIO.get_population_state,
        "GET-POPULATION-UNIVERSITY": dbIO.get_population_university,
        "GET-CITY-UNIVERSITY": dbIO.get_city_university,
        "GET-CAPITAL-STATE": dbIO.get_capital_state,
        "LIST-UNIVERSITY-STATE": dbIO.list_university_state,
        "IN-STATE-CAPITAL-UNIVERSITY": dbIO.in_state_capital_university,
	"GET-STATE-UNIVERSITY": dbIO.get_state_university,
	"GET-NUM-INSTITUTIONS-STATE": dbIO.get_num_institutions_state
    }
    command = tokens[0].upper()
    func = switch.get(command, error_msg)
    arg = tokens[1].replace('"', '')
    global database
    return func(arg, database)


def simulate_sql(arg):
    ''' Placeholder function until database functionality is implemented. '''
    test_output = "Query command issued with argument: '"
    test_output += arg
    test_output += "'. SQLite functionality TODO."
    return test_output


def error_msg(_=None,__=None):
    return 'Invalid command. Run "HELP" to see valid commands and options.'


def run_help(_=None,__=None):
    help = "Command Structure: [command] [argument]"
    help += "\nSurrounding argument with quotes is optional.\n"
    help += "\nCommand List (not case sensitive):"
    help += "\n\thelp"
    help += "\n\tload-data"
    help += "\n\tquit"
    help += "\n\tget-population-university"
    help += "\n\tget-population-state"
    help += "\n\tget-city-university"
    help += "\n\tget-capital-state"
    help += "\n\tlist-university-state"
    help += "\n\tin-state-capital-university"
    help += "\n\tget-state-university"
    help += "\n\tget-num-institutions-state"
    return help


def exit(_=None, __=None):
    global database
    if database != None:
        database.close()
    quit()


database = None
def load_data(_=None, __=None):
    global database
    database = dbIO.load_DB_wrapper()
    return "Database Loaded."

test()
