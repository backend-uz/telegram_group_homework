from read_data import read_data

def find_all_users_name(data: dict)->list:
    """
    This function will find all the users in the json file and return the list of users name.
 
    Parameters:
        data (dict): Dictionary containing the data of the json file.
    Returns:
        list: List containing all the users name.
    """
    names = []
    data = data['messages']
    for i in data:
        if 'actor' in i:
            if i['actor'] not in names:
                names.append(i['actor'])
        if 'from' in i:
            if i['from'] not in names:
                names.append(i['from'])
    return names
print(find_all_users_name(read_data('data/result.json')))
