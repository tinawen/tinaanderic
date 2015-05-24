# A tool for downloading the database into a csv file.

import sys

from app import Guest

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print 'Usage: db_to_csv.py /path/to/csv'
    sys.exit()
  guest_list_path = sys.argv[1]

  columns = [var for var in vars(Guest) if not var.startswith("_") and not var.istitle()]

  outfile = open(guest_list_path, 'w')
  outfile.write(','.join(columns))
  outfile.write('\n')
  for guest in Guest.query.all():
    outfile.write(','.join([unicode(vars(guest)[column]) for column in columns]).rstrip().encode('utf-8'))
    outfile.write('\n')
  outfile.close()
