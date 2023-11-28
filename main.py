from fastapi import FastAPI  # FastAPI import
from routers import charges
from routers import deals
from routers import pins
from starlette.middleware.cors import CORSMiddleware
import psutil
import subprocess
import threading

app = FastAPI()
app.include_router(charges.router)
app.include_router(deals.router)
app.include_router(pins.router)


app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://35.203.149.86", "http://35.203.149.86:80"],
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def printHello():
    return "Hello World"

# terminal_command = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"' #애플
# terminal_command = 'google-chrome --remote-debugging-port=9222  --user-data-dir=data_dir' #리눅스
# def target() :
#     proc = subprocess.call(terminal_command, shell=True);
# thread = threading.Thread(target=target)
# thread.start()
# thread.join(0)