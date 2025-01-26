from flask import Flask, request, render_template
from content_based_model import recommend_content_based
from collaborative_model import recommend_collaborative

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/recommend", methods=["POST"])
def recommend():
    movie = request.form["movie"]
    method = request.form["method"]  # User chooses "content" or "collaborative"
    
    if method == "content":
        recommendations = recommend_content_based(movie)
    elif method == "collaborative":
        recommendations = recommend_collaborative(movie)
    else:
        recommendations = ["Invalid method selected."]
    
    return render_template("index.html", recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)