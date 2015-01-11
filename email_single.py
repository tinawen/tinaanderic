import argparse
import os
import requests

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='Send a one-off email.')
  parser.add_argument('--file', required=True, 
                      help='Basename of email file to send.')
  parser.add_argument('--to', required=True,
                      help='Address to send to.')
  parser.add_argument('--subject', required=True,
                      help='Subject for the email')
  args = parser.parse_args()

  key = os.environ['MAILGUN_KEY']

  email_html = open(os.path.join('emails', args.file + '.html')).read()
  email_text = open(os.path.join('emails', args.file + '.txt')).read()

  request_url = 'https://api.mailgun.net/v2/tinaanderic.com/messages'
  request = requests.post(request_url, auth=('api', key), data={
    'from': 'wedding@tinaanderic.com',
    'to': args.to,
    'subject': args.subject,
    'html': email_html,
    'text': email_text,
  })

  print 'Status: {0}'.format(request.status_code)
  print 'Body:   {0}'.format(request.text)
