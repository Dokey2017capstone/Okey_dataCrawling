# -*- coding: utf-8 -*-
# 한글 주석을 사용하기 위함
import tweepy

consumer_key = 'dtaZTGizIfBywqezjfZNgTUVf'
consumer_secret = 'UXij6NAtI768ZvNIKtGNpKdpqFNSbnDQFBRDMDGgxNVcObj9H3'
access_token = '861549072527663105-LAPA04xOkIu1Ntgll4oh1MHCsd2WVg2'
access_token_secret = 'hDFLO7NHeKsyrcKzS5CfDwFrYJxSmNqsloihOKtCZwaCU'

file = open('crawlData.txt', 'a')

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

dataLenght = 0

class MyStreamLstener(tweepy.StreamListener):  #기존 tweepy의 streamListener의 오버라이딩
    def on_status(self, status):
        if dataLenght==1000000:  #원하는 데이터의 수를 지정하기 위한 조건문
            return
        dataStr = status.text
        print (dataStr)  #데이터가 크롤링 되는 모습을 확인하기 위한 출력문
        file.write(dataStr.encode('utf-8'))
        ++dataLenght

    def on_error(self, status_code):
        if status_code == 420:  #stream에 연결을 하지 못하는 에러가 발생하는 경우 False를 반환
            return False

if __name__ == '__main__':
    myStreamListener = MyStreamLstener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)
    #트위터 stream 중에 []배열 안에 들어간 단어들이 있는 문장만을 필터링 해줌
    #파이썬은 기본적으로 문자열을 unicode로 인식함
    #키워드를 u'한글'으로 하게 되면 기본적으로 인식하는 문자 형태인 unicode로 변환하여 읽음
    #사용자들 간에 대화에서 많이 등장 할 만한 단어들인 "근데", "그냥", "했어"를 포함하는 트윗들을 읽어옴
    myStream.filter(track=[u'근데', u'그냥', u'했어'])