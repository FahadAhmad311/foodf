import streamlit as st
import google.generativeai as genai

# Step 1: Set up Streamlit Title
st.title("AI-Based Meal Recommendation Chatbot")
st.header("🍴 Ask the Meal Recommendation Chatbot")
st.write("🤖 This chatbot provides meal suggestions based on your question about food, health, weather, and activities.")

# Step 2: Set Gemini API Key
genai.configure(api_key="AIzaSyDSidoNcomuW42GcClUJQ1zbYOl0nZciAI")

# Step 3: Define Keywords and Contextual Hints (Optional)
FOOD_KEYWORDS = ["food", "meal", "eat", "diet", "nutrition", "calories", "dish", "recipe", "fruit", "juice", "vegetable"]
HEALTH_CONDITIONS = ["fever", "cold", "flu", "diabetes"]
WEATHER_TERMS = ["hot", "cold", "rainy", "summer"]
ACTIVITY_TERMS = ["exercise", "gym", "workout", "football"]

# Function to check if the query is related to food, health, weather, or activities (Optional)
def is_food_related(query):
    return any(keyword in query.lower() for keyword in FOOD_KEYWORDS + HEALTH_CONDITIONS + WEATHER_TERMS + ACTIVITY_TERMS)

# Step 4: Generate AI-Based Response
def generate_ai_response(user_query):
    if not is_food_related(user_query):
        return "🚫 Please ask only about food, health, weather, or post-activity nutrition."

    st.write("🧠 Generating AI-based meal recommendation...")

    # Define AI prompt for Gemini API
    ai_prompt = f"""
    You are an AI nutritionist chatbot that provides meal recommendations based on:
    - Health conditions (e.g., fever, cold, flu, diabetes)
    - Weather (e.g., hot, cold, rainy)
    - Physical activities (e.g., post-workout, gym, football)
    - User queries on food preferences and nutrition.

    Please generate an informative and friendly meal recommendation based on this query:
    "{user_query}"
    """

    # Call the Gemini API to generate the response
    model = genai.GenerativeModel("gemini-1.5-pro-latest")
    try:
        response = model.generate_content(ai_prompt)
        return response.text
    except Exception as e:
        return f"❌ Error in generating AI response: {str(e)}"

# Step 5: User Input and AI Recommendation
user_query = st.text_input("Enter your question (e.g., 'What should I eat after a workout in the summer?')")

if st.button("Get Recommendation"):
    if user_query:
        recommendation = generate_ai_response(user_query)
        st.write("🤖 **AI Recommendation:**")
        st.write(recommendation)
    else:
        st.write("🚫 Please enter a query to get a recommendation.")
