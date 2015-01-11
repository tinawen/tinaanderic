# A tool for uploading a csv guest list to the SQL database.
# WARNING! This will entirely wipe the database.

import sys

from app import db
from models import *

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print 'Usage: csv_to_db.py /path/to/csv'
    sys.exit()
  guest_list_path = sys.argv[1]

  print 'WARNING! Uploading a CSV will entirely wipe the database '
  print 'and replace it with the new contents.'
  confirm = raw_input('Are you sure you want to continue? [N/y]')
  if confirm.upper() != 'Y':
    print 'Okay, bailing out.'
    sys.exit()

  db.drop_all()
  db.create_all()
  
  num_added = 0
  for line in open(guest_list_path).xreadlines():
    line = line.split(',')
    name = line[0]
    group_id = int(line[1])
    primary = bool(line[2])
    email = line[3]
    db.session.add(Guest(group_id, name, email, primary))
    num_added += 1

  db.session.commit()
  print 'Added', num_added, 'records.'
