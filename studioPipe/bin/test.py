import json
from studioPipe.api import studioShows
reload(studioShows)

ss = studioShows.Connect()

ss.create(na='Smy_hero',
        dn = 'My Hero',
        sn = 'MYH',
        tp = 'My Hero',
        ic = '/mnt/bkp/Icons gallery/new/137307632.jpg'
        )


d = ss.get(show_name='raja_and_rani')

print json.dumps(d, indent=4)

#print ss.hasShow('my_hero')

