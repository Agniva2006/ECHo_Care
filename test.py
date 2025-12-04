import requests

url = "https://api.murf.ai/v1/speech/voices"
headers = {"api-key": "ap2_363d87ae-d303-4aef-834b-6c0df5a15099"}

resp = requests.get(url, headers=headers)
print(resp.json())
murf_tts("Hello, this is EchoCare speaking warmly to you.", voice_id="en-IN-anisha")
