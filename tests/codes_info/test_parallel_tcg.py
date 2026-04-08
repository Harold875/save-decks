from app.codes_info.parallel_tcg import code_info, regions


def test_parallel_name():
    code = "CB-379,CB-240,3xCB-204"
    info = code_info(code)
    assert info.get("paragon") is not None
    assert info.get("paragon") == "Niamh, Wielder of Faith"


def test_parallel_not_fount():
    code = "asd-das-ads"
    info = code_info(code)
    assert info == None


def test_parallel_region():
    code = "CB-379,CB-240,3xCB-204"
    info = code_info(code)
    
    assert info.get("region") == regions.shroud.value
