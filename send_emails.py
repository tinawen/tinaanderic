from app import db
from models import Guest
from sqlalchemy import func
import unicodedata

if __name__ == "__main__":
    guests_by_groups = db.session.query(func.string_agg(Guest.name, ', ')).group_by(Guest.group_id).all()
    for guest_group in guests_by_groups:
        # TODO(tina): should find the primary
        guest_names = ''.join(guest_group) # convert tuple into a string
        # convert unicode to string
        guest_names = unicodedata.normalize('NFKD', guest_names).encode('ascii','ignore')
        # replace the last ,  with and if it applies
        index = len(guest_names) - 1
        index_of_last_break = guest_names.rfind(', ', 0, index)
        if index_of_last_break > 0:
            guest_names = guest_names[:index_of_last_break - 1] + ' and ' + guest_names[index_of_last_break + 2:]
        print "Dear {}".format(guest_names)

