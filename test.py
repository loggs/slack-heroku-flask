import app

def test_get_ip():
    assert app.get_ip({'remote_addr': '123.123.123.123'}) == '123.123.123.123'
    assert app.get_ip({'a': 'b'}) == ''
