FROM rocketchat/hubot-rocketchat:latest

ADD helloworld.coffee /home/hubot/scripts
ADD jenkins.coffee /home/hubot/scripts
RUN echo '["ping.coffee","jenkins.coffee"]' > /home/hubot/hubot-scripts.json
