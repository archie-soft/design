import requests
import json

API_ENDPOINT = "http://localhost:5000/api"


def create_doc(title, content):
    url = f"{API_ENDPOINT}/documents"
    data = {"title": title, "content": content}
    response = requests.post(url, json=data)
    response.raise_for_status()
    # print("Document created:", response.json())


def get_docs():
    url = f"{API_ENDPOINT}/documents"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return data["documents"]


if __name__ == "__main__":
    create_doc(title="doc 1", content="this is document one")
    create_doc(title="doc 2", content="this is document two")
    docs = get_docs()
    print(json.dumps(docs, indent=2))
