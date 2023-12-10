# Assignment - Product Reviews

Product reviews are evaluations or opinions shared by consumers who have purchased and used a specific product or service. These reviews are typically written on online platforms such as e-commerce websites, social media, or review websites.

Product reviews provide insights into customers' experiences, satisfaction levels, and perceptions of a particular product or service. In the context of NLP (Natural Language Processing), product reviews are a valuable source of text data that can be analyzed to extract sentiments, opinions, and insights.

DEPLOYED MODEL URL: https://okikimodel.onrender.com/

![image](https://github.com/iamfaqeehhokyky/modelDeployment/assets/73473767/8f466609-5b10-40bd-97ac-f5b3f955cee7)

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/iamfaqeehhokyky/modelDeployment.git
   ```
2. **Run the Jupyter Notebook**:
   ```bash
   sentiment-analysis-jumia-reviews.ipynb
   ```
3. **Select the Kernel to run the Notebook**:
   ```bash
   python 3.11.5
   ```
   After selcting the kernel and running the notebook, the models will be created for you to see and will be saved as `.pkl` files. There's the `sentiment_model.pkl` which is the sentiment model and the other is `count_vectorizer.pkl` which is for the vectorizer.

It's now time to see how our model run on the browser!

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
5. **Run the App**:
   ```bash
   flask run
   ```
6. **The App Running**:
   ```bash
   http://localhost:5000
   ```
7. **To Deploy The App**

```bash
ngrok http 5000
```

An Ngrok link will be auto generated which you can as well run on the browser to see your app and test the model.

## Usage

- Upon running the app, you'll have to enter the rating value, title of the review and the customer review statement.
- User can then click or select any of the listed Pokémon to see their details.

![image](https://github.com/iamfaqeehhokyky/modelDeployment/assets/73473767/19de1142-ed97-45fa-ad50-e76dfd4c1fae)

## `Good Luck! 🤝`
