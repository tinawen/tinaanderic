from app import db
from app import Guest
import unicodedata
from sqlalchemy import asc
from sqlalchemy import desc
from jinja2 import Environment, PackageLoader
import os
import requests

def send_email(email_html, email_text, email):
  key = os.environ['MAILGUN_KEY']

  request_url = 'https://api.mailgun.net/v2/tinaanderic.com/messages'
  request = requests.post(request_url, auth=('api', key), data={
    'from': 'Tina and Eric\'s Wedding <wedding@tinaanderic.com>',
      'to': email,
      'subject': 'See you at Tina and Eric\'s Wedding!',
      'html': email_html,
      'text': email_text,
      })
  print 'Status: {0}'.format(request.status_code)
  print 'Body:   {0}'.format(request.text)
  print 'Sent to email %(email)s' % {'email': email}

def parse_and_send_email(name_list, email_list):
  if len(name_list) > 0:
    if len(name_list) > 1:
      # if there are more than 2 names with the same last name, change it to first_name and first_name last_name
      # so Shishke Bab and Donerke Bab turn to Shishke and Donerke Bab
      last_names = [n.split(' ')[-1] for n in name_list]
      # test to see if all last names are the same
      if all(last_name == last_names[0] for last_name in last_names):
        first_names = [' '.join(n.split(' ')[:-1]) for n in name_list]
        first_few_before_last = first_names[:-1]
        modified_first_name = ', '.join(first_few_before_last) + " and " + first_names[-1]
        group_name = modified_first_name + ' ' + last_names[0]
      else:
        group_name = ', '.join(name_list[:-1]) + " and " + name_list[-1]
    else: # name_list only has 1 element
      group_name = name_list[0]
    name = '%(group_name)s' % {'group_name': group_name}

    html_email = html_template.render(name=name)
    text_email = txt_template.render(name=name)
  if len(email_list) > 0:
    email_list = [unicodedata.normalize('NFKD', email).encode('ascii','ignore') for email in email_list]
    # testing
    # print "%(name)s will be getting save the date at %(email_list)s" % { 'name': name, 'email_list': email_list}
    # uncomment to actually send
    for email in email_list:
      send_email(html_email, text_email, email)
  else:
    print "Can't send email for group: there is no email ", name_list


if __name__ == "__main__":
  env = Environment(loader=PackageLoader('app', 'emails'))
  html_template = env.get_template('reminder.html')
  txt_template = env.get_template('reminder.txt')
  parse_and_send_email([u"Tina Wen", u"Eric Schuchman"], [u'tinawenbj@gmail.com', u'skirun13@gmail.com'])


