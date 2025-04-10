from pydantic import BaseModel, HttpUrl
from typing import List

class Ranking(BaseModel):
    media: str
    title: str
    year: int
    url: HttpUrl
    id: str
    country: str

class RankingsList(BaseModel):
    rankings: List[Ranking]

class Album(BaseModel):
    rank: int
    artist: str
    title: str
    image: HttpUrl

class AlbumsList(BaseModel):
    albums: List[Album]
    ranking_id: str