from display import app

def test_header_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("h1").text == "Pink Morsel Sales Visualiser"

def test_chart_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#sales-chart")

def test_region_picker_present(dash_duo):
    dash_duo.start_server(app)
    assert dash_duo.find_element("#region-filter")