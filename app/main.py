from fastapi import FastAPI
app = FastAPI()

@app.get('/')
def root():
    return """
    <!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Welcome</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      font-family: Arial, sans-serif;
      background: #f5f5f5;
    }

    .container {
      text-align: center;
      padding: 40px;
      background: white;
      border-radius: 12px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }

    h1 {
      font-size: 36px;
      margin-bottom: 10px;
    }

    p {
      font-size: 18px;
      color: #555;
    }
  </style>
</head>
<body>

  <div class="container">
    <h1>Welcome, Back we Did it. </h1>
    <p>Your project is running successfully.</p>
  </div>

</body>
</html>

"""