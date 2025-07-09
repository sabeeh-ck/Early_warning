
# 🐾 Early Warning System for Wildlife Detection

An integrated web and vision-based system for early detection of wild animals near forest zones. This project aims to assist forest departments by improving wildlife monitoring, reducing human-animal conflict, and speeding up response times.

---

## 🚀 Features

### 🔧 Admin Module
- **Secure Login**: Only authorized personnel can access the dashboard.
- **Forest Division & Station Management**: Add/edit/manage divisions and their stations.
- **Animal Management**: Add and update species data and track sightings.
- **Officer Management**: Assign forest officers to divisions/stations.
- **User Complaints**: View and respond to citizen-submitted reports.
- **Notifications**: Send alerts to officers about sightings or emergencies.

### 🧑‍✈️ Forest Officer Module
- Monitor animal detections with email alerts.
- Manage and respond to public complaints.
- Track detection history and hotspot areas for smarter action.

### 📸 Camera Module
- Accepts video input (live or pre-recorded).
- Extracts frames and detects animals using **TensorFlow Inception v3**.
- Serves as the primary data source for the whole system.
- Built for continuous surveillance in forest zones.

---

## 🛠️ Tools & Technologies

### 🖥️ Frontend
- **HTML / CSS / JavaScript**: Clean UI for admin and officer dashboards.

### ⚙️ Backend
- **Python**: Backend logic and model integration.
- **MySQL**: Stores data on animals, locations, officers, and alerts.

### 🧱 Framework
- **Django**: Handles authentication, routing, and admin interface.

### 🧠 Machine Learning
- **TensorFlow (Inception v3)**: For deep learning-based animal detection.
- **OpenCV**: For frame extraction and video analysis.

### 💻 Development Environment
- **Windows OS**
- **PyCharm** for backend development
- **SQLYog** for managing MySQL databases

---

## 🧪 How It Works

1. Camera footage is fed into the system (live or recorded).
2. Frames are extracted using OpenCV.
3. Each frame is analyzed using Inception v3 (via TensorFlow).
4. If an animal is detected:
   - An alert is sent to assigned forest officers.
   - The detection is logged for analysis and future reference.

---

## 🛠️ Setup Instructions

> Make sure Python, MySQL, and pip are installed.

1. **Clone the repository**
   ```bash
   git clone https://github.com/sabeeh-ck/Early_warning.git
   cd Early_warning
   ```

2. **Set up virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database**
   - Create a MySQL database (name: `early_warning`)
   - Update `settings.py` with your DB credentials

5. **Run migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the app**
   - Admin Dashboard: `http://localhost:8000/admin`
   - Officer/Complaint Portal: `http://localhost:8000/`

---

## 📧 Contact

If you have feedback or want to contribute, feel free to open issues or pull requests!

---

## 🐍 License

This project is licensed under the MIT License — feel free to use and modify.
