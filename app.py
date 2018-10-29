from flask import Flask, render_template, request
import requests
import json
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)
#user = 'huyrua291996'
time = '2018-10'

@app.route("/", methods=["GET", "POST"])
def helloWorld():
    pr_list = []
    pr_count = 0
    pr_enable = 0
    if request.method == "POST":
        user = request.form.get('user')
        re = requests.request("GET","https://api.github.com/search/issues?q=%20+type:pr+user:{}+created:{}".format(user, time))
        results = json.loads(re.text)
        for pr in results['items']:
            #print pr['pull_request']['html_url']
            pr_list.append(pr['pull_request']['html_url'])
        pr_enable = 1
        pr_count = len(pr_list)
    return render_template("checker.html", pr_list=pr_list, pr_count=pr_count, pr_enable=pr_enable)


app.run(debug=True)