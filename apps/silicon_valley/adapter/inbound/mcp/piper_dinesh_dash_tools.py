from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Dinesh")

@mcp.tool("myself")
async def introduce_myself() -> str:
    return (
        "파이드 파이퍼 개발자 디네시 추타이입니다. "
        "화면과 대시보드 등 사용자에게 보이는 영역을 맡습니다."
    )
