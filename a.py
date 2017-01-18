fileA = sc.textFile("input/join1_FileA.txt")
fileA.collect()
#Out[]: [u'able,991', u'about,11', u'burger,15', u'actor,22']

fileB = sc.textFile("input/join1_FileB.txt")
fileB.collect()
#Out[29]: 
[u'Jan-01 able,5',
 u'Feb-02 about,3',
 u'Mar-03 about,8 ',
 u'Apr-04 able,13',
 u'Feb-22 actor,3',
 u'Feb-23 burger,5',
 u'Mar-08 burger,2',
 u'Dec-15 able,100']

def split_fileA(line):

   # split the input line in word and count on the comma
   word, count = line.split(',')

   # turn the count to an integer  
   count = int(count)

   return (word, count)


test_line = "able,991"
split_fileA(test_line)
fileA_data.collect()

def split_fileB(line):
    # split the input line into word, date and count_string
    
   word_date, count = line.split(',')

   # turn the count to an integer  
   count = int(count)
   word, date = word_date.split(' ')
   return (word, date + " " + count) 
