#Author: Prajakta V Pendse

class CSV_Reader_For_Calculator:
    @staticmethod
    def get_numbers_from_file(file_name):
        results_list = []
        with open(file_name, "r") as file:
            # Do this to ignore the header
            header = file.readline()

            new_line = file.readline()

            while new_line:
                tokens = new_line.split(",")
                results_list.append([float(t) for t in tokens[:-1]])

                new_line = file.readline()
        return results_list
