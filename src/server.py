from dotenv import load_dotenv
# load the environment variables
load_dotenv("../.env")

from fastapi import FastAPI
from auth import router
import uvicorn
import os


app = FastAPI()
app.include_router(router=router.router)


if __name__ == "__main__":
    uvicorn.run(
        app,
        host = os.environ.get("HOST"),
        port = int(os.environ.get("PORT")))    
