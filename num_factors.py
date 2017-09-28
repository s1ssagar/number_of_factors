import math

def factors(num):
    prime_fac = []
    num_of_fac = []
    # A number has factors only upto its Sqrt
    max_fac = int(math.sqrt(num)+1)
    for x in xrange(1, max_fac+1):
        count = 0
        if num % x == 0:
            for y in xrange(1, x):
                if x % y == 0:
                    count += 1
                    if count > 1:
                        break
            if count == 1:
                prime_fac.append(x)
    for factor in prime_fac:
        count = 0
        while num % factor == 0:
            count += 1
            num = num / factor
        num_of_fac.append(count)
    # print prime_fac, num_of_fac
    if prime_fac == [] and num == 0:
        print "zero is the only integer that has infinitely many factors, and zero is the only integer that has zero for a factor."
    elif prime_fac == [] and num != 1:
        print "Number of factors are:", 2
    else:
        product = 1
        for prod in num_of_fac:
            product *= (prod+1)
        print "Number of factors are:", product

def main():
    factors(abs(input("Enter the number ")))

if __name__ == "__main__":
    main()