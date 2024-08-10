import requests


def get_latest_user(digit_count, last=None, index=None, username=None):
    """
    Finds the latest Roblox user with a given number of digits in their ID.

    Args:
        digit_count (int): The number of digits in the user ID.
        last (str, optional): The last user ID found. Defaults to None.
        index (int, optional): The current index of the digit being checked. Defaults to None.
        username (str, optional): The username of the last user found. Defaults to None.

    Returns:
        None: Prints the latest user ID and username.
    """
    index = index or 0  # Set index to 0 if it's None
    last = last or ""  # Set last to an empty string if it's None
    if index != digit_count:
        # Generate user IDs based on the current index and last user ID
        user_ids = [
            last[:index] + str(i) + last[index + 1:] for i in range(10)
        ] if last else [str(i) + "0" * (digit_count - 1) for i in range(10)]

        # Make a POST request to the Roblox API to get user data
        response = requests.post("https://users.roblox.com/v1/users",
                                 json={
                                     "userIds": user_ids,
                                     "excludeBannedUsers": False
                                 })

        # Sort the user data by ID in descending order
        sorted_data = sorted(response.json()['data'],
                             key=lambda item: item['id'],
                             reverse=True)

        # Recursively call the function to check the next digit
        return get_latest_user(digit_count, str(sorted_data[0]["id"]),
                               index + 1, str(sorted_data[0]["name"]))
    else:
        # Print the latest user ID and username
        print(last)
        print(username)


get_latest_user(10)
