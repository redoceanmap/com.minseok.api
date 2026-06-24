from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Bighetti")

@mcp.tool("myself")
async def introduce_myself() -> str:
    return (
        "파이드 파이퍼 인사 담당 넬슨 '빅헤드' 비게티입니다. "
        "사람과 인사(HR) 영역을 맡습니다."
    )
