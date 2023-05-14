import json

# Đường dẫn đến file GeoJSON
geojson_file = '../data/eq_data_30_days_m1.geojson'

# Đường dẫn đến file JSON kết quả
json_file = '../data/eq_data_30_days_m1.json'

# Đọc dữ liệu từ file GeoJSON
with open(geojson_file, encoding='utf-8') as f:
    geojson_data = json.load(f)

# Ghi dữ liệu vào file JSON
with open(json_file, 'w') as f:
    json.dump(geojson_data, f)