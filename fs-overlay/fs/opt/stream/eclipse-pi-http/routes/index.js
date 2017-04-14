const fs = require('fs'),
      path = require('path')

module.exports = fs.readdirSync(__dirname)
  .filter(fileName => fileName.endsWith('.js') && fileName !== 'index.js' && !fileName.match('#'))
  .map(fileName => {
    //console.log(`[routes] Loading routes file: ${fileName}`)
    return require(path.join(__dirname, fileName))
})
