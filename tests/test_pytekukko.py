"""Pytekukko tests."""

import os
from typing import Any, Dict, TypeVar

import pytest
from aiohttp import ClientSession

from pytekukko import Pytekukko

T = TypeVar("T", bound=Dict[str, Any])  # pylint: disable=invalid-name

FAKE_CUSTOMER_NUMBER = "00-0000000-00"
FAKE_PASSWORD = "secret"  # noqa: S105


def remove_set_cookie(response: T) -> T:
    """Remove ``Set-Cookie`` header from response."""
    response["headers"].pop("Set-Cookie", None)
    return response


@pytest.fixture(scope="module")
def vcr_config() -> Dict[str, Any]:
    """Get vcrpy configuration."""
    return {
        "before_record_response": remove_set_cookie,
        "filter_headers": ["Cookie"],
        # NOTE: this should be uncommented when upgrading vcrpy to a fixed > 4.1.1:
        #   https://github.com/kevin1024/vcrpy/issues/398
        #   https://github.com/kevin1024/vcrpy/pull/582
        #   https://github.com/kevin1024/vcrpy/pull/581
        # "filter_post_data_parameters": ["j_username", "j_password"],
    }


@pytest.fixture(name="client", scope="function")
async def fixture_client() -> Pytekukko:
    """Get a client."""
    return Pytekukko(
        session=ClientSession(),
        customer_number=os.environ.get(
            "PYTEKUKKO_CUSTOMER_NUMBER", FAKE_CUSTOMER_NUMBER
        ),
        password=os.environ.get("PYTEKUKKO_PASSWORD", FAKE_PASSWORD),
    )


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_login(client: Pytekukko) -> None:
    """Test login."""
    async with client.session:
        result = await client.login()
    assert result


@pytest.mark.asyncio
@pytest.mark.vcr
async def test_logout(client: Pytekukko) -> None:
    """Test logout."""
    # TODO(scop): would be better to test from a logged in session
    async with client.session:
        await client.logout()
    # No exception counts as success here
