# AI-IT-Ticket-Classifier
# 🤖 AI IT Ticket Classifier

An AI-powered IT support ticket classification system built using **Python, Flask, SQLite, and Google's Gemini API**.

The application analyzes IT support requests, identifies their category and priority, detects sentiment, and generates suggested responses to help IT support teams handle tickets more efficiently.

## 📸 Screenshots

### 1. Home Page
The interface where users submit their IT support issues.

<img width="967" height="596" alt="Screenshot 2026-10-29 001737" src="https://github.com/user-attachments/assets/a01e32c8-9db1-4525-a283-2de84ad743e2" />



### 2. AI Classification Results
Displays the predicted category, priority, sentiment, and AI-generated suggested response.

<img width="848" height="942" alt="Screenshot 2026-10-29 001945" src="https://github.com/user-attachments/assets/cb3b6bdb-abe3-499d-bbf3-d782fb353cb6" />


### 3. Ticket History and Filters
View previously submitted tickets and filter them by category and priority.

<img width="997" height="655" alt="Screenshot 2026-10-29 002008" src="https://github.com/user-attachments/assets/2cdf5056-4fe3-41a6-a481-5c63317ec67b" />



### 4. Dashboard
Displays total tickets, priority counts, and a breakdown of tickets by category.

<img width="1161" height="851" alt="Screenshot 2026-10-29 002027" src="https://github.com/user-attachments/assets/0f52338b-902b-4257-a28c-e9ca78dc339c" />




## ✨ Features

- **AI-Powered Classification:** Classifies tickets into Hardware, Software, Network, Access, or Other.
- **Priority Detection:** Assigns Critical, High, Medium, or Low priority.
- **Sentiment Analysis:** Identifies Positive, Neutral, Negative, or Urgent sentiment.
- **Suggested Responses:** Generates practical responses to help resolve IT issues.
- **Ticket Management:** Saves submitted tickets and classification results in SQLite.
- **Ticket History:** Displays previously submitted support tickets.
- **Search and Filtering:** Filters tickets by category and priority.
- **Dashboard Analytics:** Displays total tickets, priority counts, and category statistics.
- **Input Validation:** Rejects empty or excessively long ticket descriptions.
- **Error Handling:** Displays user-friendly messages when AI classification fails.
- **Automated Testing:** Uses pytest to verify key application behaviors.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Backend web framework |
| Google Gemini API | AI-powered ticket classification |
| SQLite | Database for storing tickets |
| HTML | Web page structure |
| CSS | User interface styling |
| python-dotenv | Environment variable management |
| pytest | Automated testing |

## 📂 Project Structure

```text
AI-IT-Support/
├── app.py
├── classifier.py
├── database.py
├── test_classifier_manual.py
├── test_database.py
├── requirements.txt
├── .env
├── .gitignore
├── templates/
│   ├── index.html
│   ├── tickets.html
│   └── dashboard.html
├── tests/
   └── test_app.py

```

The `.env`, `tickets.db`, and `venv/` are local files and should not be committed to GitHub.

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.11 or another compatible Python version
- Git
- A Google Gemini API key
- Visual Studio Code or another code editor

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-IT-Support
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual repository URL.

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### Step 4: Configure the Gemini API

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=your_available_gemini_model
```

Replace the example values with your own API key and the model configured for your application.

**Important:** Never upload your API key or `.env` file to GitHub.

### Step 5: Run the Application

```bash
python app.py
```

Open the application in your browser:

- **Home Page:** http://127.0.0.1:5000
- **Ticket History:** http://127.0.0.1:5000/tickets
- **Dashboard:** http://127.0.0.1:5000/dashboard

The application initializes the SQLite database when it starts.

## 🔄 How It Works

1. The user enters an IT support ticket through the web interface.
2. Flask validates the ticket description.
3. The application sends the description to the Gemini API.
4. Gemini returns a structured classification containing the category, priority, sentiment, and suggested response.
5. The application validates the AI-generated result.
6. The ticket and classification details are saved in SQLite.
7. The classification result is displayed to the user.
8. Users can view ticket history, apply filters, and inspect dashboard statistics.

## 🧪 Testing

Run the automated test suite:

```bash
python -m pytest -v
```

The tests cover:

- Homepage loading
- Empty-ticket validation
- Ticket classification and database storage
- Graceful handling of AI service failures

The automated tests use a mocked classifier where appropriate, so they do not require a live Gemini API request for each test.

## 🔐 Security and Reliability

- API credentials are stored in environment variables.
- `.env`, virtual environments, and local database files should be excluded from version control.
- Parameterized SQL queries are used when inserting ticket data.
- Input validation limits the accepted ticket description length.
- AI responses are validated before being saved.
- Errors are logged on the server while users receive a friendly error message.

This is an educational project. Production deployment would require additional security controls, authentication, access management, monitoring, and deployment configuration.

## 🚀 Future Improvements

- Improve AI response time and retry handling.
- Add ticket status tracking and assignment.
- Implement user authentication and administrator roles.
- Add search by ticket description.
- Introduce more advanced analytics and visualizations.
- Deploy the application securely to a cloud platform.

## ⚠️ Disclaimer

AI-generated classifications and suggested responses may be inaccurate. Results should be reviewed by an IT support professional before being used to make operational decisions.

## 👨‍💻 Author

**Sunil Kumar**

B.Tech — Data Science

Project developed to explore Generative AI integration, backend development, database management, and automated testing.

---

⭐ If you find this project interesting, consider starring the repository!
