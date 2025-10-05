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
mcp = FastMCP("testServer")

data = [
    {
        "First_Name" : "Nelson",
        "Last_Name": "Pereira",
        "Age": 21
    },
    {
        "Fist_Name": "Loic",
        "Last_Name": "Michoud",
        "Age": 20
    },
    {
        "Fisrt_Name": "Thijs",
        "Last_Name": "Ananta",
        "Age": 20
    }
]
json_string = json.dumps(data)
Users = json.loads(json_string)

@mcp.tool()
async def Get_User_Info():
    pass






