from fastapi import Depends

from open_terminal.main import app, verify_api_key

@app.get(
    "/files/cwd",
    include_in_schema=False,
    dependencies=[Depends(verify_api_key)],
)
async def get_cwd():
    return {"cwd": "/home/"}

