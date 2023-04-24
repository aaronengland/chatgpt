import openai

# class
class ChatGPT:
	def __init__(self, str_key):
		self.str_key = str_key
	def send_prompt(self, str_prompt):
		# save key
		openai.api_key = self.str_key
		completion = openai.ChatCompletion.create(
			model='gpt-3.5-turbo',
			messages=[
			{'role': 'user', 'content': str_prompt}
			]
		)
		# response
		str_response = completion.choices[0].message.content
		# return
		return str_response
