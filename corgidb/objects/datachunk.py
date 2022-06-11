import csv
import json

class DataChunk:
    """
    Class to represent quired data

    Attributes:
        data (dict) : Dataframe like dictionary
    """

    def __init__(self, data: dict):
        """
        The constructor of DataChunk class

        Attributes:
            data (dict) : dataframe like dict
        """
        self.__data = data
        self.dict = data
        
    def saveas_csv(self, filepath: str):
        """
        Save DataChunk as CSV
        
        Parameters:
            filepath (str) : saving path
        """
        header = list(self.__data.keys())

        with open(filepath, 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            for i in range(len(self.__data[header[0]])):
                writer.writerow([self.__data[d][i] for d in header])


    def saveas_json(self, filepath: str):
        """
        Save DataChunk as CSV
        
        Parameters:
            filepath (str) : saving path
        """
        with open(filepath, "w") as jsonf:
            json.dump(self.__data, jsonf)

    
