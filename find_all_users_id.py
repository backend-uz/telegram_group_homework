from read_data import read_data

def find_all_users_id(data: dict)->list:
    """ 
    This function will find all the users in the json file and return the list of users id
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
    Returns:
        list: List containing all the users id
    """
    users = []
    data = data['messages']
    for i in data:
        if 'actor_id' in i:
            if i['actor_id'] not in 'channel1640165484':
                if i['actor_id'] not in users:
                    users.append(i['actor_id'])
        if 'from_id' in i:
            if i['from_id'] not in 'channel1640165484':
                if i['from_id'] not in users:
                    users.append(i['from_id'])
    return users
print(find_all_users_id(read_data('data/result.json')))