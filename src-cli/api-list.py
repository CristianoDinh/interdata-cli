import subprocess
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Cho phép CORS để Angular có thể gọi API

# 2. API lấy danh sách buckets
@app.route('/buckets', methods=['GET'])
def list_buckets():
    try:
        # Gọi CLI để lấy danh sách bucket
        result = subprocess.run(['python', 'list_v3.py', '--allBuckets'], capture_output=True, text=True)

        # Kiểm tra lỗi khi chạy subprocess
        if result.returncode != 0:
            return jsonify({'error': result.stderr.strip()}), 500

        # Chuyển đổi output thành danh sách bucket
        lines = result.stdout.strip().split("\n")

        # Tìm vị trí header trong output
        header_index = next(
            (i for i, line in enumerate(lines) if "Bucket Name" in line), None)
        if header_index is None or header_index + 1 >= len(lines):
            return jsonify([])  # Trả về dữ liệu rỗng

        # Lấy danh sách buckets
        buckets = []
        for line in lines[header_index + 1:]:
            parts = line.split("|")
            if len(parts) == 3:
                bucket_id = parts[0].split(" ")[1]
                bucket_name = parts[0].split("] ")[1].strip()
                created_at = parts[1].strip()
                buckets.append(
                    {
                     "id": bucket_id,
                     "name": bucket_name,
                     "created_at": created_at
                     }
                )

        return jsonify(buckets)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 3. API lấy danh sách objects trong bucket
@app.route('/<bucket_name>/objects', methods=['GET'])
def list_objects(bucket_name):
    try:
        # Gọi CLI với bucket_name
        result = subprocess.run(['python', 'list_v3.py', bucket_name, '--allObjects'], capture_output=True, text=True)

        # Kiểm tra lỗi khi chạy subprocess
        if result.returncode != 0:
            return jsonify({'error': result.stderr.strip()}), 500

        # Chuyển đổi output thành danh sách objects
        lines = result.stdout.strip().split("\n")

        # Tìm vị trí header trong output
        header_index = next((i for i, line in enumerate(lines) if "Object Name" in line), None)
        if header_index is None or header_index + 1 >= len(lines):
            return jsonify([])  # Không có dữ liệu

        # Lấy danh sách objects từ output
        objects = []
        for line in lines[header_index + 1:]:
            parts = line.split("|")
            if len(parts) == 3:
                object_id = parts[0].split(" ")[1]
                object_name = parts[0].split("]")[1].strip()
                last_modified = parts[1].strip()
                objects.append(
                    {
                        "id": object_id,
                        "name": object_name,
                        "last_modified": last_modified
                    }
                )

        return jsonify(objects)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# 1. API HomePage
@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>Flask API</title>
            <style>
                body { font-family: cursive ; font-size: 60px; text-align: center; 
                        margin-top: 10px; background: gainsboro; }
                }
                h1 { color: #333; }
                ul { list-style-type: none; padding: 5px; font-family: monospace; }
                li { margin: 0; }
                a { text-decoration: none; color: blue; font-size: 24px; }
                a:hover { text-decoration: underline; }
                
                /* Đầu tiên, tạo keyframes cho hiệu ứng lắc */
                @keyframes shake {
                  0% { transform: translateX(0); }
                  25% { transform: translateX(-5px); }
                  50% { transform: translateX(5px); }
                  75% { transform: translateX(-5px); }
                  100% { transform: translateX(0); }
                }            
                /* Sau đó, áp dụng hiệu ứng lắc cho text */
                .shake-text {
                  display: inline-block;
                  animation: shake 0.5s ease-in-out infinite;
                }
            </style>
        </head>
        <body>
            <h1 class="shake-text">Flask API is Running!</h1>
            <ul>
                <li><a href="/buckets">📂 List all Buckets</a></li>
                <li><a href="/ex-bucket/objects">📄 List all Objects (replace 'ex-bucket')</a></li>
            </ul>
        </body>
    </html>
    """


if __name__ == '__main__':
    app.run(debug=True)