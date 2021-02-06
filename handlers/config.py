from pathlib import Path

class Config:

    def __init__(self):

        # Default configuration options
        self.config = {
            "Rounds": [5, []],
            "Notifications": ["true", ["true", "false"]],
            "SaveScores": ["true", ["true", "false"]],
            "options": ["Rounds", "Notifications", "SaveScores"]
        }

    # Loads configuration via files when required. (For the game)
    def load_config(self):
        try:
            file = open('files/config.txt', "r")
            line = file.readline()
            split = line.split(",")

            for i in range(len(split)):
                if not split[i] == "":
                    option = self.config["options"][i]
                    self.config[option][0] = split[i]
            file.close()
        except:
            file = open('files/config.txt', "x")
            file.close()

    # Gets a particular configuration setting.
    def get_config(self, key):
        return self.config[key]

    # Updates the config value and saves it via the private __save_config function
    def update_config(self, key, value):
        self.config[key][0] = value
        self.__save_config()
        return

    # Saves the configuration set in self.config
    def __save_config(self):
        try:
            file = open('files/config.txt', "w")
            formatted_string = ""
            for i in range(len(self.config["options"])):
                formatted_string += str(self.config[self.config["options"][i]][0]) + ","
            file.write(formatted_string)
            file.close()
        except:
            return False


