#David Rodgers


#build a list comp that reads a txt file, pulls lines that fullfill criteria,
#splits the lines to focus on the number, then sums all the numbers pulled

print "The sum of the REAL numbers is:",\
      sum([int(num[1]) for num\
           in [line.strip().split(":") for line\
               in open("hw3_sample.txt","r").readlines()\
               if line[0] == "R"]])