import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = ''
insta_password = ''

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
    session.set_user_interact(amount=4, randomize=True, percentage=100, media=None)

    # actions
    #accounts:maison_foto , aldieci , amber_del_discipline , bancomoda, nfmshop,diecidiecinapoli,vicolo.official ,melonestore,glamourshopalessia,dolcelunashop
    session.interact_user_followers(['body_fitness_fashion'], amount=20, randomize=True)
    session.interact_user_followers(['fitness'], amount=20, randomize=True)
    session.interact_user_followers(['fitness.union'], amount=20, randomize=True)
    session.interact_user_followers(['hotgirlsfitnessclub'], amount=20, randomize=True)
    session.interact_user_followers(['fitnessgirlsmotivation'], amount=20, randomize=True)

    session.like_by_tags(['fitness' ,'fitnessgirl' ,'workout','fitnessgirlsmotivation','fitnessgirlsmotivation','abs','healthy','fitnesslife','fitnessmotivation','fitnessmodel','fitnessaddict'], amount=20, media=None)


    session.like_by_locations(['31499759/rome-italy/'], amount=25)
    session.like_by_locations(['213385402/london-united-kingdom/'], amount=25)
    session.like_by_locations(['6889842/paris-france/'], amount=25)
    session.like_by_locations(['213387672/venice-california/'], amount=25)
    session.like_by_locations(['213296852/venice-italy/'], amount=25)
    session.like_by_locations(['212999109/los-angeles-california/'], amount=25)
    session.like_by_locations(['239069253/golds-gym/'], amount=25)


    session.unfollow_users(amount=300, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=60)

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
