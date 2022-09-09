
import requests
from data import token, root_url, positive_codes, sentences

def get_update(root_url: str, token: str):

	# get info about new updates from users and converting from json to dictionary

	url = f'{root_url}{token}/getUpdates'
	res = requests.get(url)
	if res.status_code in positive_codes:
		return res.json()
	else:
		print(f'bad request {res.status_code}')


def get_data():

	# processing and saving data in corresponding variables

	response = get_update(root_url, token)
	message_id = response.get('result')[-1].get('message').get('message_id')
	last_messages_text = response.get('result')[-1].get('message').get('text')
	chat_id = response.get('result')[-1].get('message').get('chat').get('id')
	return chat_id, last_messages_text, message_id


def sentences_for_user(array_sentences: list, messages_text: str):
	
	# get list of sentences satisfy indicated user`s parameters and preparing result sentence for user

	matched_sentences = []
	result_sentences = ""

	for sentence in array_sentences:
		if messages_text in sentence:
			matched_sentences.append(sentence)

	if len(matched_sentences) == 0:
		result_sentences = 'no matches'
	if len(matched_sentences) == 1:
		result_sentences = matched_sentences[0]
	if len(matched_sentences) > 1:
		for match in matched_sentences:
			result_sentences += f"\n{match}\n"

	return result_sentences	


def create_message(chat_id: int, last_messages_text: str):
	
	# generate the data for sending to server

	result_sentences = sentences_for_user(array_sentences=sentences, messages_text=last_messages_text)
	data = {'chat_id': chat_id, 'text': result_sentences}

	return data


def send_message(root_url: str, token: str, data: dict):

	# sending message to user

	url = f'{root_url}{token}/sendMessage'
	send_message = requests.post(url, data)
	if send_message.status_code in positive_codes:
		return True
	else:
		print(f'bad request {send_message.status_code}')
