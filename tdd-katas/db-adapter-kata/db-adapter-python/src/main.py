import uvicorn

from endpoint import app, router

# This is used to be able to run the Rest API from the shell
app.include_router(router)
uvicorn.run(app,host="0.0.0.0",port=8080)
