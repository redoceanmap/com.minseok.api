from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Gilfoyle")

@mcp.tool("myself")
async def introduce_myself() -> str:
    return (
        "파이드 파이퍼 시스템 아키텍트 버트람 길포일입니다. "
        "인프라와 서버를 도맡으며 시스템 운영과 보안을 책임집니다."
    )
