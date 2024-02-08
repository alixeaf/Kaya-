import requests

def increase_points(username, password):
    login_url = "https://serfclick.net/login"
    increase_points_url = "https://serfclick.net/earn/serf"

    session = requests.Session()

    # Login
    login_data = {
        "login": AggzgGa1344,
        "password": 1234567890qwertyuiop,
        "button": ""
    }

    login_response = session.post(login_url, data=login_data)

    if login_response.status_code == 200 and "Dashboard" in login_response.text:
        print("Login successful!")
    else:
        print("Login failed. Please check your credentials.")
        return

    # Increase points
    points_data = {
        "button": ""
    }

    points_response = session.post(increase_points_url, data=points_data)

    if points_response.status_code == 200:
        print("Points increased successfully!")
    else:
        print("Failed to increase points. Please try again later.")

# Replace 'your_username' and 'your_password' with your actual credentials
increase_points("your_username", "your_password")
