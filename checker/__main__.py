import json
import os
import sys
from checker.query.http import is_host_http_ok

from checker.query.ping import check_host_responds_to_pings
from checker.statuspage import publish_component_status

def main() -> int:
    
    # Load the statuspage API key
    sp_api_key = os.environ.get("STATUSPAGE_API_KEY")
    if not sp_api_key:
        print("$STATUSPAGE_API_KEY not set")
        return 1
    
    # Load the statuspage page ID
    sp_page_id = os.environ.get("STATUSPAGE_PAGE_ID")
    if not sp_page_id:
        print("$STATUSPAGE_PAGE_ID not set")
        return 1
    
    # Build handler map
    handlers = {
        "ping": check_host_responds_to_pings,
        "http_get": is_host_http_ok
    }
    
    # Handle each query
    with open("./queryset.json") as fp:
        data = json.load(fp)
        for entry in data:
            if entry["action"] in handlers:
                print(f"Checking: {entry['name']}")
                
                # Check if the host is up
                is_up = handlers[entry["action"]](entry["host"], **entry.get("kwargs", {}))
                print(f"Is up? {is_up}")
                
                # Push the status to statuspage
                publish_component_status(sp_api_key, sp_page_id, entry["component"], is_up)
                
            else:
                print(f"Unknown action: {entry['action']}")
                continue
            
    

    return 0

if __name__ == "__main__":
    sys.exit(main())