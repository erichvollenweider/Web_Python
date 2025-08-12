import os
import time
import dotenv
import requests
from supabase import Client, create_client

class SupabaseAPI:

    dotenv.load_dotenv()

    SUPABASE_URL: str = os.environ.get("SUPABASE_URL")
    SUPABASE_KEY: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

    def featured(self) -> list:

        response = self.supabase.table("featured").select("*").execute()

        featured_data = []

        if len(response.data) > 0:
            for featured_items in response.data:
                featured_data.append(featured_items)

        print(featured_data)
        return featured_data
