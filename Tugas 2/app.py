from flask import Flask, render_template
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Load dataset iris
    df = sns.load_dataset("iris")

    # Analisis sederhana
    summary = df.describe().to_html(classes="table table-bordered")

    # Buat plot
    plt.figure(figsize=(6, 4))
    sns.histplot(df["sepal_length"], kde=True)
    plot_path = "static/plot.png"
    os.makedirs("static", exist_ok=True)
    plt.savefig(plot_path)
    plt.close()

    return render_template("index.html", summary=summary, plot_url=plot_path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
