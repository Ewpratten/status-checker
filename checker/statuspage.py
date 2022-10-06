
import requests


def publish_component_status(api_key: str, page_id: str, component_id: str, status: bool):
    print(f"Publishing status: {component_id} -> {status}")

    # Get all component statuses
    components = requests.get(f"https://api.statuspage.io/v1/pages/{page_id}/components", headers={
        "Authorization": f"OAuth {api_key}"
    })
    print(f"Components listing says: {components.status_code}")
    components = components.json()

    # Check the current status of the component in question
    current_published_ok = True
    for component in components:
        if component["id"] == component_id:
            current_published_ok = component["status"] == "operational"
            break

    # If the status code differs, update it
    if current_published_ok != status:
        print(f"Updating status to: {status}")
        update = requests.patch(f"https://api.statuspage.io/v1/pages/{page_id}/components/{component_id}", headers={
            "Authorization": f"OAuth {api_key}"
        }, json={
            "component": {
                "status": "operational" if status else "major_outage"
            }
        })
        print(f"Update status: {update.status_code}")
        if update.status_code != 200:
            print(f"Error: {update.text}")
