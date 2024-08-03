# Discord-Gacha-Bot
 
제비 뽑기를 하거나 팀을 짜주는 디스코드 봇입니다.  
<br>

# 목차
0. [사용하기 전 .env 파일 설정](#0-사용하기-전-env-파일-설정)  
1. [가챠](#1-가챠)  
    1-1. [혼자 모든 항목 작성](#1-1-혼자-모든-항목-작성)  
    1-2. [현재 음성채널에 함께 있는 모든 사람과 항목 작성](#1-2-현재-음성채널에-함께-있는-모든-사람과-항목-작성)  
    1-3. [모두와 함께 항목 작성](#1-3-모두와-함께-항목-작성)  
2. [팀짜기](#2-팀짜기)  
    2-1. [현재 음성채널에 함께 있는 모든 사람과 함께 팀짜기](#2-1-현재-음성채널에-함께-있는-모든-사람과-함께-팀짜기)  
    2-2. [원하는 사람을 선택 후 팀짜기](#2-2-원하는-사람을-선택-후-팀짜기)  
3. [마법의소라고동님](#3-마법의소라고동님)


--- 

<br>
<br>

# 0. 사용하기 전 .env 파일 설정
디렉토리 최상단에 .env 파일을 만들어 봇의 토큰과 봇을 사용하고자 하는 서버의 ID를 작성합니다.  
<img src="https://drive.google.com/uc?export=view&id=1XG1b3gTAVnsz09cgysHjoQ3KltGZtP0T">
  
파일 안에 봇의 토큰은 "TOKEN"에, 서버의 ID는 "GUILD_ID"에 작성합니다.  
만약 여러 서버에 작동하고 싶다면 쉼표','로 구분해서 작성합니다.  
<img src="https://drive.google.com/uc?export=view&id=1XOpHx6nmn55yZBwdh_5q77jrqI3D4CiS">

링크를 생성할 때 아래와 같은 권한이 필요합니다.  
> * SCOPES  
bot, applications.commands  
<br>
> * BOT PERMISSOINS  
View Channels, Send Message, Embed Links, Attach Files,  
Read Message History, Add Reactions, Use Slash Commands  

<br>

# 1. 가챠
여러 항목을 작성한 후 그 중 하나를 무작위로 뽑는 기능입니다.  
```
/가챠 type:[1, 2, 3]
```
type 변수에 1~3의 값을 입력하여 아래 3가지의 방식 중 하나를 선택합니다.  


## 1-1. 혼자 모든 항목 작성   
type에서 1을 선택했을 경우 이용할 수 있습니다.  
본인이 모든 항목을 별도의 메시지로 작성하여 하나를 추첨하는 방식입니다.  
<img src="https://drive.google.com/uc?export=view&id=1WvqHANrMTjkOWiaSYk9Poyyh5IK0MLyN">  


## 1-2. 현재 음성채널에 함께 있는 모든 사람과 항목 작성  
type에서 2를 선택했을 경우 이용할 수 있습니다.  
현재 음성채널에 함께 있는 사람들과 항목을 작성할 수 있습니다.  
음성채널에 들어가있지 않다면 이용할 수 없습니다.  
각각 하나의 항목만 작성할 수 있습니다.  
<img src="https://drive.google.com/uc?export=view&id=1WsLmdwmvXcqpaqG9wi4qyzzvQA57q_ro">


## 1-3. 모두와 함께 항목 작성
type에서 3을 선택했을 경우 이용할 수 있습니다.  
앞에 키워드('!')를 적어 서버에 있는 모든 사람들과 항목을 작성할 수 있습니다.  
각각 하나의 항목만 작성할 수 있습니다.  
<img src="https://drive.google.com/uc?export=view&id=1WuDdrjfzk8UYsJuYSyC_z9Ttm_cU7oHS">


<br>


# 2. 팀짜기  
서버에 있는 사람들로 팀을 짤 수 있습니다.  
```
/팀짜기 type:[1, 2] team_num:[2이상의 숫자]
```
type 변수에 1~2의 값을 입력하여 아래 2가지의 방식 중 하나를 선택합니다.  
team_num 변수에 2 이상의 값을 입력하여 뽑고자 하는 팀의 수를 정합니다.  

만약 사람 수가 홀수일 때 team_num이 짝수인 경우 (ex) 인원: 5명, 팀 수: 2팀) 3명, 2명으로 두 팀이 만들어집니다.  


## 2-1. 현재 음성채널에 함께 있는 모든 사람과 함께 팀짜기  
type에서 1을 선택했을 경우 이용할 수 있습니다.  
현재 음성채널에 함께 있는 사람들과 팀을 짤 수 있습니다.   
음성채널에 들어가있지 않다면 이용할 수 없습니다.  
<img src="https://drive.google.com/uc?export=view&id=1X7j4zHl1fUL4VAMLBVZ25i1iPPs5ZvCH">


## 2-2. 원하는 사람을 선택 후 팀짜기  
type에서 2를 선택했을 경우 이용할 수 있습니다.  
원하는 사람을 멘션으로 선택하여 팀을 짤 수 있습니다.  
<img src="https://drive.google.com/uc?export=view&id=1WtRhl9BQ7yZ1D5BmngYxKHWVU6kejx8i">

<br>


# 3. 마법의소라고동님
전지전능한 소라고동님께 여쭈어봅니다.  
```
/마법의소라고동님 question:[질문]
```
<img src="https://drive.google.com/uc?export=view&id=1X63aB2Z5M3vH0ciNKhTII8rymUpx0oxn">  

제가 지금 만들고 있는 디스코드 봇을 보고 곧 알게 될거라고 하시니 정말 위대하십니다.  
