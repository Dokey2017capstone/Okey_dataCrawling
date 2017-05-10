# -*- coding: utf-8 -*-
# 한글 주석을 사용하기 위함
import tweepy

consumer_key = 'consumer_key'
consumer_secret = 'consumer_secret'
access_token = 'access_token'
access_token_secret = 'access_token_secret'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

class MyStreamLstener(tweepy.StreamListener): #기존 tweepy의 streamListener의 오버라이딩
    def on_status(self, status):
        print (status.text)

    def on_error(self, status_code):
        if status_code == 420: #stream에 연결을 하지 못하는 에러가 발생하는 경우 False를 반환
            return False

if __name__ == '__main__':
    myStreamListener = MyStreamLstener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    myStream.filter(track=['hungry']) #트위터 stream 중에 []배열 안에 들어간 단어들이 있는 문장만을 필터링 해줌