from this import d
from flask import Flask, render_template, request

from business.parking_service import ParkingService

app = Flask(__name__)

parking_service = ParkingService()

@app.route("/")
def hello_world():
    duration = request.args.get('duration')
    amount = "N/A"
    
    if duration and int(duration):
        duration = int(duration)
        amount = parking_service.calculate_parking_price(duration)
    return render_template('index.html', amount=amount)

if __name__ == "__main__":
    app.run()
