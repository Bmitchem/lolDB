__author__ = 'bob'



def populate(json_file):
    MATCH_DATA = json.load(open(json_file))
    ri = RiotInterface()
    ri.upload_match_history(MATCH_DATA)

if __name__=='__main__':
    import os
    import json
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "RiotProject.settings")
    from armory import models
    print "Starting Population Script"
    import django
    import datetime
    from riot_api import RiotInterface
    ri = RiotInterface()
    django.setup()
    for i in range(1,9):
        starttime = datetime.datetime.now()
        print "uploading file: ", i
        populate('matches%s.json' % i)
        print "finished in ", datetime.datetime.now()-starttime

    print "updating champions"
    ri.update_champions()
    ri.update_items()
    ri.import_summoner_id_from_pull(25500646)


