import requests

# Using Classes and Methods to perform api testing
class MyJSON:
    def __init__(self, url):
        self.url = url

    # fetch the api status code
    def api_status_code(self):
        # response variable to store the api data
        response = requests.get(self.url)
        return response.status_code
    
    # fetch the entire api data
    def fetch_api_data(self):
        if self.api_status_code() == 200:
            return requests.get(self.url).json()
        else:
            return "ERROR - 404"
        
    # fetch the header data or meta information
    def fetch_headers(self):
        if self.api_status_code() == 200:
            response = requests.get(self.url)
            return response.headers
        else:
            return "ERROR - 404"

    # fetch data based on id
    def fetch_data_by_id(self, id):
        if self.api_status_code() == 200:
            # convert int to string
            # id = str(id)
            for data in self.fetch_api_data():
                if data['id'] == id:
                    print("TITLE: " , data['title'])
                    print("PRICE: ", data['price'])

    def test_api_data_by_id(self, id):
        if self.api_status_code() == 200:
            id = str(id)
            for data in self.fetch_api_data():
                if data['id'] == id:
                    if data['food_name'] == "Sweet":
                        print("Success, Food Name Matched")
                    else:
                        print("Wrong Food Name")
                else:
                    "No Data ID"

    def insert_data(self, data):
        if self.api_status_code() == 200:
            response = requests.post(self.url, json=data)
            if response:
                return True
            else:
                return False

    def count_total_foods(self, country):
        if self.api_status_code() == 200:
            counter = 0
            for data in self.fetch_api_data():
                if data['country'] == country:
                    counter += 1
            return counter
        else:
            return "ERROR 404"
                    


json_object = MyJSON("https://fakestoreapi.com/products")
data = {
"food_name": "Sweet",
"country": "India"
}
# print(json_object.api_status_code())
# print(json_object.fetch_api_data())
# print(json_object.fetch_headers())
# json_object.fetch_data_by_id(9)
# json_object.test_api_data_by_id(26)
