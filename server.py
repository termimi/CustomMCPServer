import logging
import json
import sys
from mcp.server.fastmcp import Context, FastMCP
from mcp.server.session import ServerSession

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    stream=sys.stderr
)
logger = logging.getLogger("MCP-Test-Server")
mcp = FastMCP("testServer",host="0.0.0.0",auth=None)

data = [
    {
        "First_Name" : "Nelson",
        "Last_Name": "Pereira",
        "Age": 21
    },
    {
        "First_Name": "Loic",
        "Last_Name": "Michoud",
        "Age": 20
    },
    {
        "First_Name": "Thijs",
        "Last_Name": "Ananta",
        "Age": 20
    }
]
json_string = json.dumps(data)
Users = json.loads(json_string)

@mcp.tool(
    name="Get_User_Info_With_Fisrt_Name",
    description="Get the info of a user with the first name provided"
)
def Get_User_Info_With_Fisrt_Name(first_name : str = None):
    for user in Users:
        if user['First_Name'] == first_name:
            return user
    return f"No users found for with the first name {first_name}"

mcp.run(transport="streamable-http")