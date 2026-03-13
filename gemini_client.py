from google import genai
from config import GEMINI_API_KEY

# configure gemini client
client = genai.Client(api_key=GEMINI_API_KEY)

def ask_gemini(message):

	try:
		response = client.models.generate_content(
			 model="gemini-2.5-flash",
		  	contents=f"Give short answer (max 4 to 5 sentences):{message} "
                )

		return response.text

	except Exception as e:
		return "Error: " + str(e)
