import asyncio
import logging

import httpx
import yufang_first_package

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    print("Hello, World!")
    asyncio.run(do_http_request())
    print("Done")


async def do_http_request():
    response = httpx.get("http://10.166.51.190:10099/rrweb-service/test/getfile?a=123")
    # resjson = response.json()
    # resjson["name"] = 123  # 使用字典方式访问和修改
    # print(response.text, resjson["name"])
    # logger.info("HTTP request completed")
    print(yufang_first_package.get_answer())
    print(yufang_first_package.str)
    logger.info("HTTP request completed")


if __name__ == "__main__":
    main()
