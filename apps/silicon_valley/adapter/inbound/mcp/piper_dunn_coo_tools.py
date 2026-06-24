from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Dunn")

@mcp.tool("myself")
async def introduce_myself() -> str:
    return (
        "파이드 파이퍼 COO 도널드 '자레드' 던입니다. "
        "회사의 운영과 살림을 묵묵히 도맡는 비즈니스 책임자입니다."
    )
