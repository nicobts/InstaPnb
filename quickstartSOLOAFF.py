import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'soloaffittitrieste'
insta_password = 'Affittits2018'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-0.10,
				  delimit_by_numbers=True,
				   max_followers=None,
				    max_following=None,
				     min_followers=45,
				      min_following=77)
    session.set_do_like(enabled=True, percentage=100)
    #session.set_upper_follower_count(limit=5000)
    #session.set_lower_follower_count(limit = 300)
    session.set_do_follow(enabled=True, percentage=80, times=2)
    session.set_do_comment(True, percentage=10)
    session.set_comments([u'😃😃😃☺️☺️☺️💯💯💯  @{}', u' 😃😃😃💯💯  @{}' , u'😃😃😃☺️☺️☺️💯💯💯  @{}', u'👌👍👌👍 @{}' , u' 💯💯👍👍 @{}' , u'😃😃😃👍👍 @{}'] , media=None)
    #session.set_dont_include(['friend1', 'friend2', 'friend3'])
    #session.set_dont_like(['pizza', 'girl'])
    session.set_user_interact(amount=4, randomize=True, percentage=75, media=None)

    # actions
    #accounts:maison_foto , aldieci , amber_del_discipline , bancomoda, nfmshop,diecidiecinapoli,vicolo.official ,melonestore,glamourshopalessia,dolcelunashop
    session.interact_user_followers(['igerstrieste'], amount=20, randomize=True)
    session.interact_user_followers(['unitrieste'], amount=20, randomize=True)
    session.interact_user_followers(['igersts'], amount=20, randomize=True)
    session.interact_user_followers(['triestesocial'], amount=20, randomize=True)
    session.interact_user_followers(['discover_trieste'], amount=20, randomize=True)

    session.like_by_tags(['trieste','monfalcone' ,'gorizia' ,'udine' ,'gradisca', 'unitrieste', 'triestecity' ], amount=10, media=None)


    session.like_by_locations(['214560101/trieste-italy/'], amount=25)
    session.like_by_locations(['221476691/udine-italy/'], amount=25) 
    session.like_by_locations(['236835452/monfalcone-italy/'], amount=25) 
    session.like_by_locations(['235382046/gorizia/'], amount=25) 
    session.like_by_locations(['6431604/ospedale-maggiore/'], amount=5)
    session.like_by_locations(['217471323/universita-degli-studi-di-trieste/'], amount=25)
    session.like_by_locations(['223245508031595/sslmit-trieste/'], amount=5)
    session.like_by_locations(['255671440/universita-degli-studi-di-trieste-facolta-di-lettere-e-filosofia/'], amount=5)
    session.like_by_locations(['316328658831723/piazza-unita-ditalia/'], amount=5)
    session.like_by_locations(['2132883663604915/piazza-della-borsa/'], amount=5)
    session.like_by_locations(['247298252/sissa-scuola-internazionale-superiore-di-studi-avanzati/'], amount=5)
    session.like_by_locations(['236835452/monfalcone-italy/'], amount=5)
    session.like_by_locations(['354103303/wartsila-italia/'], amount=5)


    session.unfollow_users(amount=300, onlyInstapyFollowed = True, onlyNotFollowMe=True, onlyInstapyMethod = 'FIFO', sleep_delay=60)

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
