from tableauscraper import TableauScraper as TS
import discord

class Covid19:

    def __init__(self) -> None:
        self.data = {}
    
    def getData(self):
        url = "https://public.tableau.com/views/SATCOVIDDashboard/1-dash-tiles?:embed=y&:showVizHome=no&:host_url=https%3A%2F%2Fpublic.tableau.com%2F&:embed_code_version=3&:tabs=no&:toolbar=no&:isGuestRedirectFromVizportal=y&:display_spinner=no&:loadOrderID=0"
        ts = TS()
        ts.loads(url)

        self.data['new'] = str(ts.getWorksheet("D_New").data.to_dict()['SUM(case_new)-alias'][0])
        self.data['death'] = str(ts.getWorksheet("D_Death").data.to_dict()['SUM(death_new)-alias'][0])
        self.data['newAll'] = str(ts.getWorksheet("D_NewACM").data.to_dict()['SUM(case_new)-alias'][0])
        self.data['deathAll'] = str(ts.getWorksheet("D_DeathACM").data.to_dict()['SUM(death_new)-alias'][0])
        self.data['medic'] = str(ts.getWorksheet("D_Medic").data.to_dict()['SUM(in_medicate)-alias'][0])
        self.data['recovAll'] = str(ts.getWorksheet("D_RecovACM").data.to_dict()['SUM(recovered_new)-alias'][0])
        self.data['updateTime'] = str(ts.getWorksheet("D_UpdateTime").data.to_dict()['max_update_date-alias'][0])

    def create_embed(self):
        embed = (discord.Embed(title='🏥   สถานการณ์ผู้ติดเชื้อ COVID-19 อัพเดทรายวัน', description=f'```css\n{self.data["updateTime"]}\n```', color=discord.Color.blurple())
                .add_field(name='จำนวนผู้ติดเชื้อรายใหม่', value=f'😷 {self.data["new"]}')
                .add_field(name='จำนวนผู้เสียชีวิตรายใหม่', value=f'💀 {self.data["death"]}')
                .add_field(name='รักษาหาย', value=f'😊 {self.data["medic"]}')
                .add_field(name='จำนวนผู้ติดเชื้อสะสม', value=f'{self.data["newAll"]}')
                .add_field(name='จำนวนผู้เสียชีวิตสะสม', value=f'{self.data["deathAll"]}')
                .add_field(name='รักษาหายสะสม', value=f'{self.data["recovAll"]}')
                .add_field(name='เพิ่มเติม', value='[Click](https://ddc.moph.go.th/covid19-dashboard/)'))
        return embed


if __name__ == "__main__":
    from pprint import pprint
    covid = Covid19()
    covid.getData()
    pprint(covid.data)


