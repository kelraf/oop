
class User():
    def __init__(self):
        
        # A list to store users

        self.user_list = []

    def register(self, username, email, password):
        # A dictionary to store user
        user_details = {}

        user_details["username"] = username
        user_details["email"] = email
        user_details["password"] = password
        self.user_list.append(user_details)
        return user_details

def run():

    user = User()

    kelvin = user.register("Kelvin", "kelvin@gmail.com", "kelvin12")

    print(kelvin["email"])

if __name__ == "__main__":
    run()