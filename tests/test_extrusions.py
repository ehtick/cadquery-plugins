from plugins.extrusions import extrusions


def test_e2020_basic():
    """
    Tests that the bare minimum functionality is working for e2020 extrusions.
    """

    s = extrusions.e2020(10)

    assert s.size() == 1
    assert s.solids().size() == 1
    assert s.solids().faces().size() == 67
    assert s.solids().vertices().size() == 130


def test_e2040_basic():
    """
    Tests that the bare minimum functionality is working for e2040 extrusions.
    """

    s = extrusions.e2040(10)

    assert s.size() == 1
    assert s.solids().size() == 1
    assert s.solids().faces().size() == 108
    assert s.solids().vertices().size() == 212


def test_e2080_basic():
    """
    Tests that the bare minimum functionality is working for e2040 extrusions.
    """

    s = extrusions.e2080(10)

    assert s.size() == 1
    assert s.solids().size() == 1
    assert s.solids().faces().size() == 190
    assert s.solids().vertices().size() == 376


def test_v2020_basic():
    """
    Tests that the bare minimum functionality is working for e2020 extrusions.
    """

    s = extrusions.v2020(10)

    assert s.size() == 1
    assert s.solids().size() == 1
    assert s.solids().faces().size() == 51
    assert s.solids().vertices().size() == 98


def test_v2040_basic():
    """
    Tests that the bare minimum functionality is working for e2040 extrusions.
    """

    s = extrusions.v2040(10)

    assert s.size() == 1
    assert s.solids().size() == 1
    assert s.solids().faces().size() == 84
    assert s.solids().vertices().size() == 164