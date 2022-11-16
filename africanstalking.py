# import package
import africastalking


# Initialize SDK
username = "techkiash"    
api_key = "ef5c9674d8423ab708659d6c38e0660c2edc993785cd9a1929497df5affc4179"     # use your sandbox app API key for development in the test environment
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


# Use the service synchronously
response = sms.send("Hello Message!", ["+254714128629"])
print(response)
