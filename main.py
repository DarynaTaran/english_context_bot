
from data import token, root_url
from functions import get_data, create_message, send_message

last_message_id = 0

while True:
	chat_id, last_messages_text, message_id = get_data()

	data = create_message(chat_id, last_messages_text)

	if message_id > last_message_id:
		send_message(root_url, token, data)
		last_message_id = message_id
