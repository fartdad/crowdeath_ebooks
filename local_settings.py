'''
Local Settings for a heroku_ebooks account. #fill in the name of the account you're tweeting from here.
'''

#configuration
MY_CONSUMER_KEY = puNs19ZVIDYBoSSMnb4dzqVhz
MY_CONSUMER_SECRET = ThFNOWH4zJ8rlsK4Zo3qFjHVbCEv8h8gDOxfFurPgtkkSLsk5Q
MY_ACCESS_TOKEN_KEY = 3252887558-QzPkNnScuWqRLYargsAkDvfoYLoKVlwqS0k4c5g
MY_ACCESS_TOKEN_SECRET = Docg6IAnBdLrfQqMYIUOyhskIk7PEiAqFQLah7o2CKem6

SOURCE_ACCOUNTS = ["@crow_death"] #A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. It should look like ["account1", "account2"]. If you want just one account, no comma needed.
ODDS = 4 #How often do you want this to run? 1/8 times?
ORDER = 2 #how closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = False #Set this to False to start Tweeting live
STATIC_TEST = False #Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = "butt.txt" #The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API.
TWEET_ACCOUNT = "@batmankisser420" #The name of the account you're tweeting to.
