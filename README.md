# 🌾 Crop Recommendation System 

This project is a web application that recommends the most suitable crop to grow based on various environmental factors. It leverages a pre-trained machine learning model to provide accurate and data-driven suggestions, helping farmers and gardeners optimize their yields. The application takes into account factors like nitrogen levels, phosphorus levels, potassium levels, temperature, humidity, pH, and rainfall to predict the best crop.

🚀 **Key Features**

*   **Interactive User Interface:** A user-friendly Streamlit interface allows users to easily input environmental parameters.
*   **Machine Learning Powered:** Utilizes a pre-trained Random Forest Classifier model for accurate crop recommendations.
*   **Data Visualization:** Interactive plots and charts provide insights into the data and prediction results.
*   **Real-time Prediction:** Provides instant crop recommendations based on user input.
*   **Custom CSS Styling:** Enhanced visual appeal with custom CSS for a better user experience.
*   **Model Persistence:** The trained model is saved and loaded using `joblib`, avoiding retraining on each application start.

🛠️ **Tech Stack**

*   **Frontend:**
    *   Streamlit: For building the web application interface.
    *   HTML/CSS: For custom styling and layout.
    *   Plotly: For interactive data visualization.
*   **Backend:**
    *   Python: The core programming language.
    *   joblib: For loading the pre-trained machine learning model.
    *   NumPy: For numerical operations and array manipulation.
    *   Pandas: For data manipulation and analysis.
    *   Scikit-learn: For machine learning model (RandomForestClassifier), data scaling (StandardScaler), and pipeline creation.
*   **Model Training:**
    *   Jupyter Notebook: For model development, training, and evaluation.
*   **Data Storage:**
    *   CSV file (`Crop_recommendation.csv`): For storing the training data.
    *   Pickle file (`crop_recommendation_model.pkl`): For storing the trained machine learning model.

📦 **Getting Started**

### Prerequisites

*   Python 3.6 or higher
*   pip package manager

### Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/MeetPujara/Crop-Prediction
    cd Crop-Prediction
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

### Running Locally

1.  **Run the Streamlit application:**

    ```bash
    streamlit run app.py
    ```

2.  **Open the application in your browser:**

    The application will typically be available at `http://localhost:8501`.

📂 **Project Structure**

```
crop-recommendation-system/
├── app.py                          # Main Streamlit application file
├── crop_prediction.ipynb           # Jupyter Notebook for model training and evaluation
├── crop_recommendation_model.pkl   # Pre-trained machine learning model
├── Crop_recommendation.csv         # Dataset for training the model
├── requirements.txt                # List of Python dependencies
├── README.md                       # Project documentation
└── venv/                           # Virtual environment directory (optional)
```

🤝 **Contributing**

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive messages.
4.  Push your changes to your fork.
5.  Submit a pull request.

📬 **Contact**

If you have any questions or suggestions, feel free to contact me at meetpujara02@gmail.com

💖 **Thanks**

Thank you for checking out this project! I hope it's helpful for you.

This is written by [readme.ai](https://readme-generator-phi.vercel.app/).
