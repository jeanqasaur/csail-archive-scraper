import urllib2

def get_page_contents():
    req = urllib2.Request('https://lists.csail.mit.edu/pipermail/csail-related/2014-September.txt')
    response = urllib2.urlopen(req)
    the_page = response.read()
    return the_page.splitlines()
