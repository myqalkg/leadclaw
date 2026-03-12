const ci = require('miniprogram-ci')
const path = require('path')

;(async () => {
  const project = new ci.Project({
    appid: 'wx88184ee025d38abb',
    type: 'miniProgram',
    projectPath: path.join(__dirname, 'src/miniprogram'),
    privateKeyPath: path.join(__dirname, 'private.wx88184ee025d38abb.key'),
    ignores: ['node_modules/**/*'],
  })

  try {
    const uploadResult = await ci.upload({
      project,
      version: '1.0.0',
      desc: 'Lead-Claw V5.5 稳定版发布 - 实时神价监控看板',
      setting: { es6: true, minify: true },
      onProgressUpdate: console.log,
    })
    console.log('--- UPLOAD SUCCESS ---')
    console.log(uploadResult)
  } catch (err) {
    console.error('--- UPLOAD FAILED ---')
    console.error(err)
  }
})()
