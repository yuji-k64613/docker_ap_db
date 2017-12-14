url = process.env.HUBOT_JENKINS_URL
user = process.env.HUBOT_JENKINS_USER
password = process.env.HUBOT_JENKINS_PASSWORD
room = process.env.HUBOT_JENKINS_ROOM

module.exports = (robot) ->
  robot.respond /jenkins +([^ ]+) +([^ ]+)/i, (msg) ->
    command = msg.match[1]
    if command == 'build'
      project = msg.match[2]
      build_url = "#{url}/job/#{project}/build"
      msg.http(build_url)
        .auth(user, password)
        .post() (err, res, body) ->
          msg.send body

module.exports = (robot) ->
  robot.router.post "/jenkins/hook", (req, res) ->
    headers = req.headers
    payload  = req.body
    name = payload['name']
    status = payload['build']['status']
    phase = payload['build']['phase']
    if phase == 'FINALIZED'
      robot.send {room: room}, "[Jenkins] #{name} : #{status}"
    res.send 200
