import os
import requests
import random
import json

import asyncio

JENKINS_TOKEN = os.getenv('JENKINS_TOKEN')
JENKINS_URL = os.getenv('JENKINS_URL')

async def create_job():
    return 42

async def main():
    # Schedule nested() to run soon concurrently
    # with "main()".
    task = asyncio.create_task(nested())

    # "task" can now be used to cancel "nested()", or
    # can simply be awaited to wait until it is complete:
    await task

asyncio.run(main())