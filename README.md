# pytekukko -- Jätekukko Omakukko API client

[![Python versions](https://img.shields.io/pypi/pyversions/pytekukko.svg)](https://pypi.org/project/pytekukko/)
[![PyPI version](https://badge.fury.io/py/pytekukko.svg)](https://badge.fury.io/py/pytekukko)
[![CI status](https://github.com/scop/pytekukko/workflows/check/badge.svg)](https://github.com/scop/pytekukko/actions?query=workflow%3Acheck)

Simple asyncio client for the [Jätekukko](https://www.jatekukko.fi)
[Omakukko](https://tilasto.jatekukko.fi/indexservice2.jsp) API.

Usage in a nutshell:

* construct an aiohttp `ClientSession`,
* construct a `Pytekukko` client with it and your credentials,
* invoke methods on the client.

The API uses cookie based sessions, use a persistent aiohttp
`CookieJar` to maintain client session across interpreter restarts.

High level client methods handle logging in when the need to do so is
detected. If the detection is successful, there is no need to
separately track session expiration or use the `login` method in the
first place.

For usage examples, see utilities in the `pytekukko.examples`
package. Executables and dependencies for these are installed when the
package is installed with the `examples` extra, invoke them with
`--help` for usage and setup information:

* `pytekukko-next-collections`: output next collection dates
* `pytekukko-update-google-calendar`: update Google Calendar with
  events for next collections
