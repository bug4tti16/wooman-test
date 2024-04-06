from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app=FastAPI
samplepw="78739"
account=["78739"]

class LOGIN_DATA(BaseModel):
    pw : str

@app.get("/api/v1/check/")
async def check_account(accountStatus: int = 0):
    stat = {"accountStatus" : len(account)}
    if stat["accountStatus"]==0:
        return RedirectResponse("/api/v1/create-password.html")
    elif stat["accountStatus"]>0:
        return RedirectResponse("/api/v1/login.html")
    
@app.post("/api/v1/login")
async def login(d:LOGIN_DATA):
    if 4<len(d["pd"])<20:
        if d["pd"]==samplepw:
            return RedirectResponse("/api/v1/login/success.html")
        else:
            return {
                "status" : "401",
                "statusMessage" : "Login Failed"
                    }
    else:
        return{
            "status" : "400",
            "statusMessage" : "Incorrect Password Format"
        }
    