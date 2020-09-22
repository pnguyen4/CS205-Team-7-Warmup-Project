
def parser():
    #get user input 
    userInput = input()
    #split text into list
    text = userInput.split(' ')
    #get command one 
    command = text[0]
    #declare target string
    target = ''
    #get the words between command two and end of list 
    for word in range(1,len(text)): 
        target = target + text[word] + ' '
    #remove extra space at end of target word
    target = target.rstrip()
    
    
    
parser()
