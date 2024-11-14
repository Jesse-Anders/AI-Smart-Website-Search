import markdown
from flask import Flask, request, render_template
from lang_bot_build import tool_chain
from langchain_core.runnables import RunnableConfig


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    inquiry = ""  # Initialize inquiry as an empty string
    if request.method == "POST":
        inquiry = request.form["inquiry"]
        raw_result = tool_chain.invoke(inquiry, config=RunnableConfig())  # Get the raw result
        result = markdown.markdown(raw_result)  # Convert Markdown to HTML
    return render_template("index.html", result=result if result else "", inquiry=inquiry)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6000, debug=True, threaded=False)
