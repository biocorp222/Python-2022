import webbrowser

url = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
webbrowser.register('chrome',
	None,
	webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))
webbrowser.get('chrome').open(url)



