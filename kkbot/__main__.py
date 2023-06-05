import glob 
from pathlib import Path 
from kkbot.utils import load_plug
import logging
from . import bot 


logging.basicConfig(format='[%(levelname) 5s /%(asctime)s] %(name)s: %(message)s' , level=logging.WARNING)

path = "kkbot/plugins/*.py"
files = glob.glob(path)

for name in files:
  with open(name) as a:
    pxt = Path(a.name)
    plug_name = pxt.stem
    load_plug(plug_name.replace(".py",""))
    
    
print("kkbot STARTED & LOADED ALL PLUGINS")

if __name__ == "__main__" :
  bot.run_until_disconnected()