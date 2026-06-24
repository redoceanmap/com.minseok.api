from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Hendricks")

@mcp.tool("myself")
async def introduce_myself() -> str:
    return (
        "파이드 파이퍼 CEO 리처드 헨드릭스입니다. "
        "미들아웃 압축 알고리즘을 만든 창업자로, 회사의 비전과 핵심 의사결정을 책임집니다."
    )
