from os.path import abspath, dirname, join

from twitter import Api


DIRNAME = abspath(dirname(__file__))
TAGLINE = '\n        <p>Why not ask him about it?</p>'

twitter = Api(
    consumer_key='y2UGsVoswbDXurxYZIS7mg',
    consumer_secret='SVNdTZSBnxZSgJcjrlRHfCsTX2H4OhgP1sxIcNtM',
    access_token_key='14306567-XP53DhZMp4WOHLauRrAAgmr8ispHAp8hGu2qoSkp9',
    access_token_secret='Quu3A9aTNwK1OYL2gw7Iz8IDWBqqgQbxIbgmj6yKbY'
)

def replace_text(html, cur_status, new_status, cur_tagline, new_tagline):
    with open(join(DIRNAME, 'index.html'), 'w') as f:
        f.write(html.replace(cur_status, new_status).replace(cur_tagline, new_tagline))

text = twitter.GetUserTimeline('379060931')[0].text.lower()
with open(join(DIRNAME, 'index.html')) as f:
    html = f.read()

if 'yes' in text:
    replace_text(html, 'NO', 'YES', '</h1>\n      </div>', '</h1>%s\n      </div>' % TAGLINE)
elif 'no' in text:
    replace_text(html, 'YES', 'NO', TAGLINE, '')
else:
    pass

