import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import joblib

app = FastAPI()

# Load the model
with open('phishing.pkl', 'rb') as model_file:
    phish_model_ls = joblib.load(model_file)

# ML Aspect
@app.get("/")
async def home():
    return HTMLResponse("""
    <html>
    <head>
        <title>Phishing Site Checker</title>
    </head>
    <body>
        <h1>Phishing Site Checker</h1>
        <form action="/predict/" method="get">
            <label for="url">Enter URL:</label><br>
            <input type="text" id="url" name="url"><br><br>
            <input type="submit" value="Check">
        </form>
    </body>
    </html>
    """)

@app.get("/predict/")
async def predict(url: str):
    X_predict = [url]
    y_Predict = phish_model_ls.predict(X_predict)
    result = "This is a Phishing Site" if y_Predict[0] == 'bad' else "This is not a Phishing Site"
    return HTMLResponse(f"<h2>Result:</h2><p>{result}</p>")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
