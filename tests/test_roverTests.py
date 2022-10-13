import pytest

from simple_mars_rover.MarsRover import MarsRover

testdata = [
    ('', '0:0:N'),
    ('L', '0:0:E'),
    ('LL', '0:0:S'),
    ('LLL', '0:0:W'),
    ('LLLL', '0:0:N'),
    ('LLLLL', '0:0:E'),
    ('LLLLLL', '0:0:S'),
    ('LLLLLLL', '0:0:W'),
    ('LLLLLLLL', '0:0:N'),
    ('R', '0:0:W'),
    ('RR', '0:0:S'),
    ('RRR', '0:0:E'),
    ('RRRR', '0:0:N'),
    ('RRRRR', '0:0:W'),
    ('RRRRRR', '0:0:S'),
    ('RRRRRRR', '0:0:E'),
    ('RRRRRRRR', '0:0:N'),
    ('M', '0:1:N'),
    ('MM', '0:2:N'),
    ('MMM', '0:3:N'),
    ('MMMM', '0:4:N'),
    ('MMMMM', '0:5:N'),
    ('MMMMMM', '0:6:N'),
    ('MMMMMMM', '0:7:N'),
    ('MMMMMMMM', '0:8:N'),
    ('MMMMMMMMM', '0:9:N'),
    ('MMMMMMMMMM', '0:0:N'),
    ('LLM', '0:9:S'),
    ('LLMM', '0:8:S'),
    ('LLMMM', '0:7:S'),
    ('LLMMMM', '0:6:S'),
    ('LLMMMMM', '0:5:S'),
    ('LLMMMMMM', '0:4:S'),
    ('LLMMMMMMM', '0:3:S'),
    ('LLMMMMMMMM', '0:2:S'),
    ('LLMMMMMMMMM', '0:1:S'),
    ('LLMMMMMMMMMM', '0:0:S'),
    ('LM', '9:0:E'),
    ('LMM', '8:0:E'),
    ('LMMM', '7:0:E'),
    ('LMMMM', '6:0:E'),
    ('LMMMMM', '5:0:E'),
    ('LMMMMMM', '4:0:E'),
    ('LMMMMMMM', '3:0:E'),
    ('LMMMMMMMM', '2:0:E'),
    ('LMMMMMMMMM', '1:0:E'),
    ('LMMMMMMMMMM', '0:0:E'),
    ('RM', '1:0:W'),
    ('RMM', '2:0:W'),
    ('RMMM', '3:0:W'),
    ('RMMMM', '4:0:W'),
    ('RMMMMM', '5:0:W'),
    ('RMMMMMM', '6:0:W'),
    ('RMMMMMMM', '7:0:W'),
    ('RMMMMMMMM', '8:0:W'),
    ('RMMMMMMMMM', '9:0:W'),
    ('RMMMMMMMMMM', '0:0:W'),
    ('MMRMMLM', '2:3:N')

]


@pytest.fixture
def mars_rover_commander():
    return MarsRover().execute


@pytest.mark.parametrize("command, expected", testdata)
def test_input_command_should_be_expected_result(command, expected, mars_rover_commander: MarsRover):
    assert mars_rover_commander(command) == expected
