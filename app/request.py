import urllib.request,json
from .models import Quote

base_url = None

def configure_request(app):
    global base_url
   base_url= app.config['BLOG_API']

def get_quotes(id):
    '''
    Function that gets the json response to our url request
    '''
    get_quotes_url = base_url

    with urllib.request.urlopen(get_quotes_url) as url:
        get_quotes_data = url.read()
        get_quotes_response = json.loads(get_quotes_data)

        quotes = None

        if get_quotes_response['quotes']:
            quotes_list = get_quotes_response['quotes']
            quotes = process_quotes(quotes_list)
