from mattermostdriver import Driver
import datetime
import pytz
import httpx
import os

def lambda_handler(event, context):
    jst_timezone = pytz.timezone('Asia/Tokyo')
    today = datetime.datetime.now(jst_timezone).date()

    mm_url = os.environ['MM_URL']
    mm_bot_user_id = os.environ['MM_BOT_USER_ID']
    mm_bot_access_token = os.environ['MM_BOT_ACCESS_TOKEN']
    mm_news_channel_id = os.environ['MM_NEWS_CHANNEL_ID']
    news_api_top_url = os.environ['NEWS_API_TOP_URL']
    news_api_key = os.environ['NEWS_API_KEY']

    md = Driver({
        'url': mm_url,
        'login_id': mm_bot_user_id,
        'token': mm_bot_access_token,
        'scheme': 'https',
        'port': 443,
        'verify': False
    })

    msg = f'=====\*===== **Happy Daily News ! {today}** =====\*======\n'

    headers = {'X-Api-Key': news_api_key}
    params = {
        'category': 'business',
        'country': 'jp',
    }

    with httpx.Client() as client:
        response = client.get(news_api_top_url, headers=headers, params=params)
        response_json = response.json()
        articles = response_json['articles']

    for i in range(10):
        msg += f"- [{articles[i]['title']}]({articles[i]['url']})\n"

    msg += '=====\*=====\t\t\t\t\t\t\t\t\t\t\t\t\t\t=====\*======\n'

    md.login()
    md.posts.create_post(options={
        'channel_id': mm_news_channel_id,
        'message': msg
    })
    md.logout()

    return f"finished at {today}"
