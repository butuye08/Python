from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r " % filename
print text.read()

print "Type the filename agian :"
file_agian = raw_input(">")

txt_again =open (file_again)

print txt_again.read ()