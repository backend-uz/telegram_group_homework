from read_data import read_data

def find_number_of_messages(data: dict)->int:
    """
    Get the total number of messages.

    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        int: Total number of messages.
    
    """
    data = data['messages']
    c = 0
    for i in data:
        if i['type'] == 'message':
            c += 1
    return c
print(find_number_of_messages(read_data('data/result.json')))