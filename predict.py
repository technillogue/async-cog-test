import asyncio
from cog import BasePredictor
from typing import AsyncIterator


class Predictor(BasePredictor):
    async def setup(self):
        self.x = 2
        self.q = asyncio.Queue()
        self.out = asyncio.Queue()
        self.task = asyncio.create_task(self.work())

    async def work(self):
        while 1:
            n = await self.q.get()
            for i in range(10):
                await self.out.put(n + self.x + i)

    async def predict(self, y: int) -> AsyncIterator[int]:
        await self.q.put(y)
        for i in range(10):
            yield await self.out.get()
