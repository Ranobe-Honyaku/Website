from kyoukai import Kyoukai, KyoukaiComponent
from asphalt.core import ContainerComponent, Context


app = Kyoukai("Ranobe-Honyaku", renderer="jinja2")


class Container(ContainerComponent):
    async def start(self, ctx: Context):
        self.add_component("Kyoukai", KyoukaiComponent, ip="127.0.0.1", port=4444, app=app)
        await super().start(ctx)
