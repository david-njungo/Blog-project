# import urllib.request,json
# from .models import Quote
# base_url = None

# def configure_request(app):
#     global base_url
#     base_url= app.config['BLOG_API']

# def get_quotes(random):
#     '''
#     Function that gets the json response to our url request
#     '''
#     get_quotes_url = base_url.format('random')

#     with urllib.request.urlopen(get_quotes_url) as url:
#         get_quotes_data = get_quotes_url.read()
#         get_quotes_response = json.loads(get_quotes_data)

#         quotes = None

#         if get_quotes_response['quotes']:
#             quotes_list = get_quotes_response['quotes']
#             quotes = process_quotes(quote_list)

# def process_quotes(quote_list):
#     '''
#     Function  that processes the news result and transform them to a list of Objects

#     Args:
#         quotes_list: A list of dictionaries that contain source details

#     Returns :
#        quotes: A list of source objects
#     '''
#     quotes = []
#     for quote_item in quote_list:
#         id = quote_item.get('id')
#         quote = quote_item.get('quote')
        
#         if quote:
#             quote_object = Quote(id,quote)
#             quotes.append(quote_object)

#     return quotes
