from handlers import validation

class Config:

    def __init__(self):

        # Default configuration settings [current, [valid_options]]
        self.config = {
            "Rounds": [5, [1, 100]],
            "Notifications": [True, [True, False]],
            "SaveScores": [True, [True, False]]
        }

    def load_config(self):
        try:
            file = open('files/config.txt', "r")
            line = file.readline()
            split = line.split(",")

            for i in range(len(split)):
                if not split[i] == "":
                    option = self.retrieve_config_list()[i]
                    self.config[option][0] = split[i]
            file.close()
        except:
            file = open('files/config.txt', "x")
            file.close()

    def update_config(self, key, value):
        success, output = validation.validate_to_bool(value)
        if success:
            self.config[key] = output
            self.__save_config()
            return True
        else:
            success, output = validation.validate_to_int(value)
            if success:
                self.config[key] = output
                self.__save_config()
                return True
        return False

    def __save_config(self):
        try:
            file = open('files/config.txt', "w")
            formatted_str = ""
            options = self.retrieve_config_list()

            for i in range(len(list(options))):
                value = self.config[options[i]][0]
                if value == True or value == False:
                    success, output = validation.bool_to_string(value)
                    if success:
                        formatted_str += output + ","
                else:
                    success, output = validation.int_to_string(value)
                    if success:
                        formatted_str += output + ","

            file.write(formatted_str)
            file.close()
        except:
            return False

    def retrieve_config_list(self):
        return list(self.config.keys())

    def retrieve_config(self, key):
        return self.config[key][0]

    def retrieve_config_options(self, key):
        return self.config[key][1]
