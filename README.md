# Travel Itinerary Planner

## 📝 Overview

Travel Itinerary Planner is an AI-powered web application built with Streamlit and CrewAI that helps users generate personalized travel itineraries. The application creates detailed day-by-day plans based on user preferences, including destination, duration, travel style, and specific interests.

## ✨ Features

- 🌎 Generate detailed travel itineraries for any destination worldwide
- 📅 Plan trips from 1 to 14 days in duration
- 🎨 Choose from various travel styles (Balanced, Cultural, Adventure, Relaxed, Budget-friendly, Luxury)
- 🔍 Personalize based on specific interests (History, Food, Art, Nature, etc.)
- 🚫 Specify experiences or places you want to avoid
- 💾 Download your itinerary for offline use

## 🚀 Demo

![Demo of the Travel Itinerary Planner](https://github.com/user-attachments/assets/88437ea0-3c0a-4af4-a896-64a2b749aa81)

## 🛠️ Technologies Used

- **Streamlit**: For the interactive web interface
- **CrewAI**: For AI-powered itinerary generation
- **LangChain**: For handling the LLM interactions
- **OpenAI**: The underlying language model

## 📋 Requirements

- Python 3.8+
- Streamlit
- CrewAI
- LangChain
- OpenAI API key

## ⚙️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/travel-itinerary-planner.git
   cd travel-itinerary-planner
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Set up your OpenAI API key:
   ```
   export OPENAI_API_KEY='your-api-key-here'  # On Windows use: set OPENAI_API_KEY=your-api-key-here
   ```

5. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

## 🧠 How It Works

1. The user inputs their travel details (destination, number of days, travel style)
2. The user can optionally specify interests and things to avoid
3. CrewAI's Travel Planner agent creates a detailed itinerary based on the inputs
4. The generated itinerary is displayed in the app and can be downloaded as a text file

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/) for the wonderful web app framework
- [CrewAI](https://github.com/joaomdmoura/crewAI) for the AI agent orchestration
- [LangChain](https://langchain.com/) for the LLM integration
- [OpenAI](https://openai.com/) for the powerful language models

---

⭐ **Enjoy planning your next adventure with AI assistance!** ⭐
