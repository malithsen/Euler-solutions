lst = [x for x in range(11, 21)]


def find_soln(step):
    for i in xrange(step, 999999999, step):
        if all(not i%n for n in lst):
            return i
    return None

if __name__ == '__main__':
    soln = find_soln(20)            
    if soln is None:
        print "No solution"
    else:
        print "Answer: ", soln  
