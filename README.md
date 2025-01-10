# RealTime DATA Movie Recommendation System

This repository contains a **Movie Recommendation System** built using **Streamlit** and powered by **The Movie Database (TMDb) API**. The system recommends movies based on user input by leveraging **cosine similarity** and **text vectorization** techniques. The model is preprocessed and trained on real-time movie data fetched from the TMDb API.

---

## Features

- **Real-time Movie Data Fetching**: The system fetches movie data, credits, and keywords from the TMDb API to create a comprehensive dataset.
- **Text Vectorization**: Uses **CountVectorizer** to convert movie metadata into numerical vectors for similarity computation.
- **Cosine Similarity**: Computes similarity scores between movies to generate recommendations.
- **Interactive Web App**: Built with **Streamlit**, the app allows users to input a movie name and get 10 recommended movies along with their posters.
- **Movie Posters**: Displays movie posters fetched from the TMDb API for a visually appealing experience.

![image](https://github.com/user-attachments/assets/579ca2bd-126c-4304-9a6c-81a95ac4f8c5)

## How It Works

1. **Data Collection**:
   - The system fetches movie data (metadata, credits, and keywords) from the TMDb API.
   - The data is processed and stored in Pandas DataFrames for further use.

2. **Preprocessing**:
   - Text data (e.g., genres, overview, tagline) is preprocessed using **Porter Stemmer** and **CountVectorizer**.
   - The text is converted into numerical vectors for similarity computation.

3. **Model Development**:
   - **Cosine Similarity** is used to calculate the similarity between movies based on their vectorized features.
   - The similarity matrix is stored in a pickle file for quick access during recommendations.

4. **Recommendation System**:
   - Users input a movie name or select one from the dropdown list.
   - The system calculates the top 10 most similar movies and displays their titles and posters.

---

## Technologies Used

- **Python**: Primary programming language.
- **Streamlit**: For building the interactive web app.
- **Pandas**: For data manipulation and storage.
- **Requests**: For making API calls to TMDb.
- **Scikit-learn**: For text vectorization and cosine similarity computation.
- **NLTK**: For text preprocessing (Porter Stemmer).
- **Pickle**: For saving and loading the model and data.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/RealTime-MovieRecommender.git
   cd RealTime-MovieRecommender
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```
3. Set up your TMDb API key:
   Replace the api_key variable in the code with your own TMDb API key.
   You can get an API key from TMDb.

4. Run the Streamlit app:

```bash
streamlit run app.py
```
---

## Usage
 - Open the app in your browser.

 - Input the name of a movie or select one from the dropdown list.

 - Click on "Display The Recommendations" to see the top 10 recommended movies along with their posters.
---
## File Structure
```bash
movie-recommendation-system/
├── app.py                  # Main Streamlit application
├── movie_list.pkl          # Pickle file containing the movie list
├── similarity.pkl          # Pickle file containing the similarity matrix
├── techma.png              # Logo/image for the app
├── README.md               # This file
├── requirements.txt        # List of dependencies
```
---
## Techniques Used

1. **Data Fetching**:
   - Real-time data fetching from the TMDb API using `requests`.
   - Data is stored in Pandas DataFrames for easy manipulation.

2. **Text Vectorization**:
   - **CountVectorizer** is used to convert text data (e.g., genres, overview) into numerical vectors.
   - **Porter Stemmer** is used for stemming text to reduce words to their root form.

3. **Similarity Computation**:
   - **Cosine Similarity** is used to compute the similarity between movies based on their vectorized features.

4. **Model Persistence**:
   - The movie list and similarity matrix are saved as pickle files for quick loading during recommendations.

---

## Future Improvements

- **User Preferences**: Allow users to filter recommendations based on genres, release year, or ratings.
- **Advanced NLP**: Use more advanced NLP techniques like TF-IDF or Word2Vec for better text representation.
- **Deployment**: Deploy the app on a cloud platform for public access.
