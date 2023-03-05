import requests
import pandas as pd
import numpy as np

from pandas import json_normalize
import os
from sqlalchemy import create_engine
import psycopg2

class Service():
    
    def __init__(self):
        pass
    
    def etl(self, name):
        """
        Takes name as a string and sends request to 3 different api and extract data, then transform data.

        Returns the data for user as a JSON

        Load the data to database
        """

        agify_response_list = []
        genderize_response_list = []
        nationalize_response_list = []

        agify_url = f"https://api.agify.io?name={name}"
        genderize_url = f"https://api.genderize.io?name={name}"
        nationalize_url = f"https://api.nationalize.io?name={name}"

        agify_request = requests.get(agify_url)
        genderize_request = requests.get(genderize_url)
        nationalize_request = requests.get(nationalize_url)

        agify_response_list.append(agify_request.json())
        genderize_response_list.append(genderize_request.json())
        nationalize_response_list.append(nationalize_request.json())

        agify_df = pd.DataFrame.from_dict(agify_response_list)
        genderize_df = pd.DataFrame.from_dict(genderize_response_list)
        nationalize_df = pd.DataFrame.from_dict(nationalize_response_list)

        try:           
            nation = json_normalize(data=nationalize_df['country'].explode().tolist(), meta=['name'], record_prefix='country_')
        except:
            return " "
        
        agify_df = agify_df.drop(["count", "name"], axis=1)
        genderize_df = genderize_df.drop(["count","name"], axis=1)

        agify_df.set_index("age")
        genderize_df.set_index("gender")
        nation.set_index("country_id")
        
        genderize_df.rename(columns={"probability": "gender_probability"}, inplace=True)

        agify_dict = agify_df.to_dict()
        genderize_dict = genderize_df.to_dict()
        nationalize_dict = nation.to_dict()

        returner_dict = {}
        returner_dict.update(agify_dict)
        returner_dict.update(genderize_dict)
        returner_dict.update(nationalize_dict)

        return returner_dict