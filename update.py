from datetime import datetime
from email.utils import parsedate
from os.path import abspath, dirname, join
from time import mktime

from twitter import Api


DIRNAME = abspath(dirname(__file__))
TAGLINE = '\n        <p>Why not ask him about it?</p>'

twitter = Api(
    consumer_key='Wz5EWnKIG4c8Q2Eq3vc8Q',
    consumer_secret='eY8VPjH0IrVFN9QY3gJex0jKUxBv4cCY7Jzgpe7g',
    access_token_key='379060931-sGwVkbF3nrEGt7qCHJcKYmM9Py7qxYFJHz3i16zQ',
    access_token_secret='cD21OBNRFfo8DnXkDquAFDoBYnP7oKgI72Am13kEKQ4'
)

def replace_text(html, cur_status, new_status, cur_tagline, new_tagline):
    with open(join(DIRNAME, 'index.html'), 'w') as f:
        f.write(html.replace(cur_status, new_status).replace(cur_tagline, new_tagline))

def tweet_date(date):
    return datetime.fromtimestamp(mktime(parsedate(date)))

def tweet_text():
    reply = twitter.GetReplies()[0]
    tweet = twitter.GetUserTimeline()[0]
    if tweet_date(reply.created_at) > tweet_date(tweet.created_at):
        return reply.text
    return tweet.text

text = tweet_text()
with open(join(DIRNAME, 'index.html')) as f:
    html = f.read()

if 'yes' in text:
    replace_text(html, 'NO', 'YES', '</h1>\n      </div>', '</h1>%s\n      </div>' % TAGLINE)
elif 'no' in text:
    replace_text(html, 'YES', 'NO', TAGLINE, '')
else:
    pass

