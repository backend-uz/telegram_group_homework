from read_data import read_data
from find_all_users_id import find_all_users_id

def find_user_message_count(data: dict, users_id: str)->dict:
    """
    This function will find the user's message count.
    
    Parameters:
        data (dict): Dictionary containing the data of the json file
        user_id (list): User id of the user
    Returns:
        dict: Number of messages of the users
    """
    message = {}
    for i in users_id:
        message[i] = 0

    for msg in data['messages']:
        if msg['type'] == 'message':
            if msg['from_id']:#.startswith('user'):
                message[msg['from_id']] += 1
    return message

dict()
data = read_data('data/result.json')

print(find_user_message_count(data, find_all_users_id(data)))