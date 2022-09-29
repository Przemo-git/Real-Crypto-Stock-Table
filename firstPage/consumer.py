from channels.generic.websocket import AsyncWebsocketConsumer

class TableData(AsyncWebsocketConsumer):

    async def connect(self):
        self.group_name='tableData'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self,close_code):
        pass

    # #1 sprawdzenie wstępnej konf. wstępny widok def
    # async def receive(self, text_data):
    #     print(text_data)


    #chek connection
    #start server
    #in second therminal:    python -m websockets ws://localhost:8000/ws/tableData/
    #run jupiter

    async def receive(self,text_data):
        # print (text_data)
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type':'randomFunction',
                'value':text_data,
            }
        )

    async def randomFunction(self,event):
        print (event['value'])
        await self.send(event['value'])







