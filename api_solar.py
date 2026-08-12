from flask import Flask
import Solar_scraping # สมมติชื่อไฟล์สคริปต์ดึงข้อมูลของคุณ

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello! Server is running."

@app.route('/run-scraper')
def run_scraper():
    # เรียกฟังก์ชันดึงข้อมูลของคุณตรงนี้
    # Solar_scraping.main() 
    return "Scraper executed successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
