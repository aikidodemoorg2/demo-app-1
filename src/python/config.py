	# Configuration files are a really frequent source of secrets

	import os

	'''Common Key Types with obvious names'''

	# AWS
	## AWS Access Key ID
	AWS_ACCESS_KEY_ID = '****3NWQ'

	## AWS Secret Access Key
	AWS_ACCESS_SECRET_KEY = 'UpUbsQANRHLf2uuQ7QOlNXPbbtV5fmseW/GgT5D/'

	# Google
	## GCP Credentials
	GCP_PRIVATE_KEY = '****----\n'

	## Google API Key
	GOOGLE_API_KEY = '****5MgM'

	## Slack App token
	SLACK_APP_TOKEN = '****b32b'

	## Slack OAuth Access Token
	SLACK_OAUTH_ACCESS_TOKEN = '****b5kY'

	## Slack Webhook
	SLACK_WEBHOOK = '****62DQ'

	# Facebook
	## Access Token
	FACEBOOK_ACCESS_TOKEN = '****KXBR'

	# Paypal
	## Braintree Access Token
	PAYPAL_BRAINTREE_ACCESS_TOKEN = 'access_token$production$x0lb8affpzmmnufd$3ea7cb281754b7da7eca131ef9642324'

	# Twilio
	## Twilio API Key
	TWILIO_API_KEY = '****6BA8'
	TWILIO_ACCOUNT_SID = 'ACXvJ0lkU-BhvkmBkZPUWAxExvPSF6s5En'
	TWILIO_APP_SID = 'APNLX3uzXotXDUKvurSeS95o8O3RpYuuy6'

	# Mailgun
	## Mailgun API Key
	MAILGUN_API_KEY = '****pdbI'

	# Okta
	## Okta API Key
	# TBD

	'''Common Key Types with obscure names'''

	## AWS Secret Access Key
	VAR_2 = 'UpUbsQANRHLf2uuQ7QOlNXPbbtV5fmseW/GgT5D/'

	## AWS MWS Auth Token
	VAR_3 = 'amzn.mws.f90f3ce6-9b5a-26a7-9a87-4ff8052be2ec'

	## Google Captcha
	VAR_7 = '6Lrjv_b_jgnybWRwKSn2P6lop58PGZ_NfewZWnRT'

	# Github
	## Github Personal Access Token
	VAR_8 = '88df97769ab3185f2c0b2a73fdae1b27d89409ca'

	## Github App
	VAR_9 = 'Iv1.3e3354ce147fd412'
	VAR_10 = '895b1da4051440395f90e1411c4a1150e423c922'

	## Github OAuth App
	VAR_11 = '2d7d90e5719c63788b50'
	VAR_12 = '74e7e1837a98c7e0e4cd7fcf8b955894465964ec'

	# Slack
	## Slack App
	VAR_13 = '730191371696.1410179799078'
	VAR_14 = 'f90dd63cdcb13662a6f4b008081c1524'

	## Slack Signing Secret
	VAR_15 = 'f0c8970d9c172fb35ec4c71aa536d401'

	## Slack Webhook

	# Stripe
	## Stripe Secret Key
	VAR_19 = 'sk_live_abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	## Stripe Publishable Key
	VAR_20 = 'pk_live_abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

	## Stripe Restricted Key
	VAR_21 = '****nB1O'

	# Facebook
	## Access Token
	VAR_22 = '****KXBR'

	# Square
	## Square Access Token
	VAR_23 = 'sqOatp-TDt6aBq8Z_Oup1JezKC1cK'

	## Square OAuth Secret
	VAR_24 = 'sq0csp-2WvLIfSstr6_FWefA3c p_oeTw0RtICeBsIlUTShsRo'

	# Paypal
	## Braintree Access Token
	VAR_25 = 'access_token$production$x0lb8affpzmmnufd$3ea7cb281754b7da7eca131ef9642324'

	# Mailgun
	## Mailgun API Key
	VAR_29 = '****pdbI'

	# Generic weak redis password
	REDIS_PASSWORD = 'redis'

	# Generic weak postgres password
	POSTGRES_PASSWORD = 'postgres'

	'''Generic Credentials with obscure names that flow into password sinks'''

	# Generic password
	SOURCE_1 = 'GYW2mMmpG327BtrdTnUL'

	# Generic weak password
	SOURCE_2 = 'redis'

	# Generic weak password - SECURITY: Load from environment variable
	# Never commit actual passwords to source control
	SOURCE_3 = os.getenv('POSTGRES_PASSWORD', None)
	if SOURCE_3 is None:
	    raise ValueError('POSTGRES_PASSWORD environment variable must be set. See .env.example for configuration.')

	# Generic app secret
	SOURCE_4 = 'ttn9Jb9ep2U4KvG9hq6e'

	# Generic api key
	SOURCE_5 = 'SGwJgqnZYzH945UBWnauBuKXKLEhq5Le'

	# Generic api key
	SOURCE_6 = '897f3b11-72f2-4c6f-9a9d-4750cdc609c6'

	# Generic api key
	SOURCE_7 = '7340ad40-09b3-11eb-adc1-0242ac120002'


	'''False Positives'''

	# Github Hashes

	## Obvious name
	GITHUB_COMMIT_SHA_HASH = '120ba2f7db8affd023e83964e5d8afbd10d20fe8' 

	## Less obvious name
	COMMIT_SHA = '637831c685a5f906c65d6af8389e7988619a3514'

	## Obscure name
	LATEST = '699865bd61fda628b0bea3080ae73d5f11572a74'

	# Public Keys

	## SSH RSA public key
	PUBLIC_KEY_SSH = 'AAAAB3NzaC1yc2EAAAADAQABAAAAgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe4eCZ0FPqri0cb2JZfXJ/DgYSF6vUpwmJG8wVQZKjeGcjDOL5UlsuusFncCzWBQ7RKNUSesmQRMSGkVb1/3j+skZ6UtW+5u09lHNsj6tQ51s1SPrCBkedbNf0Tp0GbMJDyR4e9T04ZZw==' 

	## Public key file
	PUBLIC_KEY_FILE = '-----BEGIN PUBLIC KEY-----\nMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCqGKukO1De7zhZj6+H0qtjTkVxwTCpvKe4eCZ0\nFPqri0cb2JZfXJ/DgYSF6vUpwmJG8wVQZKjeGcjDOL5UlsuusFncCzWBQ7RKNUSesmQRMSGkVb1/\n3j+skZ6UtW+5u09lHNsj6tQ51s1SPrCBkedbNf0Tp0GbMJDyR4e9T04ZZwIDAQAB\n-----END PUBLIC KEY-----' 