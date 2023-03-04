from flask import Flask, request, jsonify

app = Flask(__name__)

# The progress report table
progress_report = {
    'Math': {},
    'Science': {},
    'English': {},
    'Art': {},
    'PE': {},
    'Music': {},
    'History': {}
}

# Fetch a student's progress report entry
@app.route('/progress_report/<subject>/<student_name>', methods=['GET'])
def get_progress_report(subject, student_name):
    if subject in progress_report and student_name in progress_report[subject]:
        return jsonify(progress_report[subject][student_name])
    else:
        return jsonify({'error': 'Student or subject not found'})

# Insert a student's progress report entry
@app.route('/progress_report/<subject>/<student_name>', methods=['POST'])
def insert_progress_report(subject, student_name):
    if subject in progress_report:
        data = request.get_json()
        progress_report[subject][student_name] = data
        return jsonify({'message': 'Progress report updated'})
    else:
        return jsonify({'error': 'Subject not found'})

if __name__ == '__main__':
    app.run(debug=True)
