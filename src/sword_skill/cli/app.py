from cyclopts import App

from sword_skill.skills.weather import app as weather_app

root_app = App()
root_app.command(weather_app)
