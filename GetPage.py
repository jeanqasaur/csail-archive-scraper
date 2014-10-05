import urllib2

BASE_URL = "https://lists.csail.mit.edu/pipermail/csail-related/" 
MONTHS = ["January", "February", "March", "April", "May", "June", "July"
    , "August", "September", "October", "November", "December"]

def get_page_contents(num_months):
    # The first available archive is July 2004.
    cur_month = 9 # TODO: Get this from time-date.
    cur_year = 2014

    lines = []

    for i in range(0, num_months):
        # Hacky hard-coded stop at current year.
        if cur_month == 6 and cur_year == 2004:
            break

        archive_url = BASE_URL + str(cur_year) + "-" + MONTHS[cur_month] + \
            ".txt"
        print ("Fetching " + archive_url + "...")
        req = urllib2.Request(archive_url)
        response = urllib2.urlopen(req)
        the_page = response.read()
        lines.extend(the_page.splitlines())

        if cur_month == 0:
            cur_month = 11
            cur_year = cur_year - 1
        else:
            cur_month = cur_month - 1

    return lines
