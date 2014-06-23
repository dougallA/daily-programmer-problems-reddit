    import random, sys
    
    def gen_record():
        first_name = random.choice(open("dist.all.first", 'r').readlines()).rstrip()
        last_name = random.choice(open("dist.all.last", 'r').readlines()).rstrip()
        return first_name + ", " + last_name + " " + " ".join([str(random.randint(0,100))  for n in range(0,5)])


    if __name__ == "__main__":
        if len(sys.argv) == 2:
            for x in range (0, int(sys.argv[1])):
                print gen_record()
        else: 
            print "Please supply exactly one argument representing the size of the data set to generate."
