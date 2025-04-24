# Travel Itinerary Planner

![Travel Itinerary Planner Banner](https://via.placeholder.com/800x200?text=Travel+Itinerary+Planner)

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

## 🖥️ Code Structure

- `app.py`: Main application file with the Streamlit interface
- Functions are organized by responsibility:
  - `create_travel_planner_agent()`: Sets up the CrewAI agent
  - `setup_page_config()`: Configures Streamlit page settings
  - `apply_custom_css()`: Applies custom styling to the app
  - `collect_user_inputs()`: Gathers user preferences
  - `generate_itinerary()`: Creates the itinerary using CrewAI
  - `display_itinerary()`: Presents the itinerary to the user

## 🎨 Customization

- Modify the CSS in `apply_custom_css()` to change the app's appearance
- Add or remove travel styles and interests in the respective options lists
- Adjust the agent's parameters in `create_travel_planner_agent()` to fine-tune the generated itineraries

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgements

- [Streamlit](https://streamlit.io/) for the wonderful web app framework
- [CrewAI](https://github.com/joaomdmoura/crewAI) for the AI agent orchestration
- [LangChain](https://langchain.com/) for the LLM integration
- [OpenAI](https://openai.com/) for the powerful language models

## 📞 Contact

For questions or feedback, please open an issue or contact [your-email@example.com](mailto:your-email@example.com).

---

⭐ **Enjoy planning your next adventure with AI assistance!** ⭐