from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("api/v1/login", response_class=HTMLResponse)
async def password_input_page(request: Request):
    """Serve the password input page."""
    # Construct the path to the HTML file based on the project structure
    html_file_path = request.app.root_path + "/../templates/login.html"
    with open(html_file_path, "r") as file:
        password_input_page_html = file.read()
    return password_input_page_html

@app.post("api/v1/login/submit")
async def submit_password(pw: str):
    return {"pw" : pw}