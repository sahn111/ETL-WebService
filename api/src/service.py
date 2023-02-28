import requests
import pandas as pd

class Service():
    
    def __init__(self):
        self.UserOutput = None

    def get(self, name):
        """
        Returns the data for user as a JSON
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
        
        


        print(nationalize_df)

    def post(self):
        """
        Save user output to the database
        """
        

        
        pass