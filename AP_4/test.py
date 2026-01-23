from flask import Flask, request, jsonify

# Task Ap4: Custom API Experiment using Webforms
# This simple API accepts form data via POST and returns it as JSON

app = Flask(__name__)

@app.route('/api/submit', methods=['POST'])
def submit_form():
    # Get data from the form (simulated)
    user_name = request.form.get('username')
    user_role = request.form.get('role')
    
    # Process the data (mock logic)
    response_data = {
        "status": "success",
        "message": f"User {user_name} with role {user_role} has been processed.",
        "api_version": "v1.0"
    }
    
    return jsonify(response_data)

if __name__ == "__main__":
    # Runs the app on port 5050
    app.run(host='0.0.0.0', port=5050)