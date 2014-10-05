"""Scraping csail-related archives.

"""
import getopt
import sys

import GetPage
import ProcessContents

CSAIL_RELATED_URL = "https://lists.csail.mit.edu/pipermail/csail-related/"

def main(argv):
    email_of_interest = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"he:o:",["email=","ofile="])
    except getopt.GetoptError:
        print 'scrape.py -e <email> -o <outputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print 'scrape.py -e <email> -o <outputfile>'
            sys.exit()
        elif opt in ("-e", "--email"):
            email_of_interest = arg.replace("@", " at ")
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    # TODO: Read args eventually.
    page_lines = GetPage.get_page_contents()
    emails = ProcessContents.process_contents(page_lines, email_of_interest)
    
    f = open(outputfile, 'w')
    f.write(''.join(emails))
    f.close()

if __name__ == "__main__":
    main(sys.argv[1:])
