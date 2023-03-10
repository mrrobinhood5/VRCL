from typing import Union
from base_classes import *
from dataclasses import dataclass
from motor.motor_asyncio import AsyncIOMotorDatabase, AsyncIOMotorCollection
from database import db



@dataclass
class DbInterface:
    db: AsyncIOMotorDatabase = db

    async def add_season(self, season: Season):
        _coll: AsyncIOMotorCollection = db['seasons']
        _update = {'$set': season.to_dict}
        await _coll.update_one(season.id, _update, upsert=True)
        return True
