import datetime
import discord
from coinapi_rest_v1.restapi import CoinAPIv1

class Coin:

    def __init__(self) -> None:
        self.api = CoinAPIv1('E7094F68-ABFA-45C8-AFDF-7E15295ADAF5')
        self.data = {}
    
    def getData(self, base, quote):
        self.data = self.api.exchange_rates_get_specific_rate(base, quote)

    def create_embed(self):
        embed = (discord.Embed(title='🪙   ราคา Cryptocurrency อัพเดทรายวัน', description=f'```css\n{datetime.datetime.fromisoformat(self.data["time"][:-9]).ctime()}\n```', color=discord.Color.gold())
                .add_field(name='Base', value=f'{self.data["asset_id_base"]}')
                .add_field(name='Quote', value=f'{self.data["asset_id_quote"]}')
                .add_field(name='Rate', value=f'{self.data["rate"]}')
        )
        return embed


if __name__ == "__main__":
    from pprint import pprint
    coin = Coin()
    coin.getData('BTC', 'THB')
    pprint(coin.data)




