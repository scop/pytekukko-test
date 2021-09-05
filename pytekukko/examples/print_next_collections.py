#!/usr/bin/env python3

"""Print next collection dates."""

import asyncio

from pytekukko.examples import example_argparser, example_client


async def run_example() -> None:
    """Run the example."""

    client, cookie_jar, cookie_jar_path = example_client(
        example_argparser(__doc__).parse_args()
    )

    async with client.session:
        services = await client.get_services()
        for service in (x for x in services if x.next_collection):
            print(service.name, service.next_collection)
        if not cookie_jar_path:
            await client.logout()

    if cookie_jar_path:
        cookie_jar.save(cookie_jar_path)


def main() -> None:
    """Run example in event loop."""
    asyncio.get_event_loop().run_until_complete(run_example())


if __name__ == "__main__":
    main()
