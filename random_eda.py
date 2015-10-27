###Random helper function 

def find_words(email_body):
    email_text=re.search(r"Re\:|re\:|To\:|to\:|From\:|from\:|Fwd\:|FWD\:|Subject\:|FW\:|Sent\:",email_body)
    if email_text:
        return email_body
def find_wordsv(email_body):
    email_text=re.search(r"Sent from my",email_body)
    if email_text:
        return email_body

def find_words():
	email_text=re.search(r"Re\:|re\:|Subject\:",email_body)
	if email_text:
		return( " ".join( email_text ))

from random import sample
# create random index
rindex =  np.array(sample(xrange(len(emails)), 10))
dfr = emails.ix[rindex]
for i in dfr.ExtractedBodyText:
    print ""
    print ""
    print i
    print ""		