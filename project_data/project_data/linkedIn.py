from linkedin_api import Linkedin


class LinkedInProfileFetcher:
    """
    A class to interact with the LinkedIn API to fetch user profiles.

    Attributes:
        email (str): The email used to log in to LinkedIn (optional if using cookies).
        password (str): The password used to log in to LinkedIn (optional if using cookies).
        cookies (str): LinkedIn session cookies for authentication (optional if using email/password).
    """

    def __init__(self, email=None, password=None, cookies=None):
        """
        Initializes the LinkedInProfileFetcher with email/password or session cookies.

        Args:
            email (str): LinkedIn account email (optional if using cookies).
            password (str): LinkedIn account password (optional if using cookies).
            cookies (str): LinkedIn session cookies (optional if using email/password).
        """
        self.email = email
        self.password = password
        self.cookies = cookies
        self.api = None

        try:
            if cookies:
                self.api = Linkedin(cookies=cookies)
                print("Successfully logged in with session cookies.")
            elif email and password:
                self.api = Linkedin(email, password)
                print("Successfully logged in with email and password.")
            else:
                raise ValueError("You must provide either email/password or session cookies.")
        except Exception as e:
            print(f"Error initializing LinkedIn API: {e}")
            self.api = None

    def get_profile(self, profile_id):
        """
        Fetches the LinkedIn profile for the given profile ID.

        Args:
            profile_id (str): The profile ID of the LinkedIn user to fetch.

        Returns:
            dict: The profile data retrieved from LinkedIn, or None if an error occurs.
        """
        if not self.api:
            print("Login failed. Cannot fetch profile.")
            return None

        try:
            profile = self.api.get_profile(profile_id)
            print("Profile fetched successfully.")
            return profile
        except Exception as e:
            print(f"Error fetching profile: {e}")
            return None


# Example Usage
if __name__ == "__main__":
    # Replace with your credentials or session cookies
    EMAIL = "your_email@example.com"
    PASSWORD = "your_password"
    COOKIES = None  # Add your session cookies here if available

    # Create an instance of LinkedInProfileFetcher
    fetcher = LinkedInProfileFetcher(email=EMAIL, password=PASSWORD, cookies=COOKIES)

    # Test fetching a LinkedIn profile
    PROFILE_ID = "example_profile_id"  # Replace with a valid LinkedIn profile ID
    profile_data = fetcher.get_profile(PROFILE_ID)

    # Display the profile data
    if profile_data:
        print(profile_data)
    else:
        print("Failed to fetch profile.")
