import copy

HEADER_LINES = ["Message-ID:", "Subject:", "Date:", "From:"]

def process_contents(lines, email_of_interest):
    lines.reverse()

    """Takes the lines in a file and spits back out a list of emails from
    a user.
    """
    header_lines = []
    inside_email_of_interest = False
    backtrack_string = ""
    cur_email_accum = []
    all_emails_accum = []

    while lines:
        cur_line = lines.pop()

        # See if we're still going through header lines, then continue going
        # through header lines.
        if header_lines:
            line_tag = cur_line.split(' ')[0]
            # If we have a well-formatted next header, then we keep going.
            if (line_tag == header_lines[-1]):
                cur_header_line = header_lines.pop()
                if line_tag == "From:" and email_of_interest in cur_line:
                    inside_email_of_interest = True
                # If we're on the last header, then we update our accumulators.
                if len(header_lines) == 1:
                    backtrack_string = ""
                    if cur_email_accum:
                        all_emails_accum.append('\n'.join(cur_email_accum))
                        cur_email_accum = []
            # Otherwise, gotta backtrack.
            else:
                if inside_email_of_interest:
                    if backtrack_string:
                        cur_email_accum.append(backtrack_string)
                        backtrack_string = ""
        else:
            # If we're not going through the headers, check to see if we need
            # to start going through the headers.
            words = cur_line.split(' ')
            if words and words[0] == "From":
                backtrack_string = cur_line
                header_lines = copy.deepcopy(HEADER_LINES)
                inside_email_of_interest = False
            # Otherwise we're in the body of the email, so we should check
            # whether we are inside an email of interest. If so, we accumulate
            # this line.
            else:
                if inside_email_of_interest:
                    cur_email_accum.append(cur_line)

    # If we ended inside an email of interest, collect that.
    if inside_email_of_interest:
        all_emails_accum.append('\n'.join(cur_email_accum))

    return all_emails_accum
