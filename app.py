# Telegram AGAJAYOFFICIAL 
#DONT CHANGE CREDIT 
#IF YOU CHANGE MY CREDIT,
from flask import Flask, request, jsonify
import requests
import json
import threading
from byte import Encrypt_ID, encrypt_api

app = Flask(__name__)

# Owner: @AGAJAYOFFICIAL

def load_tokens():
    try:
        # Owner: @AGAJAYOFFICIAL
        with open("jwt_token.json", "r") as file:
            data = json.load(file)
        tokens = [item["token"] for item in data]  
        return tokens
    except Exception as e:
        print(f"Error loading tokens: {e}")  # @AGXJCD
        return []

def send_friend_request(uid, token, results):
    # Owner: @AGAJAYOFFICIAL
    encrypted_id = Encrypt_ID(uid)
    payload = f"08a7c4839f1e10{encrypted_id}1801"
    encrypted_payload = encrypt_api(payload)

    url = "https://client.ind.freefiremobile.com/RequestAddingFriend"
    headers = {
        "Expect": "100-continue",
        "Authorization": f"Bearer {token}",
        "X-Unity-Version": "2018.4.11f1",
        "X-GA": "v1 1",
        "ReleaseVersion": "OB52",
        "Content-Type": "application/x-www-form-urlencoded",
        "Content-Length": "16",
        "User-Agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-N975F Build/PI)",
        "Host": "clientbp.ggblueshark.com",
        "Connection": "close",
        "Accept-Encoding": "gzip, deflate, br"
    }

    response = requests.post(url, headers=headers, data=bytes.fromhex(encrypted_payload))

    if response.status_code == 200:
        results["success"] += 1
    else:
        results["failed"] += 1

@app.route("/spam", methods=["GET"])
def spam():
    # API Owner: @AGAJAYOFFICIAL
    uid = request.args.get("uid")
    key = request.args.get("key")
    
    # Key validation by @JCDMOD
    if key != "OLFFH4X":
        return jsonify({
            "error": "Invalid or missing key 🔐",
            "owner": "@Sudipta209"
        }), 401
    
    if not uid:
        return jsonify({
            "error": "uid parameter is required",
            "owner": "@Sudipta209"
        }), 400

    tokens = load_tokens()
    if not tokens:
        return jsonify({
            "error": "No tokens found in spam_ind.json",
            "owner": "@Sudipta209"
        }), 500

    results = {"success": 0, "failed": 0}
    threads = []


#FreeFire #API #Automation #Gaming #Developer #Python #Flask #@JCDMOD
    for token in tokens[:110]:
        thread = threading.Thread(target=send_friend_request, args=(uid, token, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    total_requests = results["success"] + results["failed"]
    status = 1 if results["success"] != 0 else 2

    # Response from @agajayofficial
    return jsonify({
        "success_count": results["success"],
        "failed_count": results["failed"],
        "status": status,
        "owner": "@Sudipta209",
        "message": "API by @Sudipta209"
    })

if __name__ == "__main__":
    # Server by @AGXJCD
    app.run(debug=True, host="0.0.0.0", port=5000)
