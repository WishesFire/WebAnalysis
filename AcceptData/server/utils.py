from datetime import datetime, timedelta


def prepare_info(_pages, cleaning=False):
    _visit_count_site = {}

    if cleaning:
        for page in _pages:
            _visit_count_site[_pages[page]] = 0
    else:
        future_time_loop = datetime.today() + timedelta(minutes=20)
        return future_time_loop
