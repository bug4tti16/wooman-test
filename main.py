from fastapi import FastAPI


app=FastAPI()

account=[]

@app.get("/api/v1/check/")
async def check_account(accountStatus: int = 0):
    stat = {"accountStatus" : len(account)}
    if stat["accountStatus"]==0:
        account.append("abcd")
        return {
            "status" : "418",
            "statusMessage" : "Tea must be brewed (Redirecting to Accout creation)"
        }
    elif stat["accountStatus"]>0:
        return {
            "status" : "301",
            "statusMessage" : "User account found redirecting"
        }
