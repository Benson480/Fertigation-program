##import numpy
##def levenshteinDistanceDP(token1, token2):
##    distances = numpy.zeros((len(token1) + 1, len(token2) + 1))
##
##    for t1 in range(len(token1) + 1):
##        distances[t1][0] = t1
##
##    for t2 in range(len(token2) + 1):
##        distances[0][t2] = t2
##        
##    a = 0
##    b = 0
##    c = 0
##    
##    for t1 in range(1, len(token1) + 1):
##        for t2 in range(1, len(token2) + 1):
##            if (token1[t1-1] == token2[t2-1]):
##                distances[t1][t2] = distances[t1 - 1][t2 - 1]
##            else:
##                a = distances[t1][t2 - 1]
##                b = distances[t1 - 1][t2]
##                c = distances[t1 - 1][t2 - 1]
##                
##                if (a <= b and a <= c):
##                    distances[t1][t2] = a + 1
##                elif (b <= a and b <= c):
##                    distances[t1][t2] = b + 1
##                else:
##                    distances[t1][t2] = c + 1
##
##    printDistances(distances, len(token1), len(token2))
##    return distances[len(token1)][len(token2)]
##
##def printDistances(distances, token1Length, token2Length):
##    for t1 in range(token1Length + 1):
##        for t2 in range(token2Length + 1):
##            print(int(distances[t1][t2]), end=" ")
##        print()
##
##distance = levenshteinDistanceDP("kelm", "hello")
##
import readline

class MyCompleter(object):  # Custom completer

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options 
                                    if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try: 
            return self.matches[state]
        except IndexError:
            return None

completer = MyCompleter(["hello", "hi", "how are you", "goodbye", "great"])
readline.set_completer(completer.complete)
readline.parse_and_bind('tab: complete')

input = raw_input("Input: ")
print("You entered", input)
