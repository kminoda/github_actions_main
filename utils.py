def my_util(data: dict) -> str:
    if not 'vehicle_name' in data.keys():
        return 'NaN'
    else:
        return data['vehicle_name']