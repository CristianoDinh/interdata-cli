import subprocess
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  #Enable CORS that Frontend could call API.

#1. API HomePage
@app.route('/')
def home():
    return render_template("index.html")

#2. API get list Buckets
@app.route('/buckets', methods=['GET'])
def list_buckets():
    try:
        # Run subprocess cli to get list buckets
        result = subprocess.run(['python', 'list_v3.py', '--allBuckets'], capture_output=True, text=True)

        # Check whether error running subprocess
        if result.returncode != 0:
            return jsonify({'error': result.stderr.strip()}), 500

        # Convert result(output) into each line list
        lines = result.stdout.strip().split("\n")

        # Find header index to eliminate content
        header_index = next(
            (i for i, line in enumerate(lines) if "Bucket Name" in line), None)
        if header_index is None or header_index + 1 >= len(lines):
            return jsonify([])  # Return empty data

        # Get list buckets from output
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

# 3. API get list objects in a specific Bucket
@app.route('/<bucket_name>/objects', methods=['GET'])
def list_objects(bucket_name):
    try:
        # Run subprocess cli to get list objects(in a 'bucket_name')
        result = subprocess.run(['python', 'list_v3.py', bucket_name, '--allObjects'], capture_output=True, text=True)

        # Check whether error running subprocess
        if result.returncode != 0:
            return jsonify({'error': result.stderr.strip()}), 500

        # Convert result(output) into each line list
        lines = result.stdout.strip().split("\n")

        # Find header index to eliminate content
        header_index = next((i for i, line in enumerate(lines) if "Object Name" in line), None)
        if header_index is None or header_index + 1 >= len(lines):
            return jsonify([])  # Return empty data

        # Get list objects from output
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


if __name__ == '__main__':
    app.run(debug=True)