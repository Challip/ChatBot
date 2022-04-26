

# Create a function that makes a REST request to the Text Translation service
def translate_text(text):
    import requests, uuid, json
    cog_key = '53d6da1822724ca58272f86413b2c3e3'
    cog_endpoint = 'https://translaateaaaa.cognitiveservices.azure.com/'
    cog_region = 'uksouth'
    path = 'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0'
    params = '&from={}&to={}'.format('en', 'de')
    constructed_url = path + params

    # Prepare the request headers with Cognitive Services resource key and region
    headers = {
        'Ocp-Apim-Subscription-Key': cog_key,
        'Ocp-Apim-Subscription-Region':cog_region,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    # Add the text to be translated to the body
    body = [{
        'text': text
    }]

    # Get the translation
    request = requests.post(constructed_url, headers=headers, json=body)
    response = request.json()
    return response[0]["translations"][0]["text"]



