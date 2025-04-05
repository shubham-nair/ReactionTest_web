# 🧠 Reaction Time Test Web App

A simple web-based reaction time test built with Flask. The app measures how fast a user can respond to visual cues and displays their results, making it a fun and interactive way to test reflexes.

## 🚀 Features

- Start screen with instructions  
- Randomized delay before the signal appears  
- Tracks reaction time in milliseconds  
- Displays results and allows multiple attempts  
- Clean and responsive UI with HTML/CSS  

## 📸 Screenshots

<!-- Add screenshots here, e.g. -->
<!-- ![Home Screen](screenshots/home.png) -->
<!-- ![Test Screen](screenshots/test.png) -->
<!-- ![Result Screen](screenshots/result.png) -->

## 🛠️ Tech Stack

- **Backend**: Python (Flask)  
- **Frontend**: HTML, CSS  
- **Templating**: Jinja2  

## 📁 Project Structure

```
ReactionTest_web-master/
│
├── app.py                   # Flask app
├── static/
│   └── style.css            # Stylesheet
├── templates/
│   ├── base.html            # Layout template
│   ├── index.html           # Landing page
│   ├── game.html            # Reaction test screen
│   └── result.html          # Results page
└── .idea/                   # IDE settings (can be ignored)
```

## 🧪 How to Run Locally

1. **Clone the repo**
   ```bash
   git clone <your-repo-url>
   cd ReactionTest_web-master
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask
   ```

4. **Run the app**
   ```bash
   python app.py
   ```

5. Open your browser and go to:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📌 Future Enhancements

- Store user scores across sessions  
- Add visual/audio distraction levels  
- Leaderboard or high-score tracking  

---

*Made with ❤️ using Python & Flask*
