# Import the required module from the fyers_apiv3 package
from fyers_apiv3 import fyersModel

# Replace these values with your actual API credentials
client_id = "ABCDEFGH-100"  # this values to be replaced
secret_key = "XYZXYZXYZ"    # this values to be replaced
redirect_uri = "https://www.google.co.in/" 
response_type = "code"  #  This value must always be “code”
state = "anyvalue"   # we can send a random value. The same value will be returned after successful login to the redirect uri.

# Create a session model with the provided credentials
session = fyersModel.SessionModel(
    client_id=client_id,
    secret_key=secret_key,
    redirect_uri=redirect_uri,
    response_type=response_type
)

# Generate the auth code using the session model
response = session.generate_authcode()

# Print the auth code received in the response
print(response)



