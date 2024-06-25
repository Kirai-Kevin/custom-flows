

import os.path
import asyncio
from asyncflows import AsyncFlows

async def main():
    dirname = os.path.dirname(__file__)
    flow = AsyncFlows.from_file(
        os.path.join(dirname, "string_reversal.yaml")
    )

    result = await flow.set_vars(
        my_input="hahahah hihihih",
    ).run()
    print(result)

if __name__ == "__main__":
    asyncio.run(main())
