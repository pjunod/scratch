from flask import Flask, redirect, request

from hashlib import md5

app = Flask("url_shortener")

mapping = {}


@app.route("/shorten", methods=["POST"])
def shorten():
    global mapping
    payload = request.json

    if "url" not in payload:
        return "Missing URL Parameter", 400

    hash_ = md5()
    hash_.update(payload["url"].encode())
    digest = hash_.hexdigest()[:5]

    if digest not in mapping:
        mapping[digest] = payload["url"]
        return f"Shortened: r/{digest}\n"
    else:
        return f"Already exists: f/{digest}\n"


@app.route("/r/<hash_>")
def redirect_(hash_):
    if hash_ not in mapping:
        return "URL Not Found", 404
    return redirect(mapping[hash_])


if __name__ == "__main__":
    app.run(debug=True)
