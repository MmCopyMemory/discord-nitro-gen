import requests

hh = "https://api.discord.gx.games/v1/direct-fulfillment"
hhs = {
    "accept": "*/*",
    "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
    "content-type": "application/json",
    "sec-ch-ua": "\"Opera GX\";v=\"105\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "cross-site"
}

h = {
    "partnerUserId": "cd8dc419c91d8884804707eae4c5302cf3b6f101fa30a1f530a52b1f0af472a4"
}
while True:
    try:
      a = requests.post(hh, headers=hhs, json=h)
      token = a.json().get("token", "")
      print("https://discord.com/billing/partner-promotions/1180231712274387115/" + token)
    except:
      w = ""