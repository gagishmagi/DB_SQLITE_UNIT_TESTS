from db_queries import get_all_persons


def test_get_all_persons():
    # print(get_all_persons())
    # assert get_all_persons()[0] == (1, 'AL Mishu', 'Mishu', 'Dhaka', 'Dhaka')
    assert get_all_persons()[0][2] == 'Mishu'