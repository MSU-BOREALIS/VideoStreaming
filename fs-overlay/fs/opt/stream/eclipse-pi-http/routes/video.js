const os = require('os'),
      childProcess = require('child_process'),
      spawn = childProcess.spawn,
      spawnSync = childProcess.spawnSync,
      execSync = childProcess.execSync


const router = module.exports = require('node-async-router')()


/**
 * Returns {isRecording: true} if Pi is recording
 **/
router.get('/video', async (req, res) => {
  const isRecording = isPiRecording()

  res.json({ isRecording })
})


/**
 * Start video recording
 **/
router.get('/video/start', async (req, res) => {
  let isRecording = isPiRecording()

  // if we aren't recording, don't start a second process
  if (isRecording) {
    return res.status(500).json({
      success: false,
      error: 'Video recording is already active.'
    })
  }

  // start recording
  spawn('/home/pi/bin/start-recording.sh')

  // check again
  isRecording = isPiRecording()

  res.json({ success: isRecording })
})


/**
 * Stop video recording
 **/
router.get('/video/stop', async (req, res) => {
  const isRecording = isPiRecording()

  // if we're not recording, don't attempt to stop the process
  if (!isRecording) {
    return res.status(500).json({
      success: false,
      error: 'Video recording not in process.'
    })
  }

  // kill ffmpeg
  execSync('killall ffmpeg')

  res.json({ success: true })
})




/**
 * Helper function to determine if ffmpeg is running 
 **/
function isPiRecording() {
  const c = execSync('ps aux | grep -i ffmpeg | grep -v grep | wc -l'),
        isRecording = +c.toString()

  return !!isRecording
}
