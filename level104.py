def ispan(n):
    if sorted(n) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
        return True

fn1 = 1
fn2 = fn1

mod = 10 ** 9
counter = 0
while True:
    counter += 1
    fn = fn1 + fn2
    end = fn % mod
    if ispan(str(end)):
        print "end", counter
        if ispan(str(fn)[:9]):
            print counter + 2
            break
    fn2 = fn1
    fn1 = fn
    # print fn
