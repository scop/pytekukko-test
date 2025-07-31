# Contributing to Pytekukko

- [Install pre-commit](https://pre-commit.com/#install) and enable it by
  installing its hook scripts:

  ```shellsession
  $ pre-commit install --hook-type pre-commit --hook-type commit-msg
  ```

  Do this before the first commit in your working dir.

- Set up a virtualenv of your liking (e.g. pyenv, pyvenv) and activate it,
  install our dev dependencies in it:

  ```shellsession
  $ python3 -m pip install -r requirements-dev.txt
  ```

-
