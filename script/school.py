import common

def Main(path):
    pagination = common.fetch_json('https://cpcfinder.com/api/school')['pagination']
    total = pagination['total']
    data = common.fetch_json(f'https://cpcfinder.com/api/school?pageSize={total}&current=1')['data']
    common.write_json(f'{path}.json', data)
    common.write_csv(f'{path}.csv', data)
