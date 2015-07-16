jQuery ->


  History = window.History
  currentState = History.getState()
  url = $(this).attr('href')
  title = $(this).attr('title') || null

  if ! History.enabled
    false
