import asyncio
import aiohttp


the_url = input('please write the wss_url:')
number = int(input('how many messages should we send?'))


for counter in range (1 , number+1) :
    messages = []
    message = input(f'please write {counter}th message we should send:')
    messages.append(message)
    
async def main():
    async with aiohttp.ClientSession() as session :
        ws = await session.ws_connect(the_url)
         
        for message in messages :
            print(message)
            await ws.send_str(message)
            
        while True:
            msg = await ws.receive()
            
            for m in msg:
                print(m)


asyncio.run(main())