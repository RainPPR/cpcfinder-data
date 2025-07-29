import common

def Main(path):
    pagination = common.fetch_json('https://cpcfinder.com/api/student')['pagination']
    total = pagination['total']
    data = common.fetch_json(f'https://cpcfinder.com/api/student?pageSize={total}&current=1')
    common.write_json(path, data)
