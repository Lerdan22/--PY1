import json

INPUT_FILE = "input.csv"


def csv_to_list_dict(input_file) -> list[dict]:
        with open(input_file, 'r') as i_f:
            lines_list = i_f.read().split('\n')
            cells_list = [line.split(',') for line in lines_list]
            list_dict = [dict(zip(cells_list[0], cells_list[i])) for i in range(1, len(lines_list))]
        return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
