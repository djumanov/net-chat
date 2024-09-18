import json

# Xabarni JSON formatga o'tkazish
def format_message(sender_id, text):
    return json.dumps({
        'sender_id': sender_id,
        'text': text
    })
