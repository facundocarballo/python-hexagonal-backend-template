from bootstraps.fast_api import BootstrapApp

app = BootstrapApp.get()

@app.get("/ja")
async def ja():
    return {"message": "it can be done"}