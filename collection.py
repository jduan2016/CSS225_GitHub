# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889
# Dictionary Documentation:
# https://www.geeksforgeeks.org/how-to-print-a-dictionary-in-python/
# %s for printing:
# https://www.geeksforgeeks.org/what-does-s-mean-in-a-python-format-string/
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}
for key,value in authors.items():
    #print "%s" % authors + " died in " + "%d." % Date
    #print(key,"died in",value,".")
    print("%s died in %s." % (key,value))

