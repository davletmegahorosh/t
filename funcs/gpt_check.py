from config import gpt_client
from user_edit import gpt_request
from db.quries import get_request

def check_topic(text):
    completion = gpt_client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system",
             "content": get_request() + " answer only True or False and no more words"},
            {"role": "user",
             "content": text }
        ],
        temperature=1,
    )
    result = completion.choices[0].message.content.lower()  # Convert to lowercase for case-insensitive comparison
    print(result)
    return result == 'true'
