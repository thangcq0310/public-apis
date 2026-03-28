import re
import json

print("🔄 Đang trích xuất API từ README.md...")

# Đọc README.md
with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
apis = []
current_category = ''

for i, line in enumerate(lines):
    # Tìm category (## Category)
    if line.startswith('## '):
        current_category = line.replace('## ', '').strip()
        print(f"  📁 Danh mục: {current_category}")
    
    # Tìm API (dòng trong bảng)
    elif line.startswith('| [') and '](http' in line:
        try:
            # Parse: | [Name](url) | Description | Auth | HTTPS | CORS | ...
            parts = [p.strip() for p in line.split('|')]
            
            if len(parts) >= 7:  # Cần ít nhất 7 phần
                name_link = parts[1]  # [Name](url)
                desc = parts[2]
                auth = parts[3]
                https = parts[4]
                cors = parts[5]
                
                # Extract name từ [Name](url)
                name_match = re.search(r'\[(.+?)\]\((.+?)\)', name_link)
                if name_match:
                    name = name_match.group(1)
                    url = name_match.group(2)
                    
                    # Lọc API không hợp lệ
                    if name and url and desc:
                        apis.append({
                            'name': name,
                            'url': url,
                            'desc': desc,
                            'auth': auth,
                            'https': https,
                            'cors': cors,
                            'category': current_category
                        })
        except Exception as e:
            pass

print(f"✅ Tìm thấy {len(apis)} APIs")

# Lưu dữ liệu JSON
with open('apis_data.json', 'w', encoding='utf-8') as f:
    json.dump(apis, f, ensure_ascii=False, indent=2)
print(f"💾 Đã lưu vào apis_data.json")

# Lưu dữ liệu JS để search_apis.html có thể load trực tiếp
with open('apis_data.js', 'w', encoding='utf-8') as f:
    f.write('const apisData = ')
    json.dump(apis, f, ensure_ascii=False)
    f.write(';')
print(f"💾 Đã lưu vào apis_data.js")

# Kiểm tra lại file JSON
with open('apis_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    print(f"✅ Dữ liệu có thể đọc được: {len(data)} APIs")
    if len(data) > 0:
        print(f"   Ví dụ: {data[0]['name']} ({data[0]['category']})")
