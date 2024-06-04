# tests/test_decorators.py

import pytest
from src.decorators import log

@log()
def add(x, y):
    return x + y

@log()
def raise_error():
    raise ValueError("Test error")

def test_add(capsys):
    result = add(1, 2)
    assert result == 3
    captured = capsys.readouterr()
    assert "add ok" in captured.out

def test_raise_error(capsys):
    with pytest.raises(ValueError):
        raise_error()
    captured = capsys.readouterr()
    assert "raise_error error: Test error" in captured.err

def test_log_to_file(tmpdir):
    log_file = tmpdir.join("test_log.txt")

    @log(filename=str(log_file))
    def add_to_file(x, y):
        return x + y

    add_to_file(1, 2)
    with open(str(log_file), 'r') as file:
        logs = file.read()
        assert "add_to_file ok" in logs

    @log(filename=str(log_file))
    def raise_error_to_file():
        raise ValueError("Test error to file")

    with pytest.raises(ValueError):
        raise_error_to_file()
    with open(str(log_file), 'r') as file:
        logs = file.read()
        assert "raise_error_to_file error: Test error to file" in logs
