# Movie Recommendation System

This repository contains the implementation of a movie recommendation system using collaborative filtering and content-based filtering approaches. The system leverages Python libraries for data preprocessing, exploratory data analysis (EDA), and model development, and it includes Flask deployment for web-based user interaction.

## Features

- **Collaborative Filtering**: Utilizes user-item interactions to recommend movies.
- **Content-Based Filtering**: Recommends movies based on item features like genres, keywords, etc.
- **Flask Deployment**: Provides a web interface for users to interact with the recommendation system.
- **Comprehensive EDA**: Includes Jupyter notebooks for detailed data analysis.

## Prerequisites

- Python 3.7+
- Jupyter Notebook
- Flask
- Libraries: `pandas`, `numpy`, `matplotlib`, `seaborn`, `sklearn`, `scipy`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd movie-recommendation-system
   ```
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

## Project Structure

```
movie-recommendation-system/
│
├── data/
│   ├── checksums.txt
│   ├── links.csv
│   ├── movies.csv
│   ├── movies.sql
│   ├── ratings.csv
│   ├── readme.txt
│   ├── tags.csv
│
├── models/
│   ├── __pycache__/
│   ├── templates/
│   │   ├── index.html
│   ├── app.py                # Flask deployment
│   ├── collaborative_model.py  # Converted from .ipynb
│   ├── content_based_model.py  # Converted from .ipynb
│
├── notebooks/
│   ├── collaborative_model.ipynb
│   ├── content_based_model.ipynb
│   ├── data_preprocessing.ipynb
│   ├── eda.ipynb
│   └── data/
│       ├── cleaned_data.csv
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Usage

1. **Data Preprocessing**:
   - Use `notebooks/data_preprocessing.ipynb` to clean and prepare the data.

2. **Exploratory Data Analysis**:
   - Analyze the dataset using `notebooks/eda.ipynb`.

3. **Model Training**:
   - Train collaborative filtering and content-based filtering models using the respective notebooks.
   - Converted Python scripts for deployment can be found in the `models/` folder.

4. **Run Flask App**:
   - Start the web application:
     ```bash
     python models/app.py
     ```
   - Open your browser and go to `http://127.0.0.1:5000`.

## Results

- Provides personalized movie recommendations based on user preferences and movie metadata.

## Future Work

- Add hybrid recommendation system.
- Integrate more advanced deep learning techniques.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements or bugs.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

---

Feel free to reach out for any questions or suggestions!
