# notifications/utils.py
from pyfcm import FCMNotification

def send_notification(expo_token, title, body):
    push_service = FCMNotification(api_key="<your_firebase_server_key>")
    message_title = title
    message_body = body
    result = push_service.notify_single_device(registration_id=expo_token, message_title=message_title, message_body=message_body)
    return result
