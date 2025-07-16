import requests 

def get_cat_fact():
    """
    Connects to the API and returns a random cat fact.
    """
    # API URL
    api_url = "https://catfact.ninja/fact"
    print("Connecting to the API...")

    try:
        # requests makes a GET request to the API
        response = requests.get(api_url)
        
        #check if the request was successful
        response.raise_for_status()
        
        data = response.json()
        
        # get the fact from the response
        fact = data['fact']
        return fact

    except requests.exceptions.RequestException as e:
        # exception handling
        return f"Error: {e}"

if __name__ == "__main__":
    fact = get_cat_fact()
    
    print("\n🐾 Today fact about cats :")
    print(f"-> {fact}")
    print("Thank you for the fact!")