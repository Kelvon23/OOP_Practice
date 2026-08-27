import seasons

def test_object_created_successfully():
    date_obj=seasons.create_time_object("1990-10-09")
    assert(seasons.create_time_object("1990-10-09"))== date_obj

def test_input_validation():
    with pytest.raises(SystemExit):
        seasons.create_time_object("199A-10-09")
    with pytest.raises(SystemExit):
        seasons.create_time_object("1990/10-09")
    with pytest.raises(SystemExit):
        seasons.create_time_object("2028-10-09")
    
