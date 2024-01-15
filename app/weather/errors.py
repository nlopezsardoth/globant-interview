from flask import make_response, jsonify
def build_error_response(error_message, status_code=400):
    """Builds a consistent error response with an informative message and status code."""
    return make_response(jsonify({
        'error': error_message
    }), status_code)
