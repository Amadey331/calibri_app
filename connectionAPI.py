class DataAPI:


    def __init__(self):
        super(DataAPI, self).__init__()
        


    def add_api_data(self, data):
        with open("database/ApiData.txt", "w") as file:
            file.write(data)
