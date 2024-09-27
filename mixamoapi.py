import requests

def get_gms_hash(api_key, character_id, anim_id):
    # Set the API endpoint
    api_endpoint = f"https://www.mixamo.com/api/v1/products/{anim_id}?similar=0&character_id={character_id}"

    # Set headers with API key
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
        "X-Api-Key": "mixamo2"
    }

    # Make a GET request to retrieve the animation details
    response = requests.get(api_endpoint, headers=headers)

    # Check if the response was successful
    if response.status_code == 200:
        data = response.json()
        gms_hash = data.get('details', {}).get('gms_hash', 'gms_hash not found')
        return gms_hash
    else:
        return f"Error: {response.status_code} - {response.text}"

def main():
    print("MixamoAPI v1")
    api_key = input("Enter your Mixamo API key: ")
    character_id = input("Enter the Character ID: ")
    anim_id = input("Enter the Animation ID: ")

    gms_hash = get_gms_hash(api_key, character_id, anim_id)
    print(f"GMS Hash: {gms_hash}")

if __name__ == "__main__":
    main()