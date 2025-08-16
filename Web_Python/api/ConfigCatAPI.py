import configcatclient
import dotenv
import json
import os


class ConfigCatAPI:

    dotenv.load_dotenv()

    CONFIGCAT_SDK_KEY: str = os.environ.get("CONFIGCAT_SDK_KEY")

    def __init__(self) -> None:
        if self.CONFIGCAT_SDK_KEY != None:
            self.configcat = configcatclient.get(self.CONFIGCAT_SDK_KEY)

    
    def schedule(self) -> dict:
        response = self.configcat.get_value("live_schedule", "")
        
        return json.loads(response)