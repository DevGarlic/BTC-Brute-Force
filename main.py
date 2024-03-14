from bitcoin import *
import os, aiohttp, asyncio

async def fetch_balance(session, address):
    url = f"https://blockchain.info/balance?active={address}"
    async with session.get(url) as response:
        response.raise_for_status()
        data = await response.json()
        return data[address]["final_balance"]

async def check_BTC_balance(address):
    async with aiohttp.ClientSession() as session:
        balance_satoshi = await fetch_balance(session, address)
        return balance_satoshi

async def main():
    counter = 0
    while True:
        counter += 1
        private_key = random_key()
        address = pubkey_to_address(privtopub(private_key))
        balance = await check_BTC_balance(address)

        print(f"{counter} - {address} {balance / 100000000} BTC")  # 현재 카운터 출력

        if balance > 0:
            with open("FoundWallet.txt", "a") as file:
                file_info = f"Address: {address}\nPrivateKey: {private_key}\nBalance: {balance / 100000000}\nTX: {signed_tx}\n\n"
                file.write(file_info)
                print(file_info)

asyncio.run(main())