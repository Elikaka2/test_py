import requests

CAT_API_URL = "https://catfact.ninja/fact"

def get_cat_fact() -> dict:
    try:
        response = requests.get(CAT_API_URL, timeout=5)
        if response.status_code != 200:
            return {"error": f"Error: status code {response.status_code}"}

        data = response.json()
        fact = data.get("fact", "")
        is_small_fact = len(fact) < 70
        return {"fact": fact, "is_small_fact": is_small_fact}

    except requests.RequestException as e:
        return {"error": str(e)}
