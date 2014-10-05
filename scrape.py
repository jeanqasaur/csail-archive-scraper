"""Scraping csail-related archives.

"""
import getopt
import sys

import GetPage
import ProcessContents

CSAIL_RELATED_URL = "https://lists.csail.mit.edu/pipermail/csail-related/"

def main(argv):
    email_of_interest = ''
    outputfile = 'out.txt'
    months = 1

    try:
        opts, args = getopt.getopt(argv,"he:o:m:",["email=","ofile=","months="])
    except getopt.GetoptError:
        print 'scrape.py -e <email> -o <outputfile> -m <months>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'scrape.py -e <email> -o <outputfile> -m <months>'
            sys.exit()
        elif opt in ("-e", "--email"):
            email_of_interest = arg.replace("@", " at ")
        elif opt in ("-o", "--ofile"):
            outputfile = arg
        elif opt in ("-m", "--months"):
            months = int(arg)

    page_lines = GetPage.get_page_contents(months)
    emails = ProcessContents.process_contents(page_lines, email_of_interest)
    
    f = open(outputfile, 'w')
    f.write(''.join(emails))
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
