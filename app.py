from flask import Flask, request, jsonify
from analyze import analyze_trade_file

app = Flask(__name__)

@app.route('/analyze', methods=['GET'])
def analyze():
    date = request.args.get('date')  # Format: YYYYMMDD
    if not date or len(date) != 8:
        return jsonify({'error': 'Date format must be YYYYMMDD'}), 400

    year, month, day = date[:4], date[4:6], date[6:]
    try:
        analysis_path = analyze_trade_file('data', year, month, day)
        return jsonify({'message': 'Analysis complete', 'file': analysis_path})
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
