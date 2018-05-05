import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'criminalwriter'
insta_password = 'instagramcriminalwriter2016'

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
    session.set_user_interact(amount=3, randomize=True, percentage=50, media=None)
    #session.set_upper_follower_count(limit=5000)
    #session.set_lower_follower_count(limit = 300)
    #session.set_do_follow(enabled=True, percentage=20, times=2)
    #session.set_do_comment(True, percentage=25)
    #session.set_comments([u'Nice!! Check my works, tell me what do you think! 😃😃 Handmade bags made in Italy!  @{}' , u'Nice!! 😃😃✨💫 @{} ' , u'✨💫✨💫👍👍 @{}'] , media=None)
    #session.set_dont_include(['friend1', 'friend2', 'friend3'])
    #session.set_dont_like(['pizza', 'girl'])

    # actions
    #accounts:Mille_splendidi_libri_non_solo ,Lettriceperpassioneblog,Lacacciatricedilibri00 ,Viaggiandoconimieilibri ,Lamiaesperienzadalibri,Diunlibro, Libroza, Linconvenientediesserelettori, Libreriamo, Libriamociblog, Libri_di_cristallo, Langolodeilibri, Illibraioit, Liberamenteme_blog, Amante_di_libri, Libri_e_recensioni, L_officina_del_libro, Montagnadilibri, Leggo.libri, Lequazionedeilibri, Glinda_izabel
    session.interact_user_followers(['mille_splendidi_libri_non_solo'], amount=10, randomize=True)
    session.interact_user_followers(['lettriceperpassioneblog'], amount=10, randomize=True)
    session.interact_user_followers(['lacacciatricedilibri00'], amount=10, randomize=True)
    session.interact_user_followers(['viaggiandoconimieilibri'], amount=10, randomize=True)
    session.interact_user_followers(['lamiaesperienzadalibri'], amount=10, randomize=True)
    session.interact_user_followers(['diunlibro'], amount=10, randomize=True)
    #session.interact_user_followers([ 'aldieci' , 'amber_del_discipline' , 'bancomoda' , 'nfmshop','diecidiecinapoli','vicolo.official' ,'melonestore','glamourshopalessia','dolcelunashop' ], amount=5, randomize=True)
    #session.follow_user_followers([], amount=10, randomize=True, interact=True)
    session.like_by_tags(['libridaleggere' , 'leggere' , 'leggeresempre','scrittore','writer','booklover','bookstagram','editor','publishing','acquisti','bookcommunity','booklovers','lettura','reading','readings','books','libri','libro','book', 'volgofriuli','photography' , 'ernesthemingway'
     , 'festamobile' ,'igbooks','instabook'], amount=5, media=None)


#session.set_comments([u'😃😃💯💯  @{}'] , media=None)
#session.comment_by_locations(['6889842/paris-france/'], amount=50)
#session.comment_by_locations(['213050058/milan-italy/'], amount=50)
#session.comment_by_locations(['213385402/london-united-kingdom/'], amount=50)

    session.like_by_locations(['214560101/trieste-italy/'], amount=5)
    session.like_by_locations(['217395054/bari-italy/'], amount=5)
    session.like_by_locations(['214921690/ferrara-italy/'], amount=5)
    session.like_by_locations(['213050058/milan-italy/'], amount=5)
    session.like_by_locations(['683118252/bologna-italy/'], amount=5)
    session.like_by_locations(['213830427/catania-italy/'], amount=5)

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
