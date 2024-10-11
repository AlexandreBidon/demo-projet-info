from fastapi import FastAPI
import uvicorn

from router import user, movie, watchlist

app = FastAPI()

app.include_router(user.router)
app.include_router(movie.router)
app.include_router(watchlist.router)

uvicorn.run(app, host="0.0.0.0", port=8000)
