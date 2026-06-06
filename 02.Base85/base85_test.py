from .encode_decode import encode, decode

def test_encode():
    assert encode(b"") == b"", "Empty input"
    assert encode(b"1") == b"F#", "Single byte"
    assert encode(b"12") == b"F){", "Two bytes"
    assert encode(b"123") == b"F)}j", "Three bytes"
    assert encode(b"1234") == b"F)}kW", "Four bytes"
    print("Encode tests passed")


def test_decode():
    assert decode(b"")    == b"", "Empty input"
    assert decode(b"F#")  == b"1", "Decode 'F#'"
    assert decode(b"F){") == b"12", "Decode 'F){'"
    assert decode(b"F)}j")== b"123", "Decode 'F)}j'"
    assert decode(b"F)}kW")== b"1234", "Decode 'F)}kW'"
    print("Decode tests passed")


def test_combine():
    assert decode(encode(b"")) == b"", "Empty input"
    assert decode(encode(b"1")) == b"1", "Single byte"
    assert decode(encode(b"12")) == b"12", "Two byte"
    assert decode(encode(b"123")) == b"123", "Three bytes"
    assert decode(encode(b"1234")) == b"1234", "Four bytes"
    print("Combine tests passed")

    assert encode(decode(b"F#")) == b"F#", "Empty input"
    assert encode(decode(b"F#")) == b"F#", "Single byte"
    assert encode(decode(b"F){")) == b"F){", "Two bytes"
    assert encode(decode(b"F)}j")) == b"F)}j", "Three bytes"
    assert encode(decode(b"F)}kW")) == b"F)}kW", "Four bytes"
    print("Reversed combine tests passed")

def test_some_more():
    assert decode(encode(b"\x00\x00\x00\x00")) == b"\x00\x00\x00\x00", "All zeros block"
    assert decode(encode(b"\xFF\xFF\xFF\xFF")) == b"\xFF\xFF\xFF\xFF", "All 0xFF block"
    assert decode(encode(b"1234567")) == b"1234567", "4+3 bytes"
    assert decode(encode(b"12345678")) == b"12345678", "Two full blocks"
    assert decode(encode(b"A" * 100)) == b"A" * 100,  "Long repetitive data"
    print("Some more tests passed")

if __name__ == "__main__":
    test_encode()
    test_decode()
    test_combine()
    test_some_more()
    print("All tests passed")
