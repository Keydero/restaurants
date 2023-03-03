import pytest

from store_api.skeleton import main

__author__ = "Keyproco"
__copyright__ = "Keyproco"
__license__ = "MIT"








def test_main(capsys):
    """CLI Tests"""
    # capsys is a pytest fixture that allows asserts against stdout/stderr
    # https://docs.pytest.org/en/stable/capture.html
    main()
    captured = capsys.readouterr()
    assert "running" in captured.out
