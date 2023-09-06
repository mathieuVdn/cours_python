import json


class StorageManager:
    def load_data(self, data_name):
        filename = self.get_filename(data_name)
        try:
            file = open(filename, "r")
            data = file.read()
            file.close()
            return json.loads(data)
        except FileNotFoundError:
            print(f"Le fichier {filename} n'a pas été trouvé")
            return None

    def save_data(self, data_name, data_content):
        filename = self.get_filename(data_name)
        data_str = json.dumps(data_content)
        file = open(filename, "w")
        data = file.write(data_str)
        file.close()

    def get_filename(self, data_name):
        return data_name + ".json"
