ボット用のユーザを作成する
ユーザ名: bot
パスワード: password
(ROLEをbotにする)

#
# hubotからJenkinsへのビルド設定
#
開発者
admin(リストからユーザを洗濯)
設定
APIトークンの取得
→4aac8e9aeca0930ab4a42b98ed8c05a4

グローバルセキュリティの設定
セキュリティを有効化
→off

CSRF対策
→off

# リモートAPIのテスト
curl -X POST --user admin:4aac8e9aeca0930ab4a42b98ed8c05a4 http://localhost:9090/job/sample02/build

# docker-compose.yml修正
- HUBOT_JENKINS_PASSWORD=4aac8e9aeca0930ab4a42b98ed8c05a4

# hubot再起動

# ビルド
→@bot jenkins build sample02

#
# Jenkisからhubotへのの通知設定
#
# プラグインダウンロード
Jenkinsの管理
プラグインの管理
Notification plugin
→再起動せずにインストール

# プラグイン設定
[プロジェクト]
設定
Job Notifications
Add Endpont
URL: http://hubot:8080/jenkins/hook

# 疎通確認
docker-compose exec jenkins curl -X POST http://hubot:8080/jenkins/hook

# ビルド
@bot jenkins build sample02
→[Jenkins] sample02 : SUCCESS
