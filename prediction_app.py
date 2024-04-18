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

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Phishing Site Checker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to bottom, #007bff, #000);
            margin: 0;
            padding: 0;
            color: #fff;
            height:100vh;
        }

        .container {
            max-width: 500px;
            margin: 100px auto;
            padding: 20px;
            background-color: rgba(255, 255, 255, 0.9);
            border-radius: 8px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            color: #333;
        }

        form {
            text-align: center;
        }

        label {
            font-weight: bold;
            color: #555;
        }

        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            margin-bottom: 15px;
            border-radius: 5px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        input[type="submit"] {
            background-color: #007bff;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<img src="https://futurevolve.com/uploads/college/logo/40749/thumb_BPIT_Logo.JPG" style="align:"center""/>

    <div class="container">
        <h1>Phishing Site Checker</h1>
        <form action="/predict/" method="get">
            <label for="url">Enter URL:</label><br>
            <input type="text" id="url" name="url"><br><br>
            <input type="submit" value="Check">
        </form>
    </div>
</body>
</html>


    """)

@app.get("/predict/")
async def predict(url: str):
    X_predict = [url]
    y_Predict = phish_model_ls.predict(X_predict)
    result = "❌This is a Phishing Site" if y_Predict[0] == 'bad' else "✅ This is not a Phishing Site"
    return HTMLResponse(f"<h1>{result}</h1>")

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
