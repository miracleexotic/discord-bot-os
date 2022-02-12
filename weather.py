import requests
import datetime
import discord

class Weather:

    def __init__(self) -> None:
        self.data = {}
    
    def getData(self):
        url = "https://api.openweathermap.org/data/2.5/weather?lat=13.736717&lon=100.523186&appid=6f0e002ab18f2962db0ce0de04615fbc&units=metric"
        resp = requests.get(url)
        self.data = resp.json()

    def create_embed(self):
        embed = (discord.Embed(title='สภาพอากาศ Thailand อัพเดทรายวัน', description=f'```css\n{datetime.datetime.fromtimestamp(self.data["dt"]).ctime()}\n```', color=discord.Color.green())
                .add_field(name='สภาพอากาศ', value=f'{self.data["weather"][0]["main"]} - {self.data["weather"][0]["description"]}')
                .add_field(name='อุณหภูมิ', value=f'🌡️ {self.data["main"]["temp"]} ํC')
                .add_field(name='ความรู้สึก', value=f'{self.data["main"]["feels_like"]} ํC')
                .add_field(name='ความกดอากาศ', value=f'{self.data["main"]["pressure"]}')
                .add_field(name='อุณหภูมิต่ำสุด', value=f'{self.data["main"]["temp_min"]} ํC')
                .add_field(name='ความเร็วลม', value=f'{self.data["wind"]["speed"]}')
                .add_field(name='ความชื้น', value=f'{self.data["main"]["humidity"]}')
                .add_field(name='อุณหภูมิสูงสุด', value=f'{self.data["main"]["temp_max"]} ํC')
                .add_field(name='สถานที่', value=f'{self.data["name"]}')
                .add_field(name='พระอาทิตย์ขึ้น', value=f'{datetime.datetime.fromtimestamp(self.data["sys"]["sunrise"]).ctime()}')
                .add_field(name='พระอาทิตย์ตก', value=f'{datetime.datetime.fromtimestamp(self.data["sys"]["sunset"]).ctime()}')
                .set_thumbnail(url=f'http://openweathermap.org/img/wn/{self.data["weather"][0]["icon"]}@2x.png')
        )
        return embed


if __name__ == "__main__":
    from pprint import pprint
    weather = Weather()
    weather.getData()
    pprint(weather.data)


