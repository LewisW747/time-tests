from times import compute_overlap_time, time_range
import pytest

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected


def test_overlap():
    large = time_range("2008-01-12 10:00:00", "2008-01-12 12:00:00")
    short = time_range("2010-01-12 13:30:00", "2010-01-12 14:45:00")
    expected = []
    assert compute_overlap_time(large, short) == expected

def test_touching_intervals():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 14:45:00")
    expected = []
    assert compute_overlap_time(large, short) == expected

def test_end_before_start():
    with pytest.raises(ValueError, match="End time cannot be before start time!"):
        large = time_range("2010-01-12 14:00:00", "2010-01-12 12:00:00")
    
