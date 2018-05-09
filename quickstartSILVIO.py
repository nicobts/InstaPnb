import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = ''
#insta_password = raw_input('inserisci la tua password: '
insta_password = ''


session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=True,
                  multi_logs=True,
                  )

try:
    session.login()

    #setup
    session.set_relationship_bounds(enabled=True,
				                    potency_ratio=-1.02,
				                    delimit_by_numbers=True,
				                    max_followers=10000,
				                    max_following=10000,
				                    min_followers=100,
				                    min_following=50)

    session.set_do_like(enabled=True, percentage=100)
    session.set_do_follow(enabled=True, percentage=80, times=1)

    #target

    session.set_user_interact(amount=3,randomize=False,percentage=100,media='Photo')

    session.interact_user_followers(['noelia.dp'], amount=170, randomize=False)

    #unfollow
    session.unfollow_users(amount=170, onlyInstapyFollowed = True, onlyInstapyMethod = 'FIFO', sleep_delay=30)


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
